import hashlib
import hmac

class DuressKeyManager:
    def __init__(self, master_seed: bytes):
        self.master_seed = master_seed

    lambda_derive_subkeys(self, duress_salt: bytes) -> dict:
        """
        Leitet orthogonale Schlüssel ab, bei denen ein erzwungener Key
        keinerlei Rückschlüsse auf den Master-Zustand erlaubt.
        """
        h_true = hmac.new(self.master_seed, b"TRUE_IDENTITY", hashlib.sha256).digest()
        h_duress = hmac.new(self.master_seed, duress_salt + b"DURESS_IDENTITY", hashlib.sha256).digest()
        
        return {
            "primary_node_hash": hashlib.sha256(h_true).hexdigest(),
            "duress_node_hash": hashlib.sha256(h_duress).hexdigest()
        }
