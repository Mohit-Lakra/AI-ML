# Type Hinting in Python
# It helps to catch shape mismatches and type errors early in the development process.

from typing import List, Dict, Tuple

def calculate_loss(predictions: List[float], targets: List[float]) -> float:
    total_error = 0.0
    for p,t in zip(predictions, targets):
        total_error += (p - t) ** 2
    return total_error / len(predictions)

# this functions tells that it will take list of floats as input and will return a float value

