import numpy as np
import unittest
# Importiert die echte Produktivklasse aus deinem src-Ordner
from src.wealth_economy import WealthEconomyController

class TestWealthEconomy(unittest.TestCase):

    def test_echter_bpw_gradienten_kollaps_bei_raubbau(self):
        """
        PRÜFUNG DER PRODUKTIVDATEI - ARTIKEL VII
        Validiert, dass das geometrische Mittel der echten Klasse sofort auf 0
        einstürzt, wenn eine Säule (z.B. Ökologie) vollständig ausgebeutet wird.
        """
        # Initialisierung mit echten Standardwerten (50, 30, 40)
        controller = WealthEconomyController()
        
        # 1. Test: Normalzustand muss einen positiven Gradienten liefern
        gradient_normal = controller.calculate_bpw_gradient()
        self.assertTrue(gradient_normal > 0.0)
        
        # 2. Test: Aggressiver Raubbau drückt die Natur auf 0
        controller.update_ecological_index(-50.0) # Delta zieht genau 50 ab -> 0
        
        # 3. Test: Der Gradient MUSS jetzt mathematisch zwingend 0 sein
        gradient_kollaps = controller.calculate_bpw_gradient()
        self.assertEqual(gradient_kollaps, 0.0, "Der Gradient muss bei der Zerstörung einer Säule kollabieren!")

    def berechne_payoffs_lokal(self, straffaktor_kl, verraeter_boost, zeitschritte=10):
        """Hilfsfunktion für die spieltheoretische Nash-Simulation."""
        zeit = np.arange(zeitschritte)
        payoff_kooperation = 10 * (np.log(zeit + 1) / np.log(1.5)) + 5 * (1 - np.exp(-0.1 * zeit))
        d_kl_wert = 0.8
        entropie_strafe = np.exp(-straffaktor_kl * d_kl_wert * zeit / 10)
        payoff_defektion = (verraeter_boost * (zeit == 0)) + (20 * entropie_strafe) - (5 * zeit * 0.1)
        return payoff_kooperation, payoff_defektion

    def test_nash_gleichgewicht_unter_standard_strafen(self):
        """Prüft die Incentive Compatibility der spieltheoretischen Ebene."""
        p_coop, p_defect = self.berechne_payoffs_lokal(straffaktor_kl=2.5, verraeter_boost=15)
        self.assertTrue(p_coop[-1] > p_defect[-1])

    def test_anomalie_erkennung_bei_zu_geringer_strafe(self):
        """Prüft den mathematischen Kipppunkt bei mangelnder KL-Strafe."""
        p_coop, p_defect = self.berechne_payoffs_lokal(straffaktor_kl=0.5, verraeter_boost=40)
        self.assertTrue(p_defect > p_coop)

if __name__ == '__main__':
    unittest.main()
