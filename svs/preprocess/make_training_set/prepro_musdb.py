# To run this code, you first need to parse musdb-lyrics-(a), single vocal regions of musdb
# Check https:\\\\zenodo.org\\record\\3989267#.Y2JwxC_kHT8
# Schulze-Forster, K., Doire, C., Richard, G., & Badeau, R. "Phoneme Level Lyrics Alignment and Text-Informed Singing Voice Separation." IEEE\\ACM Transactions on Audio, Speech and Language Processing (2021).

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
    "F:\\Stuff\\musdb_a_train\\train\\audio\\vocals\\a\\*.wav"
)
test_list = glob.glob(
    "F:\\Stuff\\musdb_a_train\\test\\audio\\vocals\\a\\*.wav"
)

os.makedirs(
    f"C:\\Users\\Carson\\Documents\\data\\{args.samplerate_folder_name}\\musdb_a_train",
    exist_ok=True,
)
def task1(path):
    basename = os.path.basename(path)
    wav, sr = librosa.load(path, sr=args.sample_rate, mono=True)
    sf.write(
        f"C:\\Users\\Carson\\Documents\\data\\{args.samplerate_folder_name}\\musdb_a_train\\{basename}",
        wav,
        args.sample_rate,
        subtype="PCM_16",
    )


os.makedirs(
    f"C:\\Users\\Carson\\Documents\\data\\{args.samplerate_folder_name}\\musdb_a_test",
    exist_ok=True,
)
def task2(path):
    basename = os.path.basename(path)
    wav, sr = librosa.load(path, sr=args.sample_rate, mono=True)
    sf.write(
        f"C:\\Users\\Carson\\Documents\\data\\{args.samplerate_folder_name}\\musdb_a_test\\{basename}",
        wav,
        args.sample_rate,
        subtype="PCM_16",
    )

if __name__ == "__main__":
    r = thread_map(task1, train_list)
    r = thread_map(task2, test_list)