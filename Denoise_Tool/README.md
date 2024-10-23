## Problem description
Speech denoising is the process of removing unwanted noise from speech signals while preserving the integrity of the speech itself. \
The problem of speech denoising arises when speech signals are corrupted by various types of noise, such as background noise, microphone noise, or electrical interference.\
This project aim to denoise signal given input is the noisy signal expected output will give us the denoised signal and evaluate it. The module include 3 methods: Spectral subtraction, FRCRN and Noise2noise
## Data usage
Data Usage Note: Bahnar Voice Dataset

The Bahnar voice dataset provided by Prof. Quan Thanh Tho is used for research purposes in this project. If you intend to use this dataset, please contact Prof. Tho to discuss your usage and obtain permission.

## How to use the file
FRCRN module
Step 1: To use the denoise function please go to FRCRN_denoise and first install the requirement packages in requirements.txt\
![image](https://github.com/Khaitam911/Denoise-module/assets/69432976/5919dc20-e3b7-4227-9f63-c19e78ec0433)

Step 2: Go to this file Denoise_module.ipynb and open it (recommend in jupyter lab)\
Step 3: Import the necessary package\
Step 4: Denoise module\
To use Spectral Subtraction method you can go to section Spectral Subtraction then define the path needed to denoised and run the following code. 
 ![image](https://github.com/Khaitam911/Denoise-module/assets/69432976/d6b81dd3-3003-4a63-b32e-fc46af58e7c1)
This method first compute the estimated noise and apply denoised based on the noise level. 
The model simply subtract the frequency components of noises from the noisy audio to get a cleaned/enhanced speech.
![image](https://github.com/Khaitam911/Denoise-module/assets/69432976/5d5f0524-8340-403c-90f0-ee70054677ab)\
The spectral subtraction came up with two major shortcomings
- We have to choose a noise from the audio signal to remove it.
- The noise should be present in the entire audio. 


To use FRCRN we need to resample the signal as the architecture require the sampling rate fs is 16khz if it is not 16khz the model will give bad signal
 ![image](https://github.com/Khaitam911/Denoise-module/assets/69432976/5d5fa537-a9aa-469b-bb97-f1d01b6e3d32)
FRCRN is a Mask-based models which compute masks (boolean arrays) in the time/frequency domain based on the input noisy speech
![image](https://github.com/Khaitam911/Denoise-module/assets/69432976/74545d79-b6ea-42a1-89a6-081c3ede661a)

Demo model can be found here: https://drive.google.com/drive/folders/1vq9QoRC75hIHRN47mC_3NszCxtnR2LFx?usp=sharing \
Place the link to folder in here \
![image](https://github.com/Khaitam911/Denoise-module/assets/69432976/3e137375-a070-4430-a096-2957af715b16)

Step 5: Evaluation Description (For reference)
This part is to evaluate how good a signal is compare to a clean signal. It use the two metrics as follow:
- PESQ (Perceptual Evaluation Of Speech Quality) is an objective and full-reference speech quality evaluation method. The score ranges from -0.5 to 4.5. The higher the score, the better the speech quality.
- STOI (Short-Time Objective Intelligibility) reflects the objective evaluation of speech intelligibility by the human auditory perception system. The STOI value is between 0 and 1. The larger the value, the higher the speech intelligibility , the clearer it is.

## Reference
I based on those github to denoise by FRCRN: \
https://github.com/alibabasglab/FRCRN/tree/main  \
https://github.com/modelscope/modelscope

## Author and contacts
1. Khai Tam \
2. Nguyen Huu Nam Phong. \
Contact if need help: phong.nguyenhuunam@hcmut.edu.vn


