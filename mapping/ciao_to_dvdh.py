# ciao_to_dvdh.py
# Pure mathematical feature adapter
# CIAO / CSC 2.1  →  DVDH / DSI space

import math

def rank_transform(x, xmin=1, xmax=10):
    """
    Rank-like normalization for variability index.
    Assumes CSC-style discrete variability scale.
    """
    x = max(min(x, xmax), xmin)
    return (x - xmin) / (xmax - xmin)

def map_ciao_to_dvdh(
    flux_2_7_keV,
    hard_hm,
    var_index
):
    """
    Non-invasive feature mapping.
    Raw observational meaning is preserved.
    """

    features = {}

    # Energy flux normalization (log space)
    features["E_flux_norm"] = math.log10(flux_2_7_keV)

    # Spectral hardness proxy (identity map)
    features["spectral_tension"] = hard_hm

    # Temporal instability (rank-normalized)
    features["temporal_instability"] = rank_transform(var_index)

    return features
