# Raw FITS Ingestion (CIAO-Compatible)

This module ingests user-provided Chandra Level-2 FITS files
and extracts standard, theory-agnostic observational features.

No theoretical assumptions are applied at this stage.

All outputs are compatible with CSC 2.1-style quantities
and may be independently reproduced using CIAO tools.

---

## Scope
- Input: Chandra Level-2 FITS (evt2, asol, bpix, etc.)
- Output: Standard observational feature proxies
- No model fitting
- No theoretical inference

## Purpose
This ingestion layer serves as a neutral interface between
raw observational data and downstream simulation modules.
