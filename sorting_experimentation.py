import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter

#reads the dataframe
df = (pd.read_csv('sony_stocks_cleaned.csv'))
df["Daily_Change"] = df["Closing"].diff()
diff_array = np.array(df["Daily_Change"])

#function to calculate how long it takes to sort an array with a specified number of items
def sort_time_calc(n, array):
    start_time = perf_counter()
    np.sort(array[1:n+1])
    end_time = perf_counter()
    sort_time = end_time - start_time
    sort_time_list.append([n, sort_time])

sort_time_list = []

for n in range(7, 365):
    sort_time_calc(n, diff_array)

#splits the 2D output into x and y values
x = [value[0] for value in sort_time_list]
y = [value[1] for value in sort_time_list]

#plots the results
plt.plot(x, y)

plt.xlabel("n", family='monospace')
plt.ylabel("Time (s)", family='monospace')
plt.title("Sort Time vs Data Size", family='monospace')
plt.grid(True)

plt.show()