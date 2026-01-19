def test_dsi_threshold():
    """
    Minimal sanity test for DSI solver stability.
    Ensures simulation output remains finite
    under nominal parameter values.
    """

    from src.dsi.dsi_solver import run_simulation

    params = {
        "alpha_VX": 0.01,
        "omega_res": 1.0,
        "rho_VX": 0.1,
        "sigma_obs": 0.05
    }

    result = run_simulation(params)

    assert result is not None
    assert abs(result) < 1e6
