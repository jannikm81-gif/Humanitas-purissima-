import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ztil_system import ZTILController

class TestZTILSystem(unittest.TestCase):
    def setUp(self):
        self.nodes = [ZTILController(node_id=i, capacity=100) for i in range(5)]
        for node in self.nodes:
            for peer in self.nodes:
                node.register_peer(peer.node_id)

    def test_hardware_destruction_on_aggression(self):
        target_node = self.nodes[0]
        target_node.trigger_security_alarm()
        self.assertEqual(target_node.utility, 0)
        self.assertEqual(len(target_node.connected_peers), 0)

    def test_dynamic_network_partitioning(self):
        self.nodes[4].trigger_security_alarm()
        remaining_utility = self.nodes[0].verify_grid_integrity(self.nodes)
        self.assertEqual(remaining_utility, 400)

if __name__ == '__main__':
    unittest.main()
