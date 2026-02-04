"""
CIAO-compatible FITS ingestion
Produces CSC-like proxy features for downstream simulations
"""

from astropy.io import fits
import numpy as np

def ingest_evt2(evt2_path):
    with fits.open(evt2_path) as hdul:
        data = hdul[1].data
        
        energy = data['ENERGY'] / 1000.0  # eV → keV
        time = data['TIME']
        
    return energy, time


def band_flux_proxy(energy, emin, emax):
    mask = (energy >= emin) & (energy <= emax)
    return np.sum(mask)


def extract_basic_features(evt2_path):
    energy, time = ingest_evt2(evt2_path)
    
    features = {
        "soft_counts": band_flux_proxy(energy, 0.5, 2.0),
        "hard_counts": band_flux_proxy(energy, 2.0, 7.0),
        "total_counts": len(energy),
    }
    
    return features
