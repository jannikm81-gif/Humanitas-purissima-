import sys
import os
import unittest
import numpy as np

sys.path.append('.')

from src.oracle_resilience import PairwiseBoundedOracle

class TestPairwiseBoundedOracle(unittest.TestCase):
    def setUp(self):
        self.oracle = PairwiseBoundedOracle(gamma=0.3, similarity_threshold=0.1, cluster_limit=4, penalty_factor=0.05)
        self.true_context = np.array([0.25, 0.25, 0.25, 0.25])
        self.sybil_context = np.array([0.7, 0.1, 0.1, 0.1])

    def test_sybil_cartel_isolation(self):
        weights = np.ones(10)
        sensor_data = {}

        for i in range(4):
            sensor_data[i] = self.true_context.copy()

        for i in range(4, 10):
            sensor_data[i] = self.sybil_context.copy()

        updated_weights, trusted_context = self.oracle.update_weights(sensor_data, weights)

        dist_to_true = np.sum(np.abs(trusted_context - self.true_context))
        dist_to_sybil = np.sum(np.abs(trusted_context - self.sybil_context))
        self.assertTrue(dist_to_true < dist_to_sybil)

        for i in range(4):
            for j in range(4, 10):
                self.assertTrue(updated_weights[i] > updated_weights[j])
