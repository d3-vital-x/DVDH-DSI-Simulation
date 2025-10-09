# $\mathbf{DVDH-DSI-Simulation}$: Dimensional Singularity Instability

This repository contains the core computational model for the $\mathbf{DVDH}$ microphysics, focusing on the mechanism of $\mathbf{DSI}$ (Dimensional Singularity Instability) and RCN (Relevant Coupling Network) which drives Spatio-Temporal collapse.

The primary goal is to **theoretically constrain** the cosmological parameters ($\mathbf{\alpha}$ and $\mathbf{\epsilon}$) used in the $\mathbf{DVDH-Cosmology-Project}$ via microscopic physics.

---

## 🔬 The Core Physics: DSI Mechanism

The model simulates the instability created by the coupling of **MCF** (Magnetic Component Flux) and **SEVB** (Spacetime Energy Wave Burst).

The **Dimensional Singularity Instability ($\mathbf{DSI}$)** function is defined as:

$$\mathbf{DSI(R, T) = \gamma \times MCF(R, T) \times SEVB(R, T)}$$

### Critical Collapse Condition

Collapse of Spacetime occurs when the instability exceeds a critical threshold ($\mathbf{D_{\text{crit}}}$):
$$\mathbf{DSI \ge D_{\text{crit}}} \quad (\text{where } D_{\text{crit}} = 1.0 \times 10^{-1} \text{ in simulation units})$$

---

## 🗂 Project Structure

| Folder | Purpose | Key Content |
| :--- | :--- | :--- |
| `01_SIM_CORE/` | **Core Simulation Engine** | `dsi_solver.py`, `mcf_sevb_functions.py` |
| `02_VISUALS/` | Simulation Output Plots | `DSI_Instability_Profile.png`, `Energy_Density_Map.png` |
| `03_PARAMETER_GRID/` | **Parameter Space Mapping** | Input grid for $\mathbf{B}_0, \mathbf{S}_0, \mathbf{\gamma}$ values. |
| `04_COUPLING_ANALYSIS/` | **Bridging Functions** | Scripts to derive $\mathbf{\alpha}$ and $\mathbf{\epsilon}$ from simulation results. |

---

## 🔗 Linking to Cosmology (Parameter Constraint)

The simulation results provide the theoretical values for the $\mathbf{DVDH}$ scaling parameters:

| Microscopic Result | Cosmological Parameter Constrained |
| :---: | :---: |
| $\mathbf{DSI_{\text{mean}}}$ / $\mathbf{DSI_{\text{max}}}$ | $\mathbf{\alpha}$ (Dimensional Index) |
| $\mathbf{R_{\text{collapse}}}$ / $\mathbf{T_{\text{collapse}}}$ | $\mathbf{\epsilon}$ (Vital Decay Factor) |

This link validates the $\mathbf{DVDH}$ cosmological model using fundamental physics inputs.

---

## 🚀 How to Run the Simulation

```bash
# 1️⃣ Run the DSI simulation grid
python 01_SIM_CORE/dsi_solver.py

# 2️⃣ Analyze grid results and derive alpha/epsilon
python 04_COUPLING_ANALYSIS/derive_cosmo_params.py
