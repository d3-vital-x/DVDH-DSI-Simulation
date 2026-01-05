# DVDH–DSI–Simulation
## Dimensional Singularity Instability — Microphysical Simulation Framework

This repository contains the core microphysical simulation framework supporting the **Dark Vital Dimensional Hypothesis (DVDH)**.

It focuses on the **Dimensional Singularity Instability (DSI)** mechanism as a *phenomenological microphysical construct* used to **theoretically constrain** selected cosmological parameters within the DVDH framework.

---

## Scope Notice

This codebase does **not** claim empirical validation.  
It is intended as a numerical consistency and parameter-bridging tool that complements the formal analytical derivations presented in the main DVDH monograph.

---

## Physical Motivation (Claim Classification)

### [C1] Established Reference
Field coupling, instability growth, and threshold-driven collapse are modeled using standard numerical techniques common in nonlinear field dynamics.

### [C2] DVDH Theoretical Extension
The **DSI mechanism** is introduced as an *effective instability construct* arising from the coupling of:

- **MCF** — Magnetic Component Flux  
- **SEVB** — Spacetime Energy Wave Burst  

### [C3] Speculative Boundary
DSI is treated strictly as a **simulation-level instability proxy** and **not** as a confirmed physical entity.

---

## Core Instability Definition

The Dimensional Singularity Instability is modeled as:

DSI(R, T) = γ × MCF(R, T) × SEVB(R, T)

where γ is a dimensionless coupling strength.

---

## Collapse Threshold (Simulation Criterion)

A collapse-like instability regime is identified when:

DSI ≥ D_crit

with:

D_crit = 1.0 × 10⁻¹

(simulation units)

This threshold is **model-defined** and serves as a numerical marker for regime transition, not as an observational claim.

---

## Repository Structure

01_SIM_CORE/  
├─ dsi_solver.py  
├─ mcf_sevb_functions.py  

02_VISUALS/  
├─ DSI_Instability_Profile.png  
├─ Energy_Density_Map.png  

03_PARAMETER_GRID/  
├─ parameter_grid_inputs.py  

04_COUPLING_ANALYSIS/  
├─ derive_cosmo_params.py  

---

## Parameter Bridging to DVDH Cosmology

Simulation outputs are mapped to DVDH scaling parameters as follows:

- **DSI_mean / DSI_max** → α (Dimensional Index)  
- **R_collapse / T_collapse** → ε (Vital Decay Factor)

These mappings serve as **theoretical consistency constraints**, supporting the analytical results derived in Chapters 5–7 of the DVDH derivation framework.

---

## Observability & Testability Flag

- Directly Testable: **No**  
- Indirect Signatures: **Possible**  
- Simulation Feasible: **Yes**  
- Observational Analogues: **None claimed**

---

## How to Run

### 1. Run the DSI simulation grid
```bash
python 01_SIM_CORE/dsi_solver.py
2. Derive cosmological parameters
Copy code
Bash
python 04_COUPLING_ANALYSIS/derive_cosmo_params.py
Risk Statement
This simulation contains speculative constructs beyond current experimental verification and is presented to guide hypothesis-driven exploration within the DVDH framework.
License
MIT License — see the LICENSE file for details.
