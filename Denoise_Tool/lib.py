#This script is used to import all the necessary libraries for the project
#The output of this script is the version of the libraries imported

import io
import os
import sys
import math
#import tarfile
import multiprocessing

import scipy
import librosa
import soundfile as sf

import requests
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time
from IPython.display import Audio, display

import torch
import torchaudio
import torchaudio.functional as F
import torchaudio.transforms as T

import parselmouth
from parselmouth.praat import call
from pathlib import Path

from metrics import AudioMetrics
from metrics import AudioMetrics2
#from Audio_metrics import AudioMetrics2
import noise_addition_utils
from pypesq import pesq
import shutil

#import pathlib

print(torch.__version__)
print(torchaudio.__version__)
