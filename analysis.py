import pandas as pd
from pandasql import sqldf

#importing and cleaning
df = (pd.read_csv('sony_stocks.csv'))
df = df.rename(columns={"Close/Last": "Closing"})
df = df.astype({'Date': 'datetime64[ns]'})
df["Closing"] = df["Closing"].str.replace('$', '')

#for debugging - delete later
print(df)