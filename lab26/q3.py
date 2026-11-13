import numpy as np

arr = np.array([[1, 2, 3],

                [7, 8, 9]])

reversed_rows = arr[::-1, :]
print(reversed_rows)

reversed_cols = arr[:, ::-1]
print(reversed_cols)
