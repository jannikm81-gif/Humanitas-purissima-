import hashlib
import hmac
import os
from typing import Tuple
def hkdf_extract(salt: bytes, ikm: bytes) -> bytes:
"""Master Key Extraction via HMAC-SHA256."""
return hmac.new(salt, ikm, hashlib.sha256).digest()
def hkdf_expand(prk: bytes, info: bytes, length: int = 32) -> bytes:
"""Derives sub-keys based on domain separation tags."""
return hmac.new(prk, info + b"\x01", hashlib.sha256).digest()[:length]
def derive_dkdp_keys(
master_entropy: bytes, salt: bytes = b"HP_DKDP_v10_SALT"
) -> Tuple[bytes, bytes]:
"""Generiert zwei kryptografisch orthogonale Schluessel K_real und K_duress."""
prk = hkdf_extract(salt, master_entropy)
k_real = hkdf_expand(prk, b"HP_REAL_KEY_DERIVATION", 32)
k_duress = hkdf_expand(prk, b"HP_DURESS_KEY_DERIVATION", 32)
return k_real, k_duress
def verify_pin_and_execute(
pin_entered: str, pin_real: str, pin_duress: str, master_entropy: bytes
) -> dict:
"""Authentifiziert die Eingabe zeitsicher und schaltet den entsprechenden Pfad frei."""
k_real, k_duress = derive_dkdp_keys(master_entropy)
# Constant-time comparison gegen Side-Channel-Angriffe
if hmac.compare_digest(pin_entered, pin_real):
return {
"status": "REAL_ACCESS",
"active_key_hash": hashlib.sha256(k_real).hexdigest()[:16],
"ui_mode": "V_Real (Vollzugriff)",
"timelock_alert_triggered": False,
}
elif hmac.compare_digest(pin_entered, pin_duress):
return {
"status": "DURESS_ACCESS",
"active_key_hash": hashlib.sha256(k_duress).hexdigest()[:16],
"ui_mode": "V_Schein (Tarnoberflaeche)",
"timelock_alert_triggered": True,
"alert_delay_minutes": 10,
}
else:
return {"status": "INVALID_PIN", "ui_mode": "Access Denied"}
if name == "main":
print("=== Humanitas Purissima - DKDP Prototype ===")
# Simulation einer 256-Bit Master-Entropie
seed = os.urandom(32)
PIN_REAL = "1234"
PIN_DURESS = "9999"
print("\n[1] Test: Reguläre Authentifizierung (Echt-PIN)")
res_real = verify_pin_and_execute(PIN_REAL, PIN_REAL, PIN_DURESS, seed)
print(f"Status: {res_real['status']}")
print(f"UI-Modus: {res_real['ui_mode']}")
print(f"Schlüssel-Hash: {res_real['active_key_hash']}")
print("\n[2] Test: Nötigungsfall (Duress-PIN)")
res_duress = verify_pin_and_execute(PIN_DURESS, PIN_REAL, PIN_DURESS, seed)
print(f"Status: {res_duress['status']}")
print(f"UI-Modus: {res_duress['ui_mode']}")
print(f"Schlüssel-Hash: {res_duress['active_key_hash']}")
print(f"Stummer Alarm (Time-Lock Queue): {res_duress['timelock_alert_triggered']}")
