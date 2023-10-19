# make dict of 다화자 가창데이터 dataset's {same singer: [song_list]}

import os
import glob
import json

train_list = glob.glob(
    "F:\\Stuff\k_multisinger\\01.데이터\\1.Training\\원천데이터\\*\\*\\*\\*\\*.wav"
)
valid_list = glob.glob(
    "F:\\Stuff\k_multisinger\\01.데이터\\2.Validation\\원천데이터\\*\\*\\*\\*\\*.wav"
)

total_list = train_list + valid_list

singer_list = []
for path in total_list:
    song_name = os.path.basename(path).replace(".wav", "")
    song_name_split = song_name.split("_")
    singer_name = "k_multisinger" + " - " + song_name_split[4]
    singer_list.append(singer_name)

singer_list = sorted(list(set(singer_list)))

song_path_dict = {}

for singer in singer_list:
    song_path_dict[singer] = []
for path in total_list:
    song_name = os.path.basename(path).replace(".wav", "")
    song_name_split = song_name.split("_")
    singer_name = "k_multisinger" + " - " + song_name_split[4]
    song_path_dict[singer_name] += [song_name]

with open(".\\same_singer_k_multisinger.json", "w") as json_file:
    json.dump(song_path_dict, json_file, indent=0)
