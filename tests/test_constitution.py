import sys
import os
import unittest
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.constitution_governance import ConstitutionGovernance

class TestConstitutionGovernance(unittest.TestCase):
    def setUp(self):
        self.gov = ConstitutionGovernance()

    def test_layer_0_unantastbarkeit(self):
        success, message = self.gov.propose_parameter_change("unbedingte_privatsphaere", False)
        self.assertFalse(success)

    def test_layer_1_timelock_enforcement(self):
        self.gov.propose_parameter_change("sabbatical_max_weeks", 52)
        now = int(time.time())
        five_days_later = now + (5 * 24 * 60 * 60)
        success_exec, message_exec = self.gov.execute_parameter_change("sabbatical_max_weeks", simulated_time=five_days_later)
        self.assertFalse(success_exec)

    def test_legitimate_parameter_evolution(self):
        self.gov.propose_parameter_change("sabbatical_max_weeks", 52)
        now = int(time.time())
        one_hundred_twenty_one_days_later = now + (121 * 24 * 60 * 60)
        success_exec, message_exec = self.gov.execute_parameter_change("sabbatical_max_weeks", simulated_time=one_hundred_twenty_one_days_later)
        self.assertTrue(success_exec)

if __name__ == '__main__':
    unittest.main()
