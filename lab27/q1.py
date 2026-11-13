import matplotlib 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
# print(matplotlib.__version__)

temps = np.arange(20, 71, 5)
activity = np.array([12, 20, 35, 52, 70, 85, 92, 78, 45, 18, 5])

plt.plot(temps, activity, marker='o')
plt.show()

opt_temp = temps[np.argmax(activity)]    #returns index of highest activity
opt_activity = activity.max()

figure,axes = plt.subplots()
axes.plot(temps, activity, marker='o', linestyle='dashed', color ="blue")
axes.axvline(opt_temp, linestyle='dashed', color ="red")
axes.annotate()

