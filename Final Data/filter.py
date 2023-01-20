
import pandas as pd

# # reading csv files
data1 = pd.read_csv('final2.csv')
scale = data1['scale_x'].to_list()
scale_ = data1['scale_y'].to_list()
bpm_x = data1['bpm_x'].to_list()
bpm_y = data1['bpm_y'].to_list()
for i in range(len(data1)):
    if (scale[i] == "Key Not Find"):
        scale[i] = scale_[i]
    if (bpm_y[i] == "NF"):
        bpm_y[i] = bpm_x[i]
data1['new_scale'] = scale
data1['new_bpm'] = bpm_y
data1.to_csv('filter_fs2.csv', index=False)
# data1 = data1.sort_values[data1['scale_x'] == data1['scale_y']]

# print(data1)
# using merge function by setting how='left'
# output2 = pd.merge(data1, data2,
#                    on='name',
#                    how='inner')

# displaying result
# print(output2)
# output2.to_csv('final.csv', index=False)
