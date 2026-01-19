def map_to_cosmological_params(dsi_mean, dsi_max):
    """
    Maps microphysical simulation outputs to DVDH scaling parameters.
    """
    alpha = dsi_mean / dsi_max
    return alpha

if __name__ == "__main__":
    alpha_constrained = map_to_cosmological_params(0.15, 0.45)
    print(f"Constrained Alpha (Dimensional Index): {alpha_constrained}")
