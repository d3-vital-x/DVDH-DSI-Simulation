MCMC Methodology

Overview

This document describes the Markov Chain Monte Carlo (MCMC) methodology used to infer parameters within the Dark Vital Dimensional Hypothesis (DVDH) simulation framework.

The objective of the MCMC analysis is to quantify whether a non-gravitational coupling term is statistically supported by local observational data, compared to a purely classical gravitational null model.

---

Parameter Vector

The inferred parameter vector is defined as:

{ alpha_VX, omega_res, rho_VX, sigma_obs }

Where:

- alpha_VX represents the strength of the hypothesized non-gravitational coupling
- omega_res denotes the resonance frequency of the coupled field
- rho_VX encodes the effective local field density
- sigma_obs models observational uncertainty

---

Likelihood Function

The likelihood is constructed assuming Gaussian observational noise:

L ∝ exp( -χ² / 2 )

where χ² measures the deviation between simulated trajectories and observational residuals.

---

Priors

Priors are chosen to be weakly informative:

- alpha_VX ≥ 0
- omega_res bounded by dynamical stability limits
- rho_VX ≥ 0
- sigma_obs > 0

This choice prevents unphysical solutions while avoiding over-constraining the inference.

---

Sampling Strategy

- Sampler: Ensemble-based MCMC
- Chains: Multiple walkers initialized across prior space
- Burn-in: Discarded to ensure convergence
- Convergence diagnostics: Autocorrelation time and posterior stability

---

Outputs

- Posterior distributions
- Corner plots for parameter covariance
- Model comparison against null gravitational dynamics

---

Reproducibility

All random seeds, likelihood definitions, and parameter bounds are explicitly defined in the analysis pipeline to ensure full reproducibility.
