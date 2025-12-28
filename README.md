# Microbial Survival Model for Panspermia Hypothesis

A simple computational model for microbial survival under UV radiation, simulating aspects of the Japanese Tanpopo experiment and the panspermia hypothesis.

## Mathematical Model

The survival fraction *S* of *Deinococcus radiodurans* after exposure to UV radiation is modeled using an exponential decay law:

```
S(d) = e^(-k * d)
```

where:
- *d* is the UV radiation dose (in arbitrary units, e.g., J/m²),
- *k* is a decay constant representing the microbe's sensitivity to UV radiation (unit: 1/(dose unit)),
- *S* is the survival fraction, ranging from 0 (complete inactivation) to 1 (no effect).

## Usage

The model is implemented in Python in `survival_model.py`. To use it:

```python
from survival_model import calculate_survival

# Example: dose = 150 J/m², decay constant = 0.02 per J/m²
survival = calculate_survival(150.0, 0.02)
print(f"Survival fraction: {survival:.4f}")
```

## Purpose

This project demonstrates a simplified simulation of microbial survival in space‑like UV conditions, as relevant to the **panspermia theory**—the idea that life could be distributed across planets via meteoroids. The [Tanpopo experiment](https://en.wikipedia.org/wiki/Tanpopo_(mission)) exposed microbes on the International Space Station to test their ability to survive the space environment; this model provides a basic quantitative framework for interpreting such experiments.

## License

This code is released under the MIT License.