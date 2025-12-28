"""
Module for modeling microbial survival under UV radiation.
This implements an exponential decay model for Deinococcus radiodurans.
"""

import math


def calculate_survival(uv_dose, decay_constant):
    """
    Calculate the survival fraction of microbes after exposure to UV radiation.

    Parameters
    ----------
    uv_dose : float
        UV radiation dose (in arbitrary units, e.g., J/m²).
    decay_constant : float
        Decay constant representing microbial sensitivity (unit: 1/(dose unit)).
        Higher values indicate greater sensitivity (faster decay).
        Typical values for D. radiodurans range from ~0.001 to 0.05 per J/m²
        (based on experimental data).

    Returns
    -------
    float
        Survival fraction S (0 to 1), where S = exp(-decay_constant * uv_dose).
    """
    return math.exp(-decay_constant * uv_dose)


if __name__ == "__main__":
    # Example usage
    dose = 100.0  # example UV dose
    k = 0.01      # example decay constant for D. radiodurans (within typical range)
    survival = calculate_survival(dose, k)
    print(f"UV dose: {dose}, decay constant: {k}")
    print(f"Survival fraction: {survival:.4f}")