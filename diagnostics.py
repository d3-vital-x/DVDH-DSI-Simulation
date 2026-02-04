def dcn_score(E_flux_norm, spectral_tension, temporal_instability):
    """
    DCN: heuristic consistency scalar.
    No physical claim.
    """

    return (
        abs(E_flux_norm) *
        (1.0 + spectral_tension) *
        (1.0 + temporal_instability)
    )
