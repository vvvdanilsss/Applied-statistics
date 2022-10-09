import pandas as pd
import matplotlib.pyplot as plt

all_cars = pd.read_csv('auto-mpg-quiz.csv', index_col='name')
all_cars_sorted = all_cars.sort_values('hp')
# plt.plot('hp', 'accel', data=all_cars_sorted)
# plt.show()
# plt.hist(all_cars_sorted['hp'])
# plt.show()
pie_data = all_cars.groupby(['cyl']).count()
plt.pie(pie_data['mpg'], labels=pie_data.index)
plt.show()