import pandas as pd
pd.set_option('display.max_columns', 3000)

df = pd.read_csv('new.csv', index_col=None)
df.drop(['Song_Name', 'Artist_Name'], axis=1, inplace=True)
print(df.head())

pd.DataFrame.to_csv(df, 'final.csv')
