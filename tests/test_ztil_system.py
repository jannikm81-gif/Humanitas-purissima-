import numpy as np
import unittest

def berechne_ztil_end_utility(staats_angriff, angriffs_zeitpunkt, sperr_haerte):
    """Numerische Hilfsfunktion zur Abbildung der ZTIL-Kerninvariante."""
    zeit = np.linspace(0, 200, 200)
    staats_kollektiv = np.ones(200) * 100.0
    
    if staats_angriff:
        for i, t in enumerate(zeit):
            if t >= angriffs_zeitpunkt:
                dt = t - angriffs_zeitpunkt
                staats_kollektiv[i] = max(0, 100.0 - dt * (sperr_haerte * 0.8))
    return staats_kollektiv[-1]

class TestZTILSystem(unittest.TestCase):

    def test_ztil_isolation_kollaps(self):
        """Überprüft, ob das kollektive Sub-Grid bei maximaler Sperrhärte gegen Null gedrückt wird."""
        end_utility = berechne_ztil_end_utility(staats_angriff=True, angriffs_zeitpunkt=50, sperr_haerte=10.0)
        self.assertEqual(end_utility, 0.0, "Die Utility des angegriffenen Kollektivs muss isoliert (0) sein.")

    def test_ztil_normalzustand(self):
        """Überprüft, ob das System ohne Angriffsvektor stabil auf Maximalwert verbleibt."""
        end_utility = berechne_ztil_end_utility(staats_angriff=False, angriffs_zeitpunkt=50, sperr_haerte=6.0)
        self.assertEqual(end_utility, 100.0, "Ohne strukturellen Angriff darf keine Utility-Absenkung stattfinden.")

if __name__ == '__main__':
    unittest.main()

