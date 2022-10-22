import pandas as pd

file = pd.read_csv('auto-mpg-quiz.csv', index_col='name')
# print(file)
file_drop = file.drop(columns=['mpg', 'displ', 'yr', 'origin'], axis=1)
# print(file_drop)
file_loc1 = file.loc[file['cyl'] == 4]
# print(file_loc1)
file_loc2 = file.loc[(file['cyl'] == 4) & (file['hp'] > 80)]
# print(file_loc2)
file_loc3 = file.loc[((file['cyl'] == 4) & (file['hp'] > 80)) | (
        (file['cyl'] == 8) & (file['hp'] > 90))]
# print(file_loc3)
weight_mean = file_loc3.pop('weight').mean()
print(round(weight_mean, 3))