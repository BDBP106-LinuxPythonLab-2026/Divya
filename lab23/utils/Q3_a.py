rows, cols = 3, 4

with open("stringmatrix.dat", "w") as f:
    for r in range(rows):
        letters = [chr(65 + r * cols + c) for c in range(cols)]
        f.write(" ".join(letters) + "\n")