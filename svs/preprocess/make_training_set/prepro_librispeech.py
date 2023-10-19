import os
import glob
import argparse

import librosa
import soundfile as sf
from p_tqdm import p_map

parser = argparse.ArgumentParser(description="dataset parameter")
parser.add_argument(
    "--sample_rate",
    type=int,
    default=24000,
    help="Sequence duration in seconds" "value of <=0.0 will use full/variable length",
)
parser.add_argument("--samplerate_folder_name", type=str, default="24k")

args, _ = parser.parse_known_args()

path_1 = glob.glob('F:\\Stuff\\LibriSpeech\\train-clean-360\\*\\*\\*.flac')
path_2 = glob.glob('F:\\Stuff\\LibriSpeech\\train-clean-100\\*\\*\\*.flac')
path_3 = glob.glob('F:\\Stuff\\LibriSpeech\\dev-clean\\*\\*\\*.flac')
path_4 = glob.glob('F:\\Stuff\\LibriSpeech\\test-clean\\*\\*\\*.flac')

# path_1 = glob.glob("F:/Stuff/LibriSpeech/train-clean-360/*/*/*.wav")
# path_2 = glob.glob("F:/Stuff/LibriSpeech/train-clean-100/*/*/*.wav")
# path_3 = glob.glob("F:/Stuff/LibriSpeech/dev-clean/*/*/*.wav")
# path_4 = glob.glob("F:/Stuff/LibriSpeech/test-clean/*/*/*.wav")


path_list = path_1 + path_2 + path_3 + path_4


os.makedirs(
    f"C:/Users/Carson/Documents/data/{args.samplerate_folder_name}/LibriSpeech_train-clean-360",
    exist_ok=True,
)
os.makedirs(
    f"C:/Users/Carson/Documents/data/{args.samplerate_folder_name}/LibriSpeech_train-clean-100",
    exist_ok=True,
)
os.makedirs(
    f"C:/Users/Carson/Documents/data/{args.samplerate_folder_name}/LibriSpeech_dev-clean",
    exist_ok=True,
)
os.makedirs(
    f"C:/Users/Carson/Documents/data/{args.samplerate_folder_name}/LibriSpeech_test-clean",
    exist_ok=True,
)


def task(path):
    basename = os.path.basename(path).replace(".flac", "")
    folder_name = path.split("\\")[-4]
    wav, sr = librosa.load(path, sr=args.sample_rate, mono=True)
    sf.write(
        f"C:/Users/Carson/Documents/data/{args.samplerate_folder_name}/LibriSpeech_{folder_name}/{basename}.wav",
        wav,
        args.sample_rate,
        subtype="PCM_16",
    )

if __name__ == "__main__":
    r = p_map(task, path_list)