![](../../actions/workflows/tests.yml/badge.svg)






# Humanitas Purissima
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jannikm81-gif/Humanitas-purissima-/blob/main/notebooks/oracle_kl_simulation.ipynb)


> **Systemarchitektur:** Dezentrales Resilienz-, Autonomie- & Stabilitätsprotokoll  
> **Spezifikation:** Edition 10.0  
> **Autor:** Jannik Möller  
> **Status:** Open-Source Forschungsspezifikation & Manifest  
> **Lizenz:** AGPL-3.0 / CC-BY-SA 4.0  

---

## 🕊 Vorwort des Verfassers

Menschlicher Fortschritt scheitert in der Geschichte selten an mangelnder Technik, unzureichenden Ressourcen oder fehlenden Ideen. Er scheitert fast immer an derselben strukturellen Schwachstelle: der Anfälligkeit zentralisierter Machtstrukturen für Zensur, Korruption, militärische Aggression und ideologische Vereinnahmung.

Solange Frieden, individuelle Freiheit und gesellschaftliche Stabilität auf moralischen Appellen, geopolitischen Verträgen oder dem Wohlwollen zentraler Instanzen basieren, bleiben sie fragil. Macht zieht stets die Tendenz nach sich, sich selbst zu erhalten und auszuweiten – meist auf Kosten der Souveränität des Einzelnen und des ökologischen Gleichgewichts.

**Humanitas Purissima** begegnet dieser Dynamik nicht mit einer neuen Ideologie, sondern mit **mathematisch gehärteten Invarianten**. 

Dieses Protokoll versteht sich als unbestechliche, dezentrale Systemarchitektur. Es ersetzt Vertrauensannahmen durch Kryptografie, verteilte Spieltheorie und Invarianten-Engineering. Das Ziel ist nicht, den Menschen umzuerziehen, sondern eine Infrastruktur zu schaffen, in der Zensur, Ausbeutung, Orakel-Fälschung und physische Nötigung **spieltheoretisch und ökonomisch schlicht unrentabel** werden.

Menschliche Kulanz, kulturelle Vielfalt und der Schutz der persönlichen Privatsphäre sind dabei keine nachgelagerten Zugeständnisse, sondern unumstößliche Invarianten des gehärteten Kerns (Ebene 0). 

Dieses Repository markiert den Übergang von einer theoretischen Spezifikation zu einem freien, modularen Open-Source-Ökosystem.

— *Jannik Möller*

---

## 📑 Inhaltsübersicht

- [1. Die Kerninvarianten](#1-die-kerninvarianten)
- [2. Protokoll-Architektur (Übersicht der Artikel)](#2-protokoll-architektur-übersicht-der-artikel)
- [3. Mathematische & Kryptografische Primitiven](#3-mathematische--kryptografische-primitiven)
- [4. Prototypen & Simulationen](#4-prototypen--simulationen)
- [5. Lizenz & Beitragen](#5-lizenz--beitragen)

---

## 🛡 1. Die Kerninvarianten

* **Unbedingte Privatsphäre (Zero-Knowledge by Default):** Private Gedanken, Kultur, Kunst und persönliche Kommunikation sind der Protokollebene absolut entzogen.
* **Nötigungsschutz & Plausible Deniability:** Schützt Individuen unter physischem Zwang durch kryptografisch entkoppelte Duress-Pfade (DKDP).
* **Orakel-Resilienz via Entropie-Decay:** Mathematische Entwertung gefälschter Umwelt- und Sensordaten mittels Kullback-Leibler-Divergenz ($D_{\text{KL}}$).
* **Zero-Utility Lock (ZTIL):** Automatische Entwertung physischer Infrastruktur bei gewaltsamer Besetzung oder Aggression.
* **Kartellimmunität:** Schutz von Gemeinschaftsmitteln vor Sybil-Angriffen durch *Pairwise Bounded Quadratic Funding*.

---

## 🏛 2. Protokoll-Architektur (Übersicht der Artikel)

### Artikel I: Genesis-Nullpunkt & Hardware-Degradation
* Formale Verifikation des Kerncodes (Lean/Coq) ohne Admin-Schlüssel.
* Multi-Tier Hardware Execution (Tier 0 bis Tier 2 Fallback auf Standard-8-Bit Microcontrollern).
* Der Trojanische Wohlstandsgradient zur zinslosen, dezentralen Wertschöpfung ($I_{\text{BPW}}$).

### Artikel II: Adversarieller Spatio-Temporaler Orakel-Schutz
* Dynamischer Gewichtungs-Decay für Sensorknoten:
  $$w_i(t+1) = w_i(t) \cdot \exp\left(-\gamma \cdot D_{\text{KL}}\left(P_{\text{Sensor}} \parallel P_{\text{Kontext}}\right)\right)$$

📊 **[Live-Simulationsergebnis im Jupyter-Notebook anzeigen](notebooks/oracle_sybil_simulation.ipynb)**



*   **Integration des Poethischen Orakels** zur Messung kultureller Resonanz ($I_{\text{Kult}}$).
*   **Strukturelle Kulanzfenster** zur Vermeidung algorithmischer Härte bei Erstverstößen.


### Artikel III: Sub-Grid-Autarkie & Zero-Utility Lock (ZTIL)
📊 **[Live-ZTIL-Graphen im Jupyter-Notebook anzeigen](notebooks/ztil_network_simulation.ipynb)**

* Automatische ökonomische Isolation bei nachgewiesener physischer Aggression.
* Dynamic Network Partitioning: Nahtlose Abspaltung lokaler Sub-Grids bei Netzwerktrennung.

### Artikel IV: Digitale Souveränität & DKDP-Nötigungsschutz
* Self-Sovereign Identity (SSI) & Proof-of-Personhood ohne zentrale Biometrie-Datenbank.
* Dual-Key Derivationsprotokoll (DKDP) für plausible Abstreitbarkeit bei physischer Erpressung.
* Das Freiraum-Protokoll (Recht auf Sabbatical / Auszeit ohne Verlust der Grundversorgung).

### Artikel V: Exil- & Dissidenten-Ventil
* Recht auf friedliche Sezession und individuellen Exit aus lokalen Sub-Grids.
* Offline-Voucher für reibungslose Fluchthilfe ohne aktive Internetverbindung.

### Artikel VI: Der Gehärtete Kern & Living Constitution
* Zweistufige Hierarchie: **Ebene 0** (Unmanipulierbare Grundrechte & Invarianten) vs. **Ebene 1** (Parameter-Anpassungen via Bürgerräte und 120-Tage Timelock).

### Artikel VII: Planetares Ressourcen-Modell ($I_{\text{BPW}}$)
* Sachwertgedeckte Verrechnungseinheiten für Energie, Wasser und Wohnraum.
* Messung des echten Wohlstands über $I_{\text{Bio}}$, $I_{\text{Infrastrukt}}$ und $I_{\text{Kult}}$.

---

## 🔬 3. Mathematische & Kryptografische Primitiven

### Dual-Key Derivationsprotokoll (Appendix A)
HKDF-SHA256 Ableitung zweier orthogonaler Schlüssel aus einer Master-Entropie $S$:

$$\text{HKDF}(S, \text{Salt}_{\text{Real}}) \longrightarrow K_{\text{Real}}$$
$$\text{HKDF}(S, \text{Salt}_{\text{Duress}}) \longrightarrow K_{\text{Duress}}$$

Aus Kenntnis von $K_{\text{Duress}}$ lässt sich die Existenz von $K_{\text{Real}}$ rechnerisch nicht von zufälligem Rauschen unterscheiden.

---

## 🧪 4. Prototypen & Simulationen

Im Ordner `/notebooks` finden sich die mathematischen und kryptografischen Validierungen der Kerninvarianten, die direkt via Google Colab ausgeführt werden können:

* **Orakel-Resilienz & Sybil-Schutz (`oracle_sybil_simulation.ipynb`)**: Verifiziert die Isolierung eines koordinierten 60%-Sybil-Kartells mittels Pairwise Bounding und informationstheoretischem Divergenz-Decay.
* **Nötigungsschutz & Plausible Deniability (`dkdp_verification.ipynb`)**: Beweist die mathematische Orthogonalität und maximale Shannon-Entropie der dual abgeleiteten Schlüssel unter physischem Zwang.
* **Zero-Utility Lock (`ztil_simulation.ipynb`)**: Simuliert die sofortige, automatische Hardware-Entwertung besetzter Knoten bei gleichzeitiger Aufrechterhaltung der verbleibenden Sub-Grid-Integrität.
* **Trojanischer Wohlstandsgradient (`wealth_gradient.ipynb`)**: Berechnet das reale Ressourcen-Wachstum (\(I_{BPW}\)) über das geometrische Mittel von Ökologie, Infrastruktur und Kultur, entkoppelt von spekulativer Zins-Inflation.
* **Exil- & Dissidenten-Ventil (`exil_ventil.ipynb`)**: Validiert den fälschungssicheren, asymmetrischen Transfer von Offline-Vouchern via Ed25519 ohne jegliche Internet- oder Datenbankverbindung.
* **Living Constitution (`living_constitution.ipynb`)**: Demonstriert die Unantastbarkeit der Ebene-0-Invarianten sowie die unerbittliche Einhaltung des kryptografischen 120-Tage Timelocks für Parameter-Evolutionen.





---

## 📜 5. Lizenz & Beitragen

Dieses Manifest und die zugehörigen Spezifikationen stehen unter der **GNU Affero General Public License v3.0 (AGPL-3.0)** bzw. **CC-BY-SA 4.0**. 

Contributions, Reviews und kritische Invarianten-Audits sind herzlich willkommen.
