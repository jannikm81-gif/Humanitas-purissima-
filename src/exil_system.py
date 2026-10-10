import json
import time

try:
    import ed25519
except ImportError:
    # Fallback-Hinweis, falls die Bibliothek auf dem Zielknoten noch fehlt
    ed25519 = None

class ExilVoucherSystem:
    def __init__(self):
        """
        Initialisiert das Offline-Voucher-Protokoll nach Artikel V.
        """
        if ed25519 is None:
            raise ImportError("Die Bibliothek 'ed25519' wird fuer dieses kryptografische Modul benoetigt.")

    def create_voucher(self, issuer_private_key, user_id, resource_units, expiry_hours=72):
        """
        Generiert einen kryptografisch signierten Offline-Voucher. Läuft zu 100% offline.
        """
        current_time = int(time.time())
        payload = {
            "protocol": "HP-v10-Ebene0",
            "dissident_id": user_id,
            "resource_units": resource_units,
            "expires_at": current_time + (expiry_hours * 3600)
        }
        
        # Normierte Serialisierung fuer eine konsistente Signatur-Verifikation
        serialized_payload = json.dumps(payload, sort_keys=True).encode('utf-8')
        signature = issuer_private_key.sign(serialized_payload)
        
        return {
            "payload": payload,
            "signature_hex": signature.hex()
        }

    def verify_voucher(self, voucher_ticket, issuer_public_key):
        """
        Prueft die mathematische Integritaet und Gueltigkeit des Vouchers ohne Netzanbindung.
        """
        payload = voucher_ticket["payload"]
        signature = bytes.fromhex(voucher_ticket["signature_hex"])
        serialized_payload = json.dumps(payload, sort_keys=True).encode('utf-8')
        
        # 1. Zeitliche Invarianten-Pruefung
        if int(time.time()) > payload["expires_at"]:
            return False, "Voucher abgelaufen"
            
        # 2. Asymmetrische Signatur-Pruefung
        try:
            issuer_public_key.verify(signature, serialized_payload)
            return True, f"Validiert. {payload['resource_units']} Einheiten freigegeben."
        except Exception:
            return False, "Kryptografische Faelschung erkannt"
