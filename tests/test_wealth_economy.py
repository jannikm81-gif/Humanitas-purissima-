import numpy as np
import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(file), '..')))

from src.wealth_economy import WealthEconomyController

class TestWealthEconomy(unittest.TestCase):

def test_echter_bpw_gradienten_kollaps_bei_raubbau(self):
controller = WealthEconomyController()
gradient_normal = controller.calculate_bpw_gradient()
self.assertTrue(gradient_normal > 0.0)

controller.update_ecological_index(-50.0)
gradient_kollaps = controller.calculate_bpw_gradient()
self.assertEqual(gradient_kollaps, 0.0)

def berechne_payoffs_lokal(self, straffaktor_kl, verraeter_boost, zeitschritte=10):
zeit = np.arange(zeitschritte)
payoff_kooperation = 10 * (np.log(zeit + 1) / np.log(1.5)) + 5 * (1 - np.exp(-0.1 * zeit))

d_kl_wert = 0.8
entropie_strafe = np.exp(-straffaktor_kl * d_kl_wert * zeit / 10)
payoff_defektion = (verraeter_boost * (zeit == 0)) + (20 * entropie_strafe) - (5 * zeit * 0.1)
return payoff_kooperation, payoff_defektion

def test_nash_gleichgewicht_unter_standard_strafen(self):
p_coop, p_defect = self.berechne_payoffs_lokal(straffaktor_kl=2.5, verraeter_boost=15)
self.assertTrue(p_coop[-1] > p_defect[-1])

def test_anomalie_erkennung_bei_zu_geringer_strafe(self):
p_coop, p_defect = self.berechne_payoffs_lokal(straffaktor_kl=0.5, verraeter_boost=40)
self.assertTrue(p_defect[-1] > p_coop[-1])

if name == 'main':
unittest.main()



