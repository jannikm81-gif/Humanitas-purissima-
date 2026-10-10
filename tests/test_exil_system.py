import sys
import os
import unittest
import json
import ed25519

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.exil_system import ExilVoucherSystem

class TestExilSystem(unittest.TestCase):
    def setUp(self):
        self.system = ExilVoucherSystem()
        self.sk_subgrid, self.pk_subgrid = ed25519.create_keypair()
        self.user_id = "HP-SSI-USER-TEST"

    def test_legitimate_offline_voucher(self):
        voucher = self.system.create_voucher(self.sk_subgrid, self.user_id, resource_units=150)
        success, message = self.system.verify_voucher(voucher, self.pk_subgrid)
        self.assertTrue(success)

    def test_forged_voucher_detection(self):
        voucher = self.system.create_voucher(self.sk_subgrid, self.user_id, resource_units=150)
        forged_voucher = json.loads(json.dumps(voucher))
        forged_voucher["payload"]["resource_units"] = 99999
        success, message = self.system.verify_voucher(forged_voucher, self.pk_subgrid)
        self.assertFalse(success)

if __name__ == '__main__':
    unittest.main()
