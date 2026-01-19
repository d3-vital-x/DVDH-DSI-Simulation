# Dark Vital Dimensional Hypothesis (DVDH) — Scientific Summary

#> 📘 For a high-level scientific overview, see: SCIENTIFIC_SUMMARY.md

**Project Lead:** Md. Rabiul Islam (R. Islam)  

**ORCID iD:** 0009-0009-2038-3524

**Hash (SHA-256):** 640d8ec0641cac6f1a148f3e050bb0c94bb30ab717f95693575daabf839220c4  

👥 Co-Investigators & Computational Architects: ChatGPT-5 and Gemini —  

### 📧 Contact: 📩 rabiul.peace.light@gmail.com  
**Slogan:** Transform the World, Illuminate the Future

## Overview

The Dark Vital Dimensional Hypothesis (DVDH) is a theoretical framework designed to investigate local-scale astrophysical anomalies, specifically those associated with 3I/Tsuchinshan–ATLAS. The framework integrates classical gravitational dynamics with a hypothesized non-gravitational coupling term to account for observed deviations in velocity, UV radiation signatures, and non-gravitational acceleration.

This repository provides:
- Formal derivations of DVDH field equations  
- MCMC-based statistical analysis of local observational data  
- Consistency checks against classical gravitational models  
- Tools for simulating coupled scalar–magnetic field interactions  
---

> ⚠️ **Repository Scope Clarification**
>
> The above section provides a high-level scientific context for the DVDH framework.
>  
> The sections below describe the **specific microphysical simulation implementation**
> of the **Dimensional Singularity Instability (DSI)** mechanism contained in this repository.
---

## Key Features

### MCMC Analysis & Parameter Inference

Parameter vector:  
`{ alpha_VX, omega_res, rho_VX, sigma_obs }`

- Robust posterior distributions indicate that an additional non-gravitational coupling is statistically supported by local data.
- Null-model tests demonstrate that classical dynamics alone cannot reproduce the observed anomalies.

### Mathematical Consistency

- Dimensionless normalization (Π-groups) ensures scale-invariant structure.
- Stability constraints and Lyapunov-derived bounds maintain internal coherence.
- Exact reduction to General Relativity is recovered in the limit:  
  `alpha → 0, F → 0`

### Testable Predictions

- Predicts velocity and UV-correlated anomalies consistent with 3I/Tsuchinshan–ATLAS.
- Framework is explicitly designed for local-scale astrophysical testing rather than cosmological extrapolation.

### Simulation-Ready

- All field equations and MCMC pipelines are implemented for reproducible computational experiments.
- Corner plots and likelihood diagnostics are included for posterior evaluation.

---

## Purpose

DVDH aims to:
- Bridge the gap between classical gravitational theory and unexplained local astrophysical anomalies.
- Provide a mathematically robust, testable, and simulation-ready framework.
- Offer a foundation for future investigations of dimensionally coupled phenomena in astrophysics.

---

## Recommended Repository Placement

This repository is structured as a **simulation-focused research environment**.

- Formal theory and derivations belong in a separate cosmology or theory repository.
- This repository contains numerical simulations, MCMC inference, and empirical consistency tests.
- Cross-references to the theory repository are encouraged for full context.

**Summary:**  

Theory repository = formal derivations  
Simulation repository = MCMC + empirical checks + this README

# DVDH–DSI–Simulation

## Dimensional Singularity Instability — Microphysical Simulation Framework

This repository contains the core microphysical simulation framework supporting the **Dark Vital Dimensional Hypothesis (DVDH)**.

It focuses on the **Dimensional Singularity Instability (DSI)** mechanism as a phenomenological microphysical construct used to theoretically constrain selected cosmological parameters within the DVDH framework.

---

## Scope Notice

This codebase does not claim empirical validation.  
It is intended as a numerical consistency and parameter-bridging tool that complements the formal analytical derivations presented in the main DVDH monograph.

---

## Physical Motivation (Claim Classification)

### C1 — Established Reference
Field coupling, instability growth, and threshold-driven collapse are modeled using standard numerical techniques common in nonlinear field dynamics.

### C2 — DVDH Theoretical Extension
The DSI mechanism is introduced as an effective instability construct arising from the coupling of:

- MCF — Magnetic Component Flux  
- SEVB — Spacetime Energy Wave Burst  

### C3 — Speculative Boundary
DSI is treated strictly as a simulation-level instability proxy and not as a confirmed physical entity.

---

## Core Instability Definition

Dimensional Singularity Instability is defined as:

DSI(R, T) = γ × MCF(R, T) × SEVB(R, T)

where γ is a dimensionless coupling strength.

---

## Collapse Threshold (Simulation Criterion)

A collapse-like instability regime is identified when:

DSI ≥ D_crit

with:

D_crit = 1.0 × 10^-1 (simulation units)

This threshold is model-defined and serves as a numerical marker for regime transition, not as an observational claim.

---

## Repository Structure

01_SIM_CORE  
- dsi_solver.py  
- mcf_sevb_functions.py  

02_VISUALS  
- DSI_Instability_Profile.png  
- Energy_Density_Map.png  

03_PARAMETER_GRID  
- parameter_grid_inputs.py  

04_COUPLING_ANALYSIS  
- derive_cosmo_params.py  

---

## Parameter Bridging to DVDH Cosmology

Simulation outputs are mapped to DVDH scaling parameters as follows:

- DSI_mean / DSI_max → α (Dimensional Index)  
- R_collapse / T_collapse → ε (Vital Decay Factor)

These mappings serve as theoretical consistency constraints supporting the analytical results derived in Chapters 5–7 of the DVDH derivation framework.

---

## Observability and Testability

- Directly Testable: No  
- Indirect Signatures: Possible  
- Simulation Feasible: Yes  
- Observational Analogues: None claimed  

---

## How to Run

### Run the DSI simulation
```bash
python src/dsi/dsi_solver.py
```

Derive cosmological parameters
```
python src/analysis/derive_cosmo_params.py
```
---

## Risk Statement

This simulation contains speculative constructs beyond current experimental verification and is presented to guide hypothesis-driven exploration within the DVDH framework.

---

## License

MIT License — see the LICENSE file for details.
