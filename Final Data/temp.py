import pandas as pd
import json
data = pd.read_csv('filter_fs.csv', index_col=None)
music_notes1 = ["A", "A#", "B", "C", "C#",
                "D", "D#", "E", "F", "F#", "G", "G#"]
music_notes2 = ["C", "C#",
                "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

lst = []

Keys = data['scale_x'].tolist()
Capos = data['capo'].tolist()
Chord = data['chords'].tolist()
freq_chord = data['freq'].to_list()
f = open("dict.txt", 'a+')
# print(freq_chord[0])
# res = json.loads(str(freq_chord[0]))
# print(type(res))
newCapo = []
for Capo in Capos:
    if (Capo == "no capo"):
        newCapo.append(0)
    else:
        newCapo.append(ord(Capo[0])-ord('0'))
print(newCapo)
i = 0
for Key in Keys:
    s = ""
    s += Key[0]
    scale = "M"
    if (len(Key) > 1 and Key[1] == '#'):
        s += Key[1]
    elif (len(Key) > 1 and Key[1] == 'm'):
        scale = "m"
    if (len(Key) > 2 and Key[2] == 'm'):
        scale = "m"
    if (scale == "m"):
        freq_chord[i] = freq_chord[i].replace("\'", "\"")
        index = (music_notes1.index(s)-newCapo[i]+12) % 12
        freq_chord[i] = json.loads(str(freq_chord[i]))
        temp_dict = {}
        for key in freq_chord[i]:
            temp_key = ""
            for j in range(len(key)):
                if (key[j] == '#'):
                    continue
                tempi = key[j]
                if (key[j] >= 'A' and key[j] <= 'G'):
                    tempi = key[j]
                    if (j+1 < len(key) and key[j+1] == '#'):
                        # j = j+1
                        tempi = tempi+'#'
                    tempi = music_notes1[(
                        music_notes1.index(tempi)-index+12) % 12]
                temp_key += tempi
            temp_dict.update({temp_key: freq_chord[i][key]})
        i += 1
        # print(temp_dict)
        # f.write(str(temp_dict))
        # f.write("\n")
        lst.append(temp_dict)
    else:
        freq_chord[i] = freq_chord[i].replace("\'", "\"")
        index = (music_notes2.index(s)-newCapo[i]+12) % 12
        freq_chord[i] = json.loads(str(freq_chord[i]))
        temp_dict = {}
        for key in freq_chord[i]:
            temp_key = ""
            for j in range(len(key)):
                if (key[j] == '#'):
                    continue
                tempi = key[j]
                if (key[j] >= 'A' and key[j] <= 'G'):
                    tempi = key[j]
                    if (j+1 < len(key) and key[j+1] == '#'):
                        # j = j+1
                        tempi = tempi+'#'
                    tempi = music_notes2[(
                        music_notes2.index(tempi)-index+12) % 12]
                temp_key += tempi
            temp_dict.update({temp_key: freq_chord[i][key]})
        i += 1
        # f.write(str(temp_dict))
        # f.write("\n")
        lst.append(temp_dict)
print(lst)

data = data.assign(Freq_map=lst)
data.drop(['freq'], axis=1, inplace=True)

brics = pd.DataFrame.to_csv(data, 'lol1.csv', index=False)
# brics.drop(['Unnamed:0.1'], axis=1, inplace=True)

# print(data.head())
