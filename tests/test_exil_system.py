import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
import json
import ed25519
from src.exil_system import ExilVoucherSystem

class TestExilSystem(unittest.TestCase):
    def setUp(self):
        """Generiert Schlüssel und System-Instanz vor jedem Testlauf."""
        self.system = ExilVoucherSystem()
        self.sk_subgrid, self.pk_subgrid = ed25519.create_keypair()
        self.user_id = "HP-SSI-USER-TEST"

    def test_legitimate_offline_voucher(self):
        """Prüft, ob ein echter Voucher komplett offline erfolgreich validiert wird."""
        voucher = self.system.create_voucher(self.sk_subgrid, self.user_id, resource_units=150)
        
        # INVARIANTEN-CHECK 1: Der echte Voucher muss anstandslos durchgehen
        success, message = self.system.verify_voucher(voucher, self.pk_subgrid)
        self.assertTrue(success, f"Fehler: Gültiger Voucher wurde abgewiesen! {message}")
        self.assertIn("150 Einheiten", message)

    def test_forged_voucher_detection(self):
        """Stellt sicher, dass jegliche nachträgliche Fälschung hart blockiert wird."""
        voucher = self.system.create_voucher(self.sk_subgrid, self.user_id, resource_units=150)
        
        # Angreifer versucht die Ressourceneinheiten heimlich anzuheben
        forged_voucher = json.loads(json.dumps(voucher))
        forged_voucher["payload"]["resource_units"] = 99999
        
        # INVARIANTEN-CHECK 2: Die manipulierte Signatur muss auffallen
        success, message = self.system.verify_voucher(forged_voucher, self.pk_subgrid)
        self.assertFalse(success, "Kritischer Fehler: Manipulierter Voucher wurde fälschlicherweise akzeptiert!")
        self.assertEqual(message, "Kryptografische Faelschung erkannt")

if __name__ == '__main__':
    unittest.main()
