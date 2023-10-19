import os
import glob
import argparse

import librosa
import soundfile as sf
from tqdm.contrib.concurrent import thread_map


parser = argparse.ArgumentParser(description="dataset parameter")
parser.add_argument(
    "--sample_rate",
    type=int,
    default=24000,
    help="Sequence duration in seconds" "value of <=0.0 will use full/variable length",
)
parser.add_argument("--samplerate_folder_name", type=str, default="24k")

args, _ = parser.parse_known_args()

train_list = glob.glob(
    "F:/Stuff/k_multitimbre/01.데이터/1.Training/원천데이터/*/*/*/*/*/*.wav"
)
valid_list = glob.glob(
    "F:/Stuff/k_multitimbre/01.데이터/2.Validation/원천데이터/*/*/*/*/*/*.wav"
)

path_list = train_list + valid_list


os.makedirs(
    f"C:/Users/Carson/Documents/data/{args.samplerate_folder_name}/k_multitimbre",
    exist_ok=True,
)

def task(path):
    basename = os.path.basename(path).replace(".wav", "")
    wav, sr = librosa.load(path, sr=args.sample_rate, mono=True)
    sf.write(
        f"C:/Users/Carson/Documents/data/{args.samplerate_folder_name}/k_multitimbre/{basename}.wav",
        wav,
        args.sample_rate,
        subtype="PCM_16",
    )

if __name__ == "__main__":
    r = thread_map(task, path_list)