import pandas as pd
import numpy as np

df = pd.read_excel('AVG_salary.xlsx', header=None, names=['name', 'salary'])
stop = ['Сахалинская обл.', 'Псковская область', 'Приморский край', 'Мурманская обл.']
copy_df = df[df.name.isin(stop) == False]
sort_df = copy_df.sort_values(by='salary', ignore_index=True)
print(sort_df.salary.iloc[11], sort_df.salary.iloc[22], sort_df.salary.iloc[78])

sort_df['cut'] = pd.cut(sort_df.salary, bins=10, right=False)
print(sort_df.cut.value_counts())

min_sal, max_sal = sort_df.salary.iloc[0], sort_df.salary.iloc[-1]
length = (max_sal - min_sal) / 10
print(len(sort_df[(sort_df.salary >= sort_df.salary.iloc[0] + length) & (sort_df.salary < sort_df.salary.iloc[0] + 2 * length)]))
print(len(sort_df[(sort_df.salary >= sort_df.salary.iloc[0] + 5 * length) & (sort_df.salary < sort_df.salary.iloc[0] + 6 * length)]))
print(len(sort_df[(sort_df.salary >= sort_df.salary.iloc[0] + 6 * length) & (sort_df.salary < sort_df.salary.iloc[0] + 7 * length)]))

print(np.mean(copy_df.salary))
print(np.var(copy_df.salary))
print(np.var(copy_df.salary) * len(copy_df.salary) / (len(copy_df.salary) - 1))
print(np.quantile(copy_df.salary, 0.5))
print(np.quantile(copy_df.salary, 0.25))
print(np.quantile(copy_df.salary, 0.75))