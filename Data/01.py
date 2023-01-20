import pandas as pd

df1 = pd.read_csv("new1.csv")
print(df1)
df2 = pd.read_csv("Tabsultimatedata.csv")
print(df2)

dff = pd.merge(df1, df2, on="Song_name")
dff.drop_duplicates('Song_name')
print(dff)

#dff = dff.drop(dff.columns[[0]], axis=1)
dff.to_csv("output1.csv")
