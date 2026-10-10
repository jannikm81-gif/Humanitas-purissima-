import numpy as np

class FreiraumController:
    def __init__(self, initial_reserve=500.0, base_supply_level=100.0):
        """
        Initialisiert das Freiraum-Protokoll nach Artikel IV.
        """
        self.subgrid_reserve = initial_reserve
        self.base_supply_level = base_supply_level
        self.sabbatical_active = False
        self.sabbatical_elapsed_steps = 0

    def start_sabbatical(self):
        """
        Aktiviert die Auszeit fuer das Individuum.
        """
        self.sabbatical_active = True
        self.sabbatical_elapsed_steps = 0

    def end_sabbatical(self):
        """
        Beendet das Sabbatical und leitet die Reintegration ein.
        """
        self.sabbatical_active = False
        self.sabbatical_elapsed_steps = 0

    def process_network_step(self):
        """
        Berechnet den Zeitschritt fuer Aktivitaet, Reserve und die unantastbare Versorgung.
        """
        if self.sabbatical_active:
            self.sabbatical_elapsed_steps += 1
            # Invariante Ebene 0: Grundversorgung bleibt trotz Aktivitaet = 0 fast komplett erhalten
            # Minimale Anpassung ueber das strukturelle Kulanzfenster
            damping = 5.0 * (1.0 - np.exp(-0.1 * self.sabbatical_elapsed_steps))
            current_supply = self.base_supply_level - damping
            
            # Kollektiver Ausgleich: Das Sub-Grid fängt den Ausfall ueber die Reserve ab
            self.subgrid_reserve = max(0.0, self.subgrid_reserve - 8.0)
            current_activity = 0.0
        else:
            # Normalbetrieb: Volle Aktivitaet speist die kollektive Reserve wieder oekonomisch
            current_activity = 100.0
            current_supply = self.base_supply_level
            self.subgrid_reserve = min(500.0, self.subgrid_reserve + 4.0)

        return current_activity, current_supply, self.subgrid_reserve
