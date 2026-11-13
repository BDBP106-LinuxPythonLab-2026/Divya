import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(7)
length = rng.integers(50, 800, size=100) # amino acids
weight = length * 0.11 + rng.normal(0, 3, size=100) # kDa (about 110 Da per residue)
membrane = rng.random(100) < 0.3

plt.scatter(length[membrane], weight[membrane], marker='o', alpha=0.5, color = "pink", label = "Membranous" )
plt.scatter(length[~membrane], weight[~membrane], marker='*', alpha=0.5, color = "black", label = "soluble" )
plt.xlabel("length")
plt.ylabel("weight")
plt.title("Weight of membrane")
plt.legend()

plt.savefig("protein_size.png", dpi=150)
plt.show()