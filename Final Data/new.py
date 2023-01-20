import pandas as pd
data = pd.read_csv('final.csv', index_col=None)
# data.drop(data['Frequency_map_of_each_chord'].apply(
#     lambda x: x.count(',') < 8), inplace=True)
df2 = data[data['freq'].apply(
    lambda x: x.count(',') < 8)]
brics = pd.DataFrame.to_csv(df2, 'final2.csv', index=False)
# brics.drop(['Unnamed:0.1'], axis=1, inplace=True)
