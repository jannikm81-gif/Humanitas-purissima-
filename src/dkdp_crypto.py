import os
import hashlib
import hmac
import math
from collections import Counter

class DKDPProtectedStorage:
    def __init__(self, salt_real=b"HP_v10_REAL_SALT", salt_duress=b"HP_v10_DURESS_SALT"):
        """
        Initialisiert das Dual-Key Derivationsprotokoll nach Artikel IV.
        """
        self.salt_real = salt_real
        self.salt_duress = salt_duress

    @staticmethod
    def _hkdf_extract(salt, input_key_material):
        """
        Kryptografische Extraktionsstufe (PRK-Generierung via HMAC-SHA256).
        """
        if salt is None:
            salt = b'\x00' * 32
        return hmac.new(salt, input_key_material, hashlib.sha256).digest()

    @staticmethod
    def _hkdf_expand(prk, info, length=32):
        """
        Kryptografische Expansionsstufe zur Schlüsselableitung.
        """
        t = b""
        okm = b""
        i = 1
        while len(okm) < length:
            t = hmac.new(prk, t + info + bytes([i]), hashlib.sha256).digest()
            okm += t
            i += 1
        return okm[:length]

    def derive_keys(self, master_entropy):
        """
        Generiert zwei mathematisch orthogonale 256-Bit Schluessel aus einer Master-Entropie.
        Aus Kenntnis von K_Duress ist K_Real rechnerisch nicht nachweisbar.
        """
        prk_real = self._hkdf_extract(self.salt_real, master_entropy)
        prk_duress = self._hkdf_extract(self.salt_duress, master_entropy)
        
        k_real = self._hkdf_expand(prk_real, b"Real_Access_Key", 32)
        k_duress = self._hkdf_expand(prk_duress, b"Duress_Access_Key", 32)
        
        return k_real, k_duress

    @staticmethod
    def verify_entropy(key_bytes):
        """
        Berechnet die Shannon-Entropie des Schluessels zur Überprüfung auf statistische Muster.
        Ein perfekter kryptografischer Schluessel nähert sich 8.0 Bit/Byte an.
        """
        if not key_bytes:
            return 0.0
        total_len = len(key_bytes)
        counts = Counter(key_bytes)
        entropy = 0.0
        for count in counts.values():
            p = count / total_len
            entropy -= p * math.log2(p)
        return entropy
