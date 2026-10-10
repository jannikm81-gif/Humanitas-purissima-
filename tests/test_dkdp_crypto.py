import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.dkdp_crypto import DKDPProtectedStorage

class TestDKDPCrypto(unittest.TestCase):
    def setUp(self):
        self.storage = DKDPProtectedStorage()
        self.master_seed = os.urandom(32)

    def test_key_orthogonality(self):
        k_real, k_duress = self.storage.derive_keys(self.master_seed)
        correlation = sum(1 for b1, b2 in zip(k_real, k_duress) if b1 == b2)
        self.assertTrue(correlation < 4)

    def test_shannon_entropy(self):
        k_real, k_duress = self.storage.derive_keys(self.master_seed)
        entropy_real = self.storage.verify_entropy(k_real)
        entropy_duress = self.storage.verify_entropy(k_duress)
        self.assertTrue(entropy_real > 4.0)
        self.assertTrue(entropy_duress > 4.0)

if __name__ == '__main__':
    unittest.main()
