import unittest
import time
from src.constitution_governance import ConstitutionGovernance

class TestConstitutionGovernance(unittest.TestCase):
    def setUp(self):
        """Initialisiert die Verfassung vor jedem Testlauf."""
        self.gov = ConstitutionGovernance()

    def test_layer_0_unantastbarkeit(self):
        """Stellt sicher, dass Ebene-0-Grundrechte absolut unveraenderlich sind."""
        # INVARIANTEN-CHECK 1: Versuch, ein unumstößliches Recht zu manipulieren, muss fehlschlagen
        success, message = self.gov.propose_parameter_change("unbedingte_privatsphaere", False)
        self.assertFalse(success, "Kritischer Fehler: Aenderungsvorschlag fuer Ebene 0 wurde faelschlicherweise akzeptiert!")
        self.assertIn("absolut unzulaessig", message)

    def test_layer_1_timelock_enforcement(self):
        """Beweist, dass der 120-Tage Timelock vorzeitige Aenderungen hart abweist."""
        # Legitimen Parameter zur Aenderung einreichen
        success_reg, msg_reg = self.gov.propose_parameter_change("sabbatical_max_weeks", 52)
        self.assertTrue(success_reg)
        
        # Simuliere einen illegalen Ausfuehrungsversuch nach nur 5 Tagen
        now = int(time.time())
        five_days_later = now + (5 * 24 * 60 * 60)
        
        # INVARIANTEN-CHECK 2: Ausführung vor Ablauf des Timelocks muss abgewiesen werden
        success_exec, message_exec = self.gov.execute_parameter_change("sabbatical_max_weeks", simulated_time=five_days_later)
        self.assertFalse(success_exec, "Kritischer Fehler: Timelock wurde vor Ablauf der Frist gebrochen!")
        self.assertIn("Sperrfrist aktiv", message_exec)

    def test_legitimate_parameter_evolution(self):
        """Prueft, ob die Parameter-Evolution nach regulaerem Ablauf des Timelocks klappt."""
        self.gov.propose_parameter_change("sabbatical_max_weeks", 52)
        
        # Simuliere die Ausfuehrung nach 121 Tagen
        now = int(time.time())
        one_hundred_twenty_one_days_later = now + (121 * 24 * 60 * 60)
        
        # INVARIANTEN-CHECK 3: Nach Ablauf der Frist muss der Parameter aktualisiert werden
        success_exec, message_exec = self.gov.execute_parameter_change("sabbatical_max_weeks", simulated_time=one_hundred_twenty_one_days_later)
        self.assertTrue(success_exec, f"Fehler: Legitime Aenderung nach Timelock wurde blockiert: {message_exec}")
        self.assertEqual(self.gov.layer_1_parameters["sabbatical_max_weeks"], 52)

if __name__ == '__main__':
    unittest.main()
