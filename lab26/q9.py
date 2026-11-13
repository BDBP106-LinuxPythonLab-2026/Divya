import numpy as np

a = np.array([100,234,345,565,985])
print(a)

log_val = np.round(np.log2(a), 2)
print(log_val)

percentage = np.round((a / np.sum(a)) * 100, 1)
print(percentage)