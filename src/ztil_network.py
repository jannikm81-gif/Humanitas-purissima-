import socket
import threading
import time
import json

class ZTILNetworkNode:
    def __init__(self, node_id, port):
        self.node_id = node_id
        self.port = port
        self.host = '127.0.0.1' # Lokaler Host für die Simulation
        self.peers = {}         # Gespeicherte Verbindungen zu anderen Knoten {node_id: port}
        self.is_isolated = False
        self.received_messages = []
        self.server_socket = None
        self.running = True

    def start_server(self):
        """Startet den Hintergrund-Server des Knotens, um Nachrichten zu empfangen."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Ermöglicht das schnelle Wiederverwenden des Ports bei Tests
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

        def listen_loop():
            while self.running:
                try:
                    self.server_socket.settimeout(0.5)
                    client_conn, _ = self.server_socket.accept()
                    data = client_conn.recv(1024).decode('utf-8')
                    if data:
                        msg = json.loads(data)
                        self._verarbeite_nachricht(msg)
                    client_conn.close()
                except socket.timeout:
                    continue
                except Exception:
                    break

        threading.Thread(target=listen_loop, daemon=True).start()

    def register_peer(self, peer_id, peer_port):
        """Registriert einen Nachbarknoten im Sub-Grid."""
        self.peers[peer_id] = peer_port

    def send_message(self, target_id, payload):
        """Sendet eine verschlüsselte/strukturierte Nachricht an einen Peer, außer bei Isolation."""
        if self.is_isolated:
            return False # ZTIL-Sperre blockiert jeglichen Ausgang

        if target_id in self.peers:
            try:
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect((self.host, self.peers[target_id]))
                msg = {
                    "sender_id": self.node_id,
                    "payload": payload,
                    "timestamp": time.time()
                }
                client_socket.send(json.dumps(msg).encode('utf-8'))
                client_socket.close()
                return True
            except Exception:
                return False
        return False

    def _verarbeite_nachricht(self, msg):
        """Interne Logik: Erkennt Angriffe und löst das Isolation Lock aus."""
        if self.is_isolated:
            return # Isolierte Knoten verarbeiten nichts mehr

        # Wenn die Nachricht als kompromittiert markiert ist (Staatsangriff-Simulation)
        if msg["payload"] == "SIG_STATE_ATTACK":
            self.trigger_ztil_lock()
        else:
            self.received_messages.append(msg)

    def trigger_ztil_lock(self):
        """Das physikalische Abschaltventil: Trennt den Knoten augenblicklich vom Netz."""
        self.is_isolated = True
        self.peers = {} # Löscht alle Verbindungen sofort (Zero-Utility)

    def shutdown(self):
        """Beendet den Knoten sauber."""
        self.running = False
        if self.server_socket:
            self.server_socket.close()
