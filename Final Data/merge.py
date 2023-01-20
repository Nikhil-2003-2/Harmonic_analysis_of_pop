
import pandas as pd

# reading csv files
data1 = pd.read_csv('new.csv')
data2 = pd.read_csv('Tabsultimatedata.csv')
data1 = data1.drop_duplicates('name')
data2 = data2.drop_duplicates('name')
# using merge function by setting how='left'
output2 = pd.merge(data1, data2,
                   on='name',
                   how='inner')

# displaying result
# print(output2)
output2.to_csv('final.csv', index=False)
