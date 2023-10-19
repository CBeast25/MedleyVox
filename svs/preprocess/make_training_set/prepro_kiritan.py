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


path_list = glob.glob("F:\\Stuff\\kiritan_revised\\wav\\*.wav")

os.makedirs(
    f"C:\\Users\\Carson\\Documents\\data\\{args.samplerate_folder_name}\\kiritan_revised",
    exist_ok=True,
)

def task(path):
    basename = os.path.basename(path).replace(".wav", "")
    wav, sr = librosa.load(path, sr=args.sample_rate, mono=True)
    # wav_segments, index = librosa.effects.trim(wav, top_db=60)
    intervals = librosa.effects.split(wav, top_db=75)
    for i in range(intervals.shape[0]):
        sf.write(
            f"C:\\Users\\Carson\\Documents\\data\\{args.samplerate_folder_name}\\kiritan_revised\\{basename}_{i}.wav",
            wav[intervals[i, 0] : intervals[i, 1]],
            args.sample_rate,
            subtype="PCM_16",
        )

if __name__ == "__main__":
    r = thread_map(task, path_list)
