class SystemEconomy:
    def __init__(self, base_resource_index: float = 1.0):
        self.bpw_index = base_resource_index  # Sachwert-Indizierung (I_BPW)

    def calculate_bpw_utility(self, tangible_value: float, risk_factor: float) -> float:
        """
        Berechnet den realen Nutzen basierend auf physischen Sachwerten 
        und entkoppelt von spekulativen Fiat-Mechaniken.
        """
        return (tangible_value * self.bpw_index) / (1.0 + risk_factor)

    def evaluate_cultural_status(self, peer_validations: int, contribution_weight: float) -> float:
        """
        Berechnet den Status über kulturelle und konstruktive Schöpfung (I_Kult)
        anstatt über destruktive oder kapitale Konkurrenz.
        """
        return float(peer_validations * contribution_weight)
