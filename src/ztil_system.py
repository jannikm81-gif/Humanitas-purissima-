import numpy as np

class ZTILController:
    def __init__(self, node_id, capacity=100):
        """
        Initialisiert eine physische Infrastruktur-Einheit nach Artikel III.
        """
        self.node_id = node_id
        self.capacity = capacity
        self.utility = capacity
        self.is_compromised = False
        self.ztil_activated = False
        self.connected_peers = set()

    def register_peer(self, peer_node_id):
        """
        Vernetzt den Knoten innerhalb des lokalen Sub-Grids.
        """
        if peer_node_id != self.node_id:
            self.connected_peers.add(peer_node_id)

    def trigger_security_alarm(self):
        """
        Löst das physische Notfall-Protokoll bei erkannter Aggression aus.
        """
        self.is_compromised = True
        self._activate_zero_utility_lock()

    def _activate_zero_utility_lock(self):
        """
        Invariante: Nutzen faellt auf 0, alle logischen Verbindungen werden gekappt.
        """
        self.ztil_activated = True
        self.utility = 0
        self.connected_peers.clear()

    def verify_grid_integrity(self, active_grid_nodes):
        """
        Dynamic Network Partitioning: Berechnet die verbleibende Leistung des freien Sub-Grids.
        """
        total_utility = sum(node.utility for node in active_grid_nodes if not node.ztil_activated)
        return total_utility
