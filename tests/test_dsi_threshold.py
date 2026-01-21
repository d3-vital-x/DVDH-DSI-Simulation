import sys
from pathlib import Path
import math

# Ensure src/ is discoverable in CI and local runs
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))


def test_dsi_threshold():
    """
    Minimal sanity test for DSI solver stability.

    Ensures the simulation runs without numerical
    divergence under nominal parameter values.
    """

    from dsi.dsi_solver import run_simulation

    params = {
        "alpha_VX": 0.01,
        "omega_res": 1.0,
        "rho_VX": 0.1,
        "sigma_obs": 0.05,
    }

    result = run_simulation(params)

    # Basic sanity checks (non-physics-claiming)
    assert result is not None
    assert isinstance(result, (int, float))
    assert math.isfinite(result)
