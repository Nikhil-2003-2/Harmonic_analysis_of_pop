import pandas as pd
from csv import writer

import pandas as pd

df = pd.read_csv("link.csv")

data = df.drop_duplicates(subset="link")
f = open("link_used.csv", 'a+')
for link in data:
    f.write(link)
    f.write("\n")
