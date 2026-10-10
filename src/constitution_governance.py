import time

class ConstitutionGovernance:
    def __init__(self):
        """
        Initialisiert die Living Constitution Verwaltung nach Artikel VI.
        """
        # Ebene 0: Unveraenderliche Kerninvarianten (Absoluter Protokollschutz)
        self._layer_0_invariants = {
            "unbedingte_privatsphaere": True,
            "noetigungsschutz_dkdp": True,
            "freiraum_garantie": True,
            "zero_utility_lock": True
        }
        
        # Ebene 1: Anpassbare Systemparameter (Ueber Buergerraete modifizierbar)
        self.layer_1_parameters = {
            "subgrid_reserve_threshold": 200.0,
            "kl_decay_gamma": 0.3,
            "sabbatical_max_weeks": 26
        }
        
        self.timelock_registry = {}
        # 120 Tage gesetzte Sperrfrist in Sekunden
        self.TIMELOCK_DURATION = 120 * 24 * 60 * 60

    def propose_parameter_change(self, parameter_name, new_value):
        """
        Registriert einen Modifikationswunsch fuer Ebene 1 im Timelock-Register.
        Versuche, Ebene 0 zu manipulieren, werden hart blockiert.
        """
        current_time = int(time.time())
        
        if parameter_name in self._layer_0_invariants:
            return False, "PROTOKOLL-ALARM: Modifikation von Ebene 0 absolut unzulaessig!"
            
        if parameter_name in self.layer_1_parameters:
            self.timelock_registry[parameter_name] = {
                "new_value": new_value,
                "available_at": current_time + self.TIMELOCK_DURATION
            }
            return True, f"Aenderung registriert. 120-Tage Timelock aktiv."
            
        return False, "Parameter im Systemkontext unbekannt."

    def execute_parameter_change(self, parameter_name, simulated_time=None):
        """
        Aktiviert die Parameter-Evolution nach Ablauf der kryptografischen Sperrfrist.
        """
        if parameter_name not in self.timelock_registry:
            return False, "Kein registrierter Aenderungsvorschlag vorhanden."
            
        proposal = self.timelock_registry[parameter_name]
        check_time = simulated_time if simulated_time is not None else int(time.time())
        
        # Invarianten-Pruefung des Timelocks
        if check_time < proposal["available_at"]:
            remaining_seconds = proposal["available_at"] - check_time
            remaining_days = remaining_seconds / (24 * 60 * 60)
            return False, f"ABGEWIESEN: Sperrfrist aktiv. Verbleibend: {remaining_days:.1f} Tage."
            
        # Aktualisierung durchfuehren
        self.layer_1_parameters[parameter_name] = proposal["new_value"]
        del self.timelock_registry[parameter_name]
        return True, f"ERFOLG: Parameter '{parameter_name}' aktualisiert."
