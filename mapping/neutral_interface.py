# neutral_interface.py
# Mission-agnostic observable vector (NOV)

def neutral_observable_vector(F_energy, H_spectral, T_variation):
    """
    Telescope-agnostic observable interface.
    Canonical feature slots:
      F_energy   : band-integrated flux (any band)
      H_spectral : hardness / color index
      T_variation: variability metric
    """
    return {
        "F_energy": F_energy,
        "H_spectral": H_spectral,
        "T_variation": T_variation
    }
