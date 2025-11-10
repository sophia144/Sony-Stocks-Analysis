import pandas as pd
import matplotlib.pyplot as plt

#importing and cleaning
df = (pd.read_csv('sony_stocks.csv'))
df = df.rename(columns={"Close/Last": "Closing"})
df = df.astype({'Date': 'datetime64[ns]'})

dollar_cols = ['Closing', 'Open', 'High', 'Low']
for col in dollar_cols:
    df[col] = df[col].str.replace('$', '')
    df = df.astype({col: 'Float64'})

df.sort_values(by="Date", inplace=True, ignore_index=True)
df.to_csv('sony_stocks_cleaned.csv', index=False)

x = df["Date"].values
y = df["Closing"].values

plt.plot(x, y)

plt.xlabel("Date")
plt.ylabel("Closing ($)")
plt.title("Sony Stocks 24-25")
plt.grid(True)

plt.show()