import pandas as pd
from sklearn import preprocessing as pp

df = pd.read_csv('report.csv')
df_loc = pd.DataFrame(df.loc[((df['TARGET'] == 0) & (
        df['MIP'] >= 88.484375) & (df['MIP'] <= 89.453125)) | (
        (df['TARGET'] == 1) & (df['MIP'] >= 65.078123) & (df['MIP'] <= 70.7421875))])
# print(df_loc)

MIP_mean = round(df_loc['MIP'].mean(), 3)
# print(MIP_mean)

df_loc.drop(columns='TARGET', axis=1, inplace=True)
# print(df)

scaler = pp.MinMaxScaler()
names = df_loc.columns
d = scaler.fit_transform(df_loc)
df_scaled = pd.DataFrame(d, columns=names)
# print(df_scaled)

MIP_mean = round(df_scaled['MIP'].mean(), 3)
# print(MIP_mean)

lst_dist = []
STAR = [0.595, 0.894, 0.813, 0.868, 0.067, 0.547, 0.08, 0.427]

for line in df_scaled.iloc:
    dist = 0
    line = list(line)

    for _ in range(len(line)):
        dist += (STAR[_] - line[_]) ** 2
    dist **= 0.5
    lst_dist.append(dist)

print(round(min(lst_dist), 3))