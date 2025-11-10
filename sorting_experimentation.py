import pandas as pd
import matplotlib.pyplot as plt
from time import perf_counter

df = (pd.read_csv('sony_stocks_cleaned.csv'))
df["Daily Change"] = df["Closing"].diff()

def sort_time_calc(n):
    df_slice = df[1:n+1]
    start_time = perf_counter()
    sorted_slice = df_slice.sort_values(by="Daily Change")
    end_time = perf_counter()
    sort_time = end_time - start_time
    sort_time_list.append([n, sort_time])

sort_time_list = []

for n in range(7, 365):
    sort_time_calc(n)

x = [value[0] for value in sort_time_list]
y = [value[1] for value in sort_time_list]

plt.plot(x, y)
plt.show()

plt.xlabel("Number of Rows")
plt.ylabel("Sort Time (seconds)")
plt.title("Sort Time vs Data Size")
plt.grid(True)