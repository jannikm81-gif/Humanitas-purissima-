import numpy as np
import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.wealth_economy import WealthEconomyController

class TestWealthEconomy(unittest.TestCase):

    def test_echter_bpw_gradienten_kollaps_bei_raubbau(self):
        controller = WealthEconomyController()
        gradient_normal = controller.calculate_bpw_gradient()
        self.assertTrue(gradient_normal > 0.0)

        controller.update_ecological_index(-50.0)
        gradient_kollaps = controller.calculate_bpw_gradient()
        self.assertEqual(gradient_kollaps, 0.0)

if __name__ == '__main__':
    unittest.main()
