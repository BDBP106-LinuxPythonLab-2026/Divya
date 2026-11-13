import matplotlib.pyplot as plt
import matplotlib
import numpy as np

genes = ["GAPDH", "ACTB", "TP53", "MYC", "EGFR"]
control = np.array([950, 1200, 310, 150, 420])
treated = np.array([940, 1180, 610, 75, 430])

x = np.arange(len(genes))
width = 0.2
plt.bar(x-width, control, width, label="Control", color ="pink")
plt.bar(x+width, treated, width, label="Treated", color ="blue")


#to add gene names
plt.xticks(x, labels=genes)
plt.legend()
plt.show()

fold_change = np.round(control/treated, 2)
for i in range(len(genes)):
  print(genes[i], ":", fold_change[i])