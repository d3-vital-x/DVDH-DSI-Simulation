# Version: v0.4-neutral-adapter
# Updated: mission-agnostic mapping compatibility (2026-02)

import math
from mapping.neutral_interface import neutral_observable_vector

def rank_transform(x, xmin=1, xmax=10):
    """ Rank-like normalization for variability index. """
    x = max(min(x, xmax), xmin)
    return (x - xmin) / (xmax - xmin)

def map_ciao_to_dvdh(flux_2_7_keV, hard_hm, var_index):
    """
    Chandra-specific mapping producing a Neutral Observable Vector (NOV).
    """
    f_energy = math.log10(flux_2_7_keV) if flux_2_7_keV > 0 else -15.0
    h_spectral = hard_hm
    t_variation = rank_transform(var_index)
    
    return neutral_observable_vector(
        F_energy=f_energy,
        H_spectral=h_spectral,
        T_variation=t_variation
    )
