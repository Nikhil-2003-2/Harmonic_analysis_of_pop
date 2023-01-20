import pandas as pd
pd.set_option('display.max_columns', 500)

df = pd.read_csv('new.csv')
df.drop(['Tuning', 'Chord'], axis=1, inplace=True)
print(df.head())

pd.DataFrame.to_csv(df, 'final.csv')
