import pandas as pd

df = pd.read_csv('Uniform_193.csv', header=None, names=['coord'])
x_m = df.coord.mean()
d = df.coord.var()
print(x_m - (3 * d) ** 0.5, x_m + (3 * d) ** 0.5)
df['sort'] = df.sort_values(by='coord', ignore_index=True)
print(df)
a, b = df.sort.iloc[0], df.sort.iloc[-1]
print(a, b)
l = len(df.sort[(df.sort >= 34) & (df.sort <= 43)])
print(l / len(df.coord))