import pandas as pd
import json
data = pd.read_csv('lol1.csv', index_col=None)
music_notes1 = ["A", "A#", "B", "C", "C#",
                "D", "D#", "E", "F", "F#", "G", "G#"]
music_notes2 = ["C", "C#",
                "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

lst = []

# Keys = data['Key'].tolist()
# Capos = data['Capo'].tolist()
# Chord = data['Chord'].tolist()
si = set()
freq_chord = data['Freq_map'].to_list()
for freq in freq_chord:
    freq = freq.replace("\'", "\"")
    freq = json.loads(str(freq))
    for key in freq:
        lst.append(key)
si = set(lst)
print(len(si))
print(sorted(si))
