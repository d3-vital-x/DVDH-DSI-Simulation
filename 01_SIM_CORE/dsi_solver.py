import numpy as np

def calculate_dsi(gamma, mcf, sevb):
    """
    Dimensional Singularity Instability calculation.
    DSI = gamma * MCF * SEVB
    """
    return gamma * mcf * sevb

if __name__ == "__main__":
    # Normalized parameters for consistency check
    gamma_val = 0.5
    mcf_val = 0.4
    sevb_val = 0.6

    dsi_result = calculate_dsi(gamma_val, mcf_val, sevb_val)
    print(f"Computed DSI: {dsi_result}")

    d_crit = 0.1
    if dsi_result >= d_crit:
        print("Status: Stability threshold exceeded (Predicted Regime Transition)")
