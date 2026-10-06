Contributing to Humanitas Purissima
Welcome to the Humanitas Purissima open-source repository. By participating in this project, you are contributing to a verifiable, decentralized system architecture designed to safeguard individual freedom, ecological regeneration, and global stability through mathematical invariants rather than trust.
Because this protocol directly impacts systemic security, privacy, and sovereignty, contribution standards are rigorous. Please read these guidelines carefully before submitting code, documentation, or mathematical proofs.
1. Code of Conduct & Core Principles
 * Invariant Preservation: No pull request may violate Ebene -1 (the unconditional survival invariant) or Ebene 0 (the hardened core of absolute privacy, zero-knowledge guarantees, and individual exit rights). Any contribution attempting to introduce backdoors, central control mechanisms, telemetry, or deanonymization will be rejected permanently.
 * Radical Transparency: All protocol modifications must be mathematically justified, formally verified where applicable, and open to public audit.
 * Constructive Collaboration: Peer review focuses on security, fault tolerance, and game-theoretic robustness.
2. Getting Started
 * Fork the Repository and clone your fork locally.
 * Set up your environment:
   python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

 * Run existing test suites & simulations:
   pytest tests/
jupyter notebook notebooks/oracle_kl_simulation.ipynb

 * Create a feature branch: git checkout -b feature/your-feature-name or fix/issue-description.
3. Contribution Workflow
 * Open an Issue: Before starting major work on core primitives, economic models (I_{\text{BPW}}), or cryptographic mechanisms (like DKDP or ZK-SNARK circuits), open an issue describing the problem and your proposed mathematical or architectural solution.
 * Implement & Test: Ensure your code includes comprehensive unit tests and passes all local simulations.
 * Submit a Pull Request (PR): Target the main or appropriate development branch. Provide a clear description of the changes, their game-theoretic impact, and how they adhere to the constitutional invariants.
4. Guidelines for Invariant-Audits & Security Reviews
Any contribution modifying cryptographic modules, consensus logic, the Kullback-Leibler oracle weights, or the Dual-Key Derivation Protocol (DKDP) requires a formal Invariant Audit:
 * Threat Modeling: Every PR touching core routing, sensor validation, or asset transfer must include a short threat model in the PR description detailing potential attack vectors (e.g., Sybil attacks, hardware spoofing, duress scenarios).
 * Zero-Knowledge Compliance: Ensure no PR introduces state tracking, logging of personal metadata, or unencrypted user telemetry. Zero-Knowledge by Default is non-negotiable.
 * Formal Verification (Lean/Coq): Where applicable, logical changes to the protocol kernel must be accompanied by corresponding formal proof updates in the verification suite.
 * Simulation Verification: Changes to oracle weighting (D_{\text{KL}}) or quadratic funding (S(i,j)) must be tested against Monte-Carlo simulations in the /notebooks directory to prove resistance against cartels and Goodharting.
5. Directory Structure & Contribution Targets
 * /kernel — Core protocol logic and cryptographic primitives. Changes here require multi-sig review by core maintainers.
 * /notebooks — Python simulations and Jupyter notebooks. Contributions improving simulation rigor or adding stress-test scenarios are highly encouraged.
 * /docs — Protocol specifications, architectural overviews, and translations.
6. License
By contributing to Humanitas Purissima, you agree that your contributions will be licensed under the terms of the GNU Affero General Public License v3.0 (AGPL-3.0) for code and CC-BY-SA 4.0 for documentation.
