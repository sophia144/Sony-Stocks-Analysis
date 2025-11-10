import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter

#reads the dataframe
df = (pd.read_csv('sony_stocks_cleaned.csv'))
df["Daily_Change"] = df["Closing"].diff()

#function to calculate how long it takes to sort an array with a specified number of items
def sort_time_calc(n, array):
    sub_array = array[1:n+1]

    start_time = perf_counter()
    np.sort(sub_array)
    end_time = perf_counter()

    sort_time = end_time - start_time
    x.append(n)
    y.append(sort_time)

x = []
y = []

array = np.array(df["Daily_Change"])
for n in range(7, 365):
    sort_time_calc(n, array)

#plots the results
plt.plot(x, y)

plt.xlabel("n", family='monospace')
plt.ylabel("Time (s)", family='monospace')
plt.title("Sort Time vs Data Size", family='monospace')
plt.grid(True)

plt.show()