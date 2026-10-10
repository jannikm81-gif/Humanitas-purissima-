import numpy as np

class WealthEconomyController:
    def __init__(self, initial_bio=50.0, initial_infrastrukt=30.0, initial_kult=40.0):
        """
        Initialisiert das planetare Ressourcen-Modell nach Artikel VII.
        """
        self.I_Bio = initial_bio
        self.I_Infrastrukt = initial_infrastrukt
        self.I_Kult = initial_kult

    def absorb_fiat_liquidity(self, external_fiat_value):
        """
        Invariante aus Artikel I: Wandelt spekulatives Kapital zinslos 
        in reale, sachwertgedeckte Infrastruktur-Einheiten um.
        """
        drain_factor = 0.02 * (external_fiat_value / 100.0)
        self.I_Infrastrukt += (drain_factor * 1.5)
        return drain_factor

    def update_ecological_index(self, growth_delta):
        """
        Aktualisiert den Index fuer oekologische Regeneration (I_Bio).
        """
        self.I_Bio = max(0.0, self.I_Bio + growth_delta)

    def update_cultural_resonance(self, resonance_delta):
        """
        Aktualisiert die kulturelle Resonanz und die Kulanzfenster (I_Kult).
        """
        self.I_Kult = max(0.0, self.I_Kult + resonance_delta)

    def calculate_bpw_gradient(self):
        """
        Berechnet den echten Wohlstandsgradienten (I_BPW) als geometrisches Mittel.
        Stellt sicher, dass das System kollabiert, wenn eine Saeule ausgebeutet wird (Wert = 0).
        """
        if self.I_Bio <= 0 or self.I_Infrastrukt <= 0 or self.I_Kult <= 0:
            return 0.0
        
        # Geometrisches Mittel aus den drei tragenden Saeulen
        I_BPW = (self.I_Bio * self.I_Infrastrukt * self.I_Kult) ** (1.0 / 3.0)
        return I_BPW
