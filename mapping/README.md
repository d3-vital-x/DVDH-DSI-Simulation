# CIAO Output → DVDH Feature Mapping (Non-Invasive)

This module defines a non-invasive mapping between
standard CIAO-derived observational quantities and
DVDH/DSI simulation input features.

No theoretical reinterpretation is applied at this stage.

The mapping is purely structural and dimensional,
preserving the original observational meaning of each quantity.

---

## Design Principles

- CIAO outputs remain unchanged
- No hidden model assumptions
- One-to-one or monotonic transformations only
- Fully reversible where applicable

This layer functions as a numerical interface,
not as a physical explanation.

---

## Standard CIAO Outputs Considered

| CIAO Quantity | Description |
|---------------|------------|
| `flux_2_7_keV` | Integrated X-ray flux (2–7 keV band) |
| `hard_hm` | Hardness ratio proxy |
| `var_index` | Variability index (e.g., Gregory–Loredo) |
| `theta_arcmin` | Off-axis angle |
| `sig_id` | Detection significance class |

These quantities are directly reproducible
using CIAO tools such as `srcflux`, `dmextract`, and `glvary`.

---

## DVDH / DSI Feature Interface

| CIAO Output | DVDH Feature Name | Mapping Type |
|------------|------------------|--------------|
| `flux_2_7_keV` | `E_flux_norm` | Log-normal scaling |
| `hard_hm` | `spectral_tension` | Linear rescale |
| `var_index` | `temporal_instability` | Rank-preserving |
| `theta_arcmin` | `projection_bias` | Geometric weight |
| `sig_id` | `confidence_tag` | Categorical pass-through |

These feature labels are internal simulation handles
and do not imply physical reinterpretation.

---

## Example (Conceptual)

CIAO output:

---

## Reproducibility Statement

Any user may bypass this mapping layer entirely
and operate directly on CIAO or CSC 2.1 outputs.

This module exists solely to standardize numerical
interfaces for simulation workflows.

---

## Compliance

- Compatible with Chandra CIAO
- Compatible with CSC 2.1 catalog quantities
- No dependency on proprietary datasets
- No modification of raw observational data

---
