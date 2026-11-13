import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(3)
organisms = ["E. coli", "S. cerevisiae", "P. falciparum", "S. coelicolor"]
mean_gc = [51, 38, 19, 72]

figure , axes = plt.subplots(2,2)
