import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from src.ztil_system import ZTILController

class TestZTILSystem(unittest.TestCase):
    def setUp(self):
        """Erstellt ein Test-Grid aus Infrastrukturknoten vor jedem Lauf."""
        self.nodes = [ZTILController(node_id=i, capacity=100) for i in range(5)]
        
        # Knoten miteinander vernetzen
        for node in self.nodes:
            for peer in self.nodes:
                node.register_peer(peer.node_id)

    def test_hardware_destruction_on_aggression(self):
        """Überprüft, ob der angegriffene Knoten sofort entwertet wird."""
        target_node = self.nodes[4]
        
        # Physischen Angriff auslösen
        target_node.trigger_security_alarm()
        
        # INVARIANTEN-CHECK 1: Der Nutzen der Hardware muss exakt 0 sein
        self.assertEqual(target_node.utility, 0, "Kritischer Fehler: ZTIL hat die Hardware nicht entwertet!")
        
        # INVARIANTEN-CHECK 2: Alle Verbindungen des Knotens müssen gekappt sein
        self.assertEqual(len(target_node.connected_peers), 0, "Knoten ist nach ZTIL noch vernetzt!")

    def test_dynamic_network_partitioning(self):
        """Prüft, ob das verbleibende freie Sub-Grid voll funktionsfähig bleibt."""
        # Knoten 4 fällt durch Aggression aus
        self.nodes[4].trigger_security_alarm()
        
        # Integrität des Gesamtsystems über den Controller prüfen
        remaining_utility = self.nodes[0].verify_grid_integrity(self.nodes)
        
        # INVARIANTEN-CHECK 3: Die restlichen 4 Knoten müssen stabil weiterarbeiten (4 * 100)
        self.assertEqual(remaining_utility, 400, "Das freie Sub-Grid wurde durch die Partitionierung beschädigt!")

if __name__ == '__main__':
    unittest.main()
