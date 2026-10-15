import unittest
import time
import os
import sys
import socket

# Zwingt Python, das Hauptverzeichnis nach Imports zu durchsuchen
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ztil_network import ZTILNetworkNode

def finde_freien_port():
    """Findet dynamisch einen freien Port im Betriebssystem."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    port = s.getsockname()[1]
    s.close()
    return port

class TestZTILNetworkIntegration(unittest.TestCase):

    def setUp(self):
        # Dynamische Ports anfordern, um 'Address already in use' zu verhindern
        self.port_a = finde_freien_port()
        self.port_b = finde_freien_port()
        
        while self.port_a == self.port_b:
            self.port_b = finde_freien_port()

        self.node_a = ZTILNetworkNode(node_id="Node_A", port=self.port_a)
        self.node_b = ZTILNetworkNode(node_id="Node_B", port=self.port_b)
        
        self.node_a.start_server()
        self.node_b.start_server()
        
        # Verbindet die Knoten im Netzwerk
        self.node_a.register_peer("Node_B", self.port_b)
        self.node_b.register_peer("Node_A", self.port_a)
        time.sleep(0.3)

    def tearDown(self):
        # Schließt die Ports nach dem Test wieder sauber
        self.node_a.shutdown()
        self.node_b.shutdown()
        time.sleep(0.2)

    def test_normaler_p2p_nachrichtenfluss(self):
        """Prüft, ob Daten im Normalzustand fehlerfrei fließen."""
        erfolg = self.node_a.send_message("Node_B", "Hallo Welt")
        self.assertTrue(erfolg)
        time.sleep(0.3)
        
        self.assertEqual(len(self.node_b.received_messages), 1)
        self.assertEqual(self.node_b.received_messages[0]["payload"], "Hallo Welt")

    def test_ztil_isolation_bei_angriff(self):
        """Prüft, ob das ZTIL-Abschaltventil bei einem Angriff sofort trennt."""
        self.node_b.send_message("Node_A", "SIG_STATE_ATTACK")
        time.sleep(0.3)
        
        self.assertTrue(self.node_a.is_isolated)
        self.assertEqual(len(self.node_a.peers), 0)
        
        # Ein isolierter Knoten darf nicht mehr senden können
        erfolg = self.node_a.send_message("Node_B", "Versuchter Ausbruch")
        self.assertFalse(erfolg)

if __name__ == '__main__':
    unittest.main()
