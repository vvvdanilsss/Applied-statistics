import pandas as pd
import numpy as np

df10 = pd.read_csv('Poisson_10_84.csv', header=None)
mean10 = round(np.mean(df10[0]), 3)
disp10 = round(np.var(df10[0]), 3)
print(mean10, abs(round(3.7 - mean10, 3)))
print(disp10, abs(round(3.7 - disp10, 3)))

df10000 = pd.read_csv('Poisson_10000_84.csv', header=None)
mean10000 = round(np.mean(df10000[0]), 3)
disp10000 = round(np.var(df10000[0]), 3)
print(mean10000, abs(round(3.7 - mean10000, 3)))
print(disp10000, abs(round(3.7 - disp10000, 3)))