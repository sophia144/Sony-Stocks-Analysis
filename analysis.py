import pandas as pd

#importing and cleaning
df = (pd.read_csv('sony_stocks.csv'))
df = df.rename(columns={"Close/Last": "Closing"})
df = df.astype({'Date': 'datetime64[ns]'})

df["Closing"] = df["Closing"].str.replace('$', '')
df["Open"] = df["Open"].str.replace('$', '')
df["High"] = df["High"].str.replace('$', '')
df["Low"] = df["Low"].str.replace('$', '')

df.sort_values(by="Date", inplace=True, ignore_index=True)
df.to_csv('sony_stocks_cleaned.csv', index=False)

print(df)