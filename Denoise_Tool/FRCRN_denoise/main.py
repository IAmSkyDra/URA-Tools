#This script is used to import all the necessary libraries for the project
#The output of this script is the version of the libraries imported

import os

import librosa
import soundfile as sf

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from IPython.display import Audio, display

import torch
import torchaudio
import torchaudio.transforms as T

import parselmouth
from parselmouth.praat import call
from pathlib import Path
import shutil

import moviepy
from moviepy.editor import *
from tqdm import tqdm
print(torch.__version__)
print(torchaudio.__version__)

#-------------------------------------------------------------------------------
# Helper functions.
#-------------------------------------------------------------------------------

def movieToAudio(input_path, output_path):
    # Load the video file
    video = moviepy.editor.VideoFileClip(input_path)

    # Extract the audio from the video
    audio = video.audio

    # Save the audio to a WAV file
    audio.write_audiofile(output_path)

def denoise_audio(input_path, output_path, smoothing_factor):
    # Load the audio file
    snd = parselmouth.Sound(input_path)

    # Apply smoothing to reduce noise
    snd_denoised = snd.copy()
    #snd_denoised = call(snd_denoised, "Smooth", smoothing_factor)
    snd_denoised = call(snd_denoised, "Reduce noise", 0.0, 0.0, 0.025, 80.0, 10000.0, 40.0,-20, "Spectral-subtraction")
    # Save the denoised audio
    snd_denoised.save(output_path, "WAV")
def get_stats(waveform, sample_rate=None, src=None):
    max_ = waveform.max().numpy()
    min_ = waveform.min().numpy()
    mean_ = waveform.mean().numpy()
    std_ = waveform.std().numpy()
    return max_,min_,mean_,std_

def print_stats(waveform, sample_rate=None, src=None):
    if src:
        print("-" * 10)
        print("Source:", src)
        print("-" * 10)
    if sample_rate:
        print("Sample Rate:", sample_rate)
        print("Shape:", tuple(waveform.shape))
        print("Dtype:", waveform.dtype)
        print(f" - Max:     {waveform.max().item():6.3f}")
        print(f" - Min:     {waveform.min().item():6.3f}")
        print(f" - Mean:    {waveform.mean().item():6.3f}")
        print(f" - Std Dev: {waveform.std().item():6.3f}")
        print()
        print(waveform)
        print()
    # max_ = waveform.max().numpy()
    # min_ = waveform.min().numpy()
    # mean_ = waveform.mean().numpy()
    # std_ = waveform.std().numpy()
    # return max_,min_,mean_,std_

def plot_waveform(waveform, sample_rate, title="Waveform", xlim=None, ylim=None):
  waveform = waveform.numpy()

  num_channels, num_frames = waveform.shape
  time_axis = torch.arange(0, num_frames) / sample_rate

  figure, axes = plt.subplots(num_channels, 1)
  if num_channels == 1:
    axes = [axes]
  for c in range(num_channels):
    axes[c].plot(time_axis, waveform[c], linewidth=1)
    axes[c].grid(True)
    if num_channels > 1:
      axes[c].set_ylabel(f'Channel {c+1}')
    if xlim:
      axes[c].set_xlim(xlim)
    if ylim:
      axes[c].set_ylim(ylim)
  figure.suptitle(title)
  plt.show(block=False)

def plot_specgram(waveform, sample_rate, title="Spectrogram", xlim=None):
  waveform = waveform.numpy()
  num_channels, num_frames = waveform.shape
  time_axis = torch.arange(0, num_frames) / sample_rate
  figure, axes = plt.subplots(num_channels, 1)
  if num_channels == 1:
    axes = [axes]
  for c in range(num_channels):
    axes[c].specgram(waveform[c], Fs=sample_rate)
    if num_channels > 1:
      axes[c].set_ylabel(f'Channel {c+1}')
    if xlim:
      axes[c].set_xlim(xlim)
  figure.suptitle(title)
  plt.show(block=False)

def play_audio(waveform, sample_rate):
  waveform = waveform.numpy()
  num_channels, num_frames = waveform.shape
  if num_channels == 1:
    display(Audio(waveform[0], rate=sample_rate))
  elif num_channels == 2:
    display(Audio((waveform[0], waveform[1]), rate=sample_rate))
  else:
    raise ValueError("Waveform with more than 2 channels are not supported.")

def plot_spectrogram(spec, title=None, ylabel='freq_bin', aspect='auto', xmax=None):
  fig, axs = plt.subplots(1, 1)
  axs.set_title(title or 'Spectrogram (db)')
  axs.set_ylabel(ylabel)
  axs.set_xlabel('frame')
  im = axs.imshow(librosa.power_to_db(spec), origin='lower', aspect=aspect)
  if xmax:
    axs.set_xlim((0, xmax))
  fig.colorbar(im, ax=axs)
  plt.show(block=False)

def get_spectrogram(
    n_fft = 400,
    win_len = None,
    hop_len = None,
    power = 2.0,
):
  waveform, _ = get_speech_sample()
  spectrogram = T.Spectrogram(
      n_fft=n_fft,
      win_length=win_len,
      hop_length=hop_len,
      center=True,
      pad_mode="reflect",
      power=power,
  )
  return spectrogram(waveform)
def resample_wav_files(input_path, output_path, target_sr):
    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    # Get a list of all WAV files in the input directory and its subfolders
    for root, dirs, files in os.walk(input_path):
        for file_name in files:
            if file_name.endswith('.wav'):
                # Read the input WAV file
                input_file = os.path.join(root, file_name)
                audio, sr = librosa.load(input_file, sr=target_sr)

                # Write the resampled audio to the output WAV file
                output_dir = os.path.join(output_path, os.path.relpath(root, input_path))
                os.makedirs(output_dir, exist_ok=True)
                output_file = os.path.join(output_dir, file_name)
                sf.write(output_file, audio, target_sr)
def copy_wav_files_to_single_directory(input_path, output_path):
    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    # Get a list of all WAV files in the input directory and its subfolders
    for root, dirs, files in os.walk(input_path):
        for file_name in files:
            if file_name.endswith('.wav'):
                # Copy the WAV file to the output directory with the original filename
                input_file = os.path.join(root, file_name)
                output_file = os.path.join(output_path, file_name)
                shutil.copy2(input_file, output_file)



def main(path, type):
  if (type == "wav"):
    bahna_dataset = sorted(list(Path(path).rglob('*.wav')))
  elif (type == "mp4"):
    video_dataset = sorted(list(Path(path).rglob('*.mp4')))
    for i in video_dataset:
        normalized_path = os.path.normpath(i)
        audio_path = os.path.splitext(normalized_path)[0] + ".wav"
        movieToAudio(normalized_path, audio_path)
        bahna_dataset = sorted(list(Path(path).rglob('*.wav')))
      
  print(bahna_dataset)
  stat_bahna_spectral_subtraction = pd.DataFrame(columns=['Name','Max', 'Min', 'Mean','Std','Noise_level_before_denoised','Max_after_denoised', 'Min_after_denoised', 'Mean_after_denoised','Std_after_denoised','Noise_level_after_denoised'])
  for i in tqdm(bahna_dataset, desc="Processing audio files"):
      print(i)
      waveform, sample_rate = torchaudio.load(i)
      max_,min_,mean_,std_ = get_stats(waveform, sample_rate = sample_rate)
      # Calculate noise level
      if std_!=0 :
          noise_level = 20*( np.log10(std_/max_))
      else:
          noise_level = 0
      normalized_path = os.path.normpath(i)
      input_path = os.path.splitext(normalized_path)[0] + os.path.splitext(normalized_path)[1]
      denoised_path = os.path.splitext(normalized_path)[0] + "_denoised_spectral_subtraction" + os.path.splitext(normalized_path)[1]
      snd = parselmouth.Sound(input_path)
      snd_denoised = snd.copy()
      snd_denoised = call(snd_denoised, "Reduce noise", 0.0, 0.0, 0.025, 80.0, 10000.0, 40.0,noise_level, "Spectral-subtraction")
      # Save the denoised audio
      snd_denoised.save(denoised_path, "WAV")
      print(denoised_path)
      waveform_denoised, sample_rate_denoised = torchaudio.load(denoised_path)
      max_after,min_after,mean_after,std_after=get_stats(waveform_denoised, sample_rate=sample_rate_denoised)
      if std_after!=0 :
          noise_level_after = 10*( np.log10(std_after/max_after))
      else:
          noise_level_after = 0
      df = pd.DataFrame({"Name":[i],"Max":[max_],"Min":[min_],"Mean":[mean_],"Std":[std_],"Noise_level_before_denoised":[noise_level],'Max_after_denoised':[max_after], 'Min_after_denoised':[min_after], 'Mean_after_denoised':[mean_after],'Std_after_denoised':[std_after],'Noise_level_after_denoised':[noise_level_after]})
      stat_bahna_spectral_subtraction=pd.concat([stat_bahna_spectral_subtraction,df], ignore_index=True)
  
  stat_bahna_spectral_subtraction.to_csv('stat_bahna_spectral_subtraction.csv')
  
        
  print("Done")
  if (type == "mp4"):
    video_dataset = sorted(list(Path(path).rglob('*.mp4')))
    audio_dataset = sorted(list(Path(path).rglob('*.wav')))

    for i in tqdm(video_dataset, desc="Processing video files"):
        normalized_path = os.path.normpath(i)
        videoclip = VideoFileClip(normalized_path)
        audio_path = os.path.splitext(normalized_path)[0] + "_denoised_spectral_subtraction" + ".wav"
        print(audio_path)
        audioclip = AudioFileClip(audio_path)
        videoclip = videoclip.set_audio(audioclip)
        videoclip.write_videofile(os.path.splitext(normalized_path)[0] + "_denoised_spectral_subtraction" + ".mp4")
        print(os.path.splitext(normalized_path)[0] + "_denoised_spectral_subtraction" + ".mp4")
    print("Done video")
        
  
  print(stat_bahna_spectral_subtraction)

if __name__ == "__main__":
    main()