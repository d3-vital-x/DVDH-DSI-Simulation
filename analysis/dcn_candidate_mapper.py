def select_dcn_candidates(df,
                          flux_min=1e-13,
                          var_min=5,
                          hard_min=0.7,
                          theta_max=1.0):
    """
    Identifies DCN-compatible sources using observational constraints.
    """
    return df[
        (df["flux_2_7_keV"] > flux_min) &
        (df["var_index"] >= var_min) &
        (df["hard_hm"] >= hard_min) &
        (df["theta_arcmin"] <= theta_max)
    ]
