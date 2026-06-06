import numpy as np

def sigmoid(x) -> np.ndarray:
    """
    Vectorized sigmoid function.
    """
    # Write code here
    np_array_x = np.array(x)

    return 1 / (1 + (np.e ** -np_array_x))