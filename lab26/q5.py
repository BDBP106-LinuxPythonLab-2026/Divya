import numpy as np


def elementwise_max(arr_a, arr_b):
    
    # Convert inputs to NumPy arrays if they aren't already
    a = np.asarray(arr_a)
    b = np.asarray(arr_b)

    return np.maximum(a, b)


# Example Usage:
a = [1, 2, 8, 4]
b = [0, 5, 3, 9]

c = elementwise_max(a, b)

print("Array a:", a)
print("Array b:", b)
print("Result c:", c)
