grid = []
with open("stringmatrix.dat", "r") as f:
    for line in f:
        items = line.split()
        if items:
            grid.append(items)

rows = len(grid)
cols = len(grid[0])

print("Grid:")
print(grid)

columns = [[grid[r][c] for r in range(rows)] for c in range(cols)]
print("Columns:")
print(columns)

diagonals = []
for s in range(rows + cols - 1):
    diag = []
    for r in range(rows):
        c = s - r
        if 0 <= c < cols:
            diag.append(grid[r][c])
    diagonals.append(diag)
print("Diagonals:")
print(diagonals)