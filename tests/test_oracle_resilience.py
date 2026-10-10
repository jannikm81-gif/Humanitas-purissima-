import unittest
import numpy as np
from src.oracle_resilience import PairwiseBoundedOracle

class TestPairwiseBoundedOracle(unittest.TestCase):
    def setUp(self):
        """Initialisiert das Test-Orakel vor jedem Testlauf."""
        self.oracle = PairwiseBoundedOracle(gamma=0.3, similarity_threshold=0.1, cluster_limit=4, penalty_factor=0.05)
        self.true_context = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
        self.sybil_context = np.array([0.6, 0.1, 0.1, 0.1, 0.1])

    def test_sybil_cartel_isolation(self):
        """
        Prüft, ob das Pairwise Bounding ein 60%-Sybil-Kartell (6 von 10 Knoten)
        erfolgreich abwehrt und die ehrliche Minderheit schützt.
        """
        weights = np.ones(10)
        sensor_data = {}

        # 4 ehrliche Knoten generieren
        for i in range(4):
            sensor_data[i] = self.true_context.copy()

        # 6 bösartige Kartell-Knoten generieren (60% Mehrheit)
        for i in range(4, 10):
            sensor_data[i] = self.sybil_context.copy()

        # Führe einen Protokoll-Zeitschritt aus
        updated_weights, trusted_context = self.oracle.update_weights(sensor_data, weights)

        # INVARIANTEN-CHECK 1: Das Kartell darf den berechneten Kontext nicht dominieren.
        # Der berechnete Systemkontext muss näher am wahren Kontext liegen als an der Lüge.
        dist_to_true = np.sum(np.abs(trusted_context - self.true_context))
        dist_to_sybil = np.sum(np.abs(trusted_context - self.sybil_context))
        self.assertTrue(dist_to_true < dist_to_sybil, "Das Sybil-Kartell hat den Systemkontext manipuliert!")

        # INVARIANTEN-CHECK 2: Die Gewichte des Kartells müssen nach dem Schritt kleiner sein
        # als die Gewichte der ehrlichen, geschützten Minderheit.
        for i in range(4):
            for j in range(4, 10):
                self.assertTrue(updated_weights[i] > updated_weights[j], f"Knoten {j} (Kartell) wurde nicht ausreichend degradiert!")

if __name__ == '__main__':
    unittest.main()
