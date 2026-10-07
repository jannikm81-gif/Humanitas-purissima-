import numpy as np
from src.oracle import AdversarialOracle

def test_oracle_kl_divergence():
    oracle = AdversarialOracle()
    
    # Referenzverteilung (erwartetes, normales Verhalten)
    p = np.array([0.7, 0.2, 0.1])
    
    # Beobachtete Verteilung (ähnliches Verhalten -> geringe Abweichung)
    q_normal = np.array([0.65, 0.25, 0.1])
    
    # Beobachtete Verteilung (anomales/adversarielles Verhalten -> hohe Abweichung)
    q_malicious = np.array([0.05, 0.05, 0.9])
    
    kl_normal = oracle.compute_kl_divergence(p, q_normal)
    kl_malicious = oracle.compute_kl_divergence(p, q_malicious)
    
    print(f"KL-Divergence (Normal): {kl_normal:.4f}")
    print(f"KL-Divergence (Malicious): {kl_malicious:.4f}")
    
    assert kl_normal < kl_malicious, "Normale Abweichung sollte geringer sein als bei Anomalien!"

def test_weight_decay():
    oracle = AdversarialOracle(gamma=0.5)
    
    kl_div = 2.0
    weight = oracle.calculate_weight_decay(kl_div)
    
    print(f"Gewichts-Decay bei KL={kl_div}: {weight:.4f}")
    assert 0.0 <= weight <= 1.0, "Das Gewicht muss im Intervall [0, 1] liegen."

if __name__ == "__main__":
    test_oracle_kl_divergence()
    test_weight_decay()
    print("Alle Orakel-Tests erfolgreich bestanden!")
