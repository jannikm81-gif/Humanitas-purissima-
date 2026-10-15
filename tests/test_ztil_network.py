import unittest
import time
import os
import sys

# Zwingt Python, das Hauptverzeichnis nach Imports zu durchsuchen
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ztil_network import ZTILNetworkNode

class TestZTILNetworkIntegration(unittest.TestCase):

    def setUp(self):
        # Startet zwei echte, simulierte Knoten auf deinem System
        self.node_a = ZTILNetworkNode(node_id="Node_A", port=9001)
        self.node_b = ZTILNetworkNode(node_id="Node_B", port=9002)
        
        self.node_a.start_server()
        self.node_b.start_server()
        
        # Verbindet die Knoten im Netzwerk
        self.node_a.register_peer("Node_B", 9002)
        self.node_b.register_peer("Node_A", 9001)
        time.sleep(0.2)

    def tearDown(self):
        # Schließt die Ports nach dem Test wieder sauber
        self.node_a.shutdown()
        self.node_b.shutdown()
        time.sleep(0.1)

    def test_normaler_p2p_nachrichtenfluss(self):
        """Prüft, ob Daten im Normalzustand fehlerfrei fließen."""
        erfolg = self.node_a.send_message("Node_B", "Hallo Welt")
        self.assertTrue(erfolg)
        time.sleep(0.2)
        
        self.assertEqual(len(self.node_b.received_messages), 1)
        # HIER WAR DER FEHLER: Greift jetzt korrekt auf das erste Element der Liste zu
        self.assertEqual(self.node_b.received_messages[0]["payload"], "Hallo Welt")

    def test_ztil_isolation_bei_angriff(self):
        """Prüft, ob das ZTIL-Abschaltventil bei einem Angriff sofort trennt."""
        self.node_b.send_message("Node_A", "SIG_STATE_ATTACK")
        time.sleep(0.2)
        
        self.assertTrue(self.node_a.is_isolated)
        self.assertEqual(len(self.node_a.peers), 0)
        
        # Ein isolierter Knoten darf nicht mehr senden können
        erfolg = self.node_a.send_message("Node_B", "Versuchter Ausbruch")
        self.assertFalse(erfolg)

if __name__ == '__main__':
    unittest.main()
