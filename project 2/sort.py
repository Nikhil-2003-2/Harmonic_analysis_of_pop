import pandas as pd

data = pd.read_csv('new1.csv', index_col=None)
data.drop_duplicates()
rslt_df = data.sort_values(by="Key")
pd.DataFrame.to_csv(rslt_df, 'new3.csv')
# (v*(v+1))/2
# 0 1
# o(v*v)+e
# 1 . (o(v)+O(E))*o(v)
# for(int i=0;i<n;i++){
#     for(auto x;v[i])
# }
