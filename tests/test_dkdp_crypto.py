import unittest
import os
from src.dkdp_crypto import DKDPProtectedStorage

class TestDKDPCrypto(unittest.TestCase):
    def setUp(self):
        """Initialisiert das DKDP-Modul vor jedem Testlauf."""
        self.storage = DKDPProtectedStorage()
        self.master_seed = os.urandom(32)

    def test_key_orthogonality(self):
        """Prüft, ob die abgeleiteten Schlüssel mathematisch orthogonal sind."""
        k_real, k_duress = self.storage.derive_keys(self.master_seed)
        
        # INVARIANTEN-CHECK 1: Die Schlüssel dürfen an identischen Positionen keine Übereinstimmung haben
        correlation = sum(1 for b1, b2 in zip(k_real, k_duress) if b1 == b2)
        self.assertTrue(correlation < 4, "Kritischer Fehler: Zu hohe Korrelation zwischen Real- und Duress-Key!")

    def test_shannon_entropy(self):
        """Überprüft, ob die abgeleiteten Schlüssel ununterscheidbar von Rauschen sind."""
        k_real, k_duress = self.storage.derive_keys(self.master_seed)
        
        entropy_real = self.storage.verify_entropy(k_real)
        entropy_duress = self.storage.verify_entropy(k_duress)
        
        # INVARIANTEN-CHECK 2: Die Entropie muss hoch genug sein, um als Zufall zu gelten
        self.assertTrue(entropy_real > 4.0, "Muster im Real-Key erkannt! Entropie zu niedrig.")
        self.assertTrue(entropy_duress > 4.0, "Muster im Duress-Key erkannt! Entropie zu niedrig.")

if __name__ == '__main__':
    unittest.main()
