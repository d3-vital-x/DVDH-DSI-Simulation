import numpy as np
from scipy.stats import norm

def dcn_spectrum(energy_bins, flux_norm):
    """
    Collapse-regulated spectral envelope (dimensionless).
    """
    background = flux_norm * (energy_bins ** -1.9)
    soft_echo = 0.15 * flux_norm * norm.pdf(energy_bins, 0.72, 0.05)
    return background + soft_echo
