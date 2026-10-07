import numpy as np

class AdversarialOracle:
    def __init__(self, gamma: float = 0.5, epsilon: float = 1e-10):
        """
        Initialisiert das Orakel für die adversarielle Resilienz.
        :5param gamma: Dämpfungsfaktor für den Gewichts-Decay.
        :param epsilon: Glättungswert zur Vermeidung von Divisionen durch Null.
        """
        self.gamma = gamma
        self.epsilon = epsilon

    def _normalize_distribution(self, dist: np.ndarray) -> np.ndarray:
        dist = np.asarray(dist, dtype=float)
        dist = np.clip(dist, self.epsilon, 1.0)
        return dist / np.sum(dist)

    def compute_kl_divergence(self, p: np.ndarray, q: np.ndarray) -> float:
        """
        Berechnet die KL-Divergenz D_KL(P || Q) zwischen der Referenzverteilung P 
        und der beobachteten Verteilung Q.
        """
        p_norm = self._normalize_distribution(p)
        q_norm = self._normalize_distribution(q)
        
        # D_KL(P || Q) = sum(P(i) * log(P(i) / Q(i)))
        kl_div = np.sum(p_norm * np.log(p_norm / q_norm))
        return float(kl_div)

    def calculate_weight_decay(self, kl_div: float) -> float:
        """
        Berechnet den Vertrauens-Decay basierend auf der KL-Divergenz:
        Gewicht = exp(-gamma * D_KL)
        """
        return float(np.exp(-self.gamma * kl_div))
