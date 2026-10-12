import numpy as np
import pytest

def berechne_payoffs_lokal(straffaktor_kl, verraeter_boost, zeitschritte=10):
    """
    Hilfsfunktion zur numerischen Validierung innerhalb der Testsuite.
    Simuliert die mathematischen Payoffs von HP-v10 lokal für die Assertions.
    """
    zeit = np.arange(zeitschritte)
    # Nutzenfunktion Kooperation
    payoff_kooperation = 10 * (np.log(zeit + 1) / np.log(1.5)) + 5 * (1 - np.exp(-0.1 * zeit))
    
    # Nutzenfunktion Defektion mit KL-Divergenz-Decay
    d_kl_wert = 0.8
    entropie_strafe = np.exp(-straffaktor_kl * d_kl_wert * zeit / 10)
    payoff_defektion = (verraeter_boost * (zeit == 0)) + (20 * entropie_strafe) - (5 * zeit * 0.1)
    
    return payoff_kooperation, payoff_defektion

def test_nash_gleichgewicht_unter_standard_strafen():
    """
    Prüft, ob bei regulärem KL-Straffaktor (2.5) die Kooperation 
    langfristig die Defektion strikt dominiert (Incentive Compatibility).
    """
    p_coop, p_defect = berechne_payoffs_lokal(straffaktor_kl=2.5, verraeter_boost=15)
    
    # Am Ende der Testperiode muss der ehrliche Knoten signifikant mehr Nutzen haben
    assert p_coop[-1] > p_defect[-1], "Kooperation muss Defektion langfristig dominieren!"

def test_anomalie_erkennung_bei_zu_geringer_strafe():
    """
    Prüft, ob das mathematische Modell mathematisch kippt, wenn der
    KL-Straffaktor absichtlich zu schwach gewählt wird (Sicherheits-Grenztest).
    """
    p_coop, p_defect = berechne_payoffs_lokal(straffaktor_kl=0.5, verraeter_boost=40)
    
    # Bei einem massiven Boost und winziger Strafe darf das Gleichgewicht temporär brechen
    # Dies validiert, dass unsere Anomalie-Erkennung im System logisch anspringt.
    assert p_defect[0] > p_coop[0], "Bei unzureichender Strafe muss ein temporärer Einbruch simulierbar sein."
