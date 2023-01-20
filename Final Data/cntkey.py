import pandas as pd
import json
data = pd.read_csv('filter_fs.csv', index_col=None)

freq_chord = data['freq'].to_list()
f = open("dict.txt", 'a+')
dict = {}
for i in range(len(freq_chord)):
    freq_chord[i] = freq_chord[i].replace("\'", "\"")
    freq_chord[i] = json.loads(str(freq_chord[i]))
    for key in freq_chord[i]:
        if key in dict:
            dict[key] = dict.get(key)+freq_chord[i].get(key)
            # print(freq_chord[i].get(key))
        else:
            dict[key] = freq_chord[i].get(key)
for key in dict:
    f.write(key+":"+str(dict.get(key))+"\n")
