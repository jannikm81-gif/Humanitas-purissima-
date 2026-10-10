import unittest
from src.freiraum_system import FreiraumController

class TestFreiraumProtocol(unittest.TestCase):
    def setUp(self):
        """Initialisiert den Freiraum-Controller vor jedem Testlauf."""
        self.controller = FreiraumController(initial_reserve=500.0, base_supply_level=100.0)

    def test_sabbatical_existenz_garantie(self):
        """Beweist, dass die Grundversorgung im Sabbatical geschützt bleibt."""
        self.controller.start_sabbatical()
        
        # Simuliere 10 Zeitschritte im Sabbatical
        for _ in range(10):
            activity, supply, reserve = self.controller.process_network_step()
            
            # INVARIANTEN-CHECK 1: Aktivität muss absolut 0 sein
            self.assertEqual(activity, 0.0, "Nutzer hat trotz Sabbatical aktive Netzwerk-Beteiligung!")
            
            # INVARIANTEN-CHECK 2: Die Grundversorgung darf niemals massiv einbrechen (muss > 90% bleiben)
            self.assertTrue(supply > 90.0, f"Kritischer Fehler: Grundversorgung im Sabbatical zu stark gedämpft: {supply}!")

    def test_subgrid_reserve_compensation(self):
        """Prüft, ob die kollektive Reserve den Ausfall mathematisch sauber auffängt."""
        initial_reserve = self.controller.subgrid_reserve
        self.controller.start_sabbatical()
        
        # Einen Schritt ausführen
        _, _, reserve_after_step = self.controller.process_network_step()
        
        # INVARIANTEN-CHECK 3: Die Reserve muss plangemäß gesunken sein, um das Individuum zu puffern
        self.assertTrue(reserve_after_step < initial_reserve, "Das Kollektiv hat den Ausfall nicht über die Reserve ausgeglichen!")

    def test_reintegration_recovery(self):
        """Überprüft die automatische Regeneration nach der Rückkehr aus der Auszeit."""
        self.controller.start_sabbatical()
        self.controller.process_network_step()
        
        # Sabbatical beenden und Normalbetrieb simulieren
        self.controller.end_sabbatical()
        _, supply, reserve = self.controller.process_network_step()
        
        # INVARIANTEN-CHECK 4: Werte müssen sofort wieder nach oben tendieren
        self.assertEqual(supply, 100.0, "Grundversorgung hat sich nach Sabbatical-Ende nicht erholt!")

if __name__ == '__main__':
    unittest.main()
