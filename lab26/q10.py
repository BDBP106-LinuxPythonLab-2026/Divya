import numpy as np

t = np.arange(0,121,20)

population = 100*2**(t/20)

print("population:", population)

print(t)

print("final population is", population[-1]/population[0], "times larger")

print(t[population > 1000])

