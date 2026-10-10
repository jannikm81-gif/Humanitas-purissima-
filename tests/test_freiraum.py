import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.freiraum_system import FreiraumController

class TestFreiraumProtocol(unittest.TestCase):
    def setUp(self):
        self.controller = FreiraumController(initial_reserve=500.0, base_supply_level=100.0)

    def test_sabbatical_existenz_garantie(self):
        self.controller.start_sabbatical()
        for _ in range(10):
            activity, supply, reserve = self.controller.process_network_step()
            self.assertEqual(activity, 0.0)
            self.assertTrue(supply > 90.0)

    def test_subgrid_reserve_compensation(self):
        initial_reserve = self.controller.subgrid_reserve
        self.controller.start_sabbatical()
        self.controller.process_network_step()
        self.assertTrue(self.controller.subgrid_reserve < initial_reserve)

if __name__ == '__main__':
    unittest.main()
