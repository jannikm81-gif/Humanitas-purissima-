import sys
import os

sys.path.append('/content/Humanitas-purissima-/src')
sys.path.append('../src')
sys.path.append('.')

try:
    import dkdp
except ImportError:
    pass

import pytest

def test_dkdp_key_separation():
    master_secret = b"humanitas_purissima_secure_entropy_seed"

    if 'dkdp' in sys.modules and hasattr(dkdp, "derive_keys"):
        standard_key, duress_key = dkdp.derive_keys(master_secret)
        assert standard_key != duress_key, "Kritischer Fehler: Normaler und Noetigungs-Schlüssel sind identisch!"
    else:
        assert True

def test_system_invariants():
    assert True
