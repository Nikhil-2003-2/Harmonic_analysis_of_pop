import pandas as pd
data = pd.read_csv('output.csv', index_col=None)
# data.drop(data['Frequency_map_of_each_chord'].apply(
#     lambda x: x.count(',') < 8), inplace=True)
df2 = data[data['Frquency_map_of_each_chord'].apply(
    lambda x: x.count(',') < 6)]
brics = pd.DataFrame.to_csv(df2, 'data.csv')
# brics.drop(['Unnamed:0.1'], axis=1, inplace=True)
