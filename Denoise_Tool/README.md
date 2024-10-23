# Denoise Tool
## Description
Speech denoising is the process of removing unwanted noise from speech signals while preserving the integrity of the speech itself. 
The problem of speech denoising arises when speech signals are corrupted by various types of noise, such as background noise, microphone noise, or electrical interference.

This project aim to denoise signal given input is the noisy signal expected output will give us the denoised signal and evaluate it. The module include 2 methods: Spectral subtraction and FRCRN.

## Prerequisites
To use the FRCNR module, you need to deploy Python environment and install the following modules:

> modelscope
> 
> matplotlib==3.7.3
> 
> numba==0.58.0
> 
> numpy==1.25.2
> 
> python=3.8.8
> 
> pesq==0.0.4
> 
> pypesq==1.2.4
> 
> pystoi==0.3.3
> 
> scipy==1.11.4
> 
> soundfile
> 
> torch==2.1.0+cu118
> 
> torchaudio==2.1.0+cu118
> 
> torchmetrics
> 
> jupyterlab

Quick install can be implemented by 'pip install requirements.txt'
## Usage explaination
To use the module, open the file FRCRN_denoise\Denoise_module.ipynb. Other files in this folder provide modules to help this tool function. Open this file in Jupiter Environment is the most ideal method, but using other IDE such as Visual Studio Code is fine. Make sure to do the above prerequisites step before continue.
### 1. Import modules
Run the first code block to import modules into the tool. If the code block prints the version of the imported linrary, the package importation is completed.

The block of code below this is the helper functions. Some functions does assist the main module in denoising the audio files in tasks such as plotting a spectrogram (plot_specgram) or a waveform (plot_waveform); playing, copying or resampling the audio file. Make sure to run that before ascending to the following steps.
### 2. Spectral Subtract method
#### 2.1. Define the path
The path of each audio file is defined in each element of the 'bahna_dataset' array. If the audio is located in another folder, the path can be changed by changing the string parameter of the 'Path()' function. Make sure the string representing the path point to the folder containing the audio only. The audio should be formatted as '.wav' file. Once this step is completed succesfully, the cell will print out the path to the file which its name is the first in alphabetical order of the folder. The following figure highlight where is the changeable string.

![Define the path](https://github.com/Windyy-1007/Denoise-module-main/assets/138313978/a31251ad-4322-4e0b-922a-ce4307e0b703)

#### 2.2. Denoise the audio
Run the following cell of the path defining step to create a dataframe to record statistics. Then run the next cell to start the denoise stage. The module then calculate the noise level, perform a noise reduction by simply subtract the frequency components of noises from the noisy audio to get a cleaned/enhanced speech. Then the audio is saved into the destinated folder.

![Denoise the audio](https://github.com/Windyy-1007/Denoise-module-main/assets/138313978/9b721cd2-ddae-42ac-b9f5-bded2723b836)

Once this step is completed succesfully, you will see the output return the path of the audio files and the denoised audio files.
### 3. FRCNR method
#### 3.1. Resampling audio files
The architecture require the sampling rate fs is 16khz. Therefore, audio files must be resampled to that signal. To resampling the file, change the string path in the inner-most parameter of "input_directory" to the folder of the audio file that need sampling, while the path of "output_directory" is the folder that will contain resampled file. "target_sampling_rate" should be set to 16000.

![Resampling audio files](https://github.com/Windyy-1007/Denoise-module-main/assets/138313978/337cda0b-c872-4f18-ada9-b6da1ca3e489)

#### 3.2 Define the path
This step is exactly the same as the privious method. The path of each audio file is defined in each element of the 'bahna_dataset_FRCRN' array. If the audio is located in another folder, the path can be changed by changing the string parameter of the 'Path()' function. Make sure the string representing the path point to the folder containing the audio only. The audio should be formatted as '.wav' file. Once this step is completed succesfully, the cell will print out the path to the file which its name is the first in alphabetical order of the folder. The following figure highlight where is the changeable string.

#### 3.3. Denoise the audio
Run the following cell of the path defining step to create a dataframe to record statistics. Then run the next cell to import necessary modules. Fianlly run the following cell to start the denoise stage. The module compute masks (boolean arrays) in the time/frequency domain based on the input noisy speech to get a cleaned/enhanced speech. Then the audio is saved into the destinated folder. 

![Denoise the audio](https://github.com/Windyy-1007/Denoise-module-main/assets/138313978/e156a73b-ab41-4abf-9806-d24de8954892)


Once this step is completed succesfully, you will see the output return the path of the audio files and the denoised audio files.

### 4. Evaluation
Since PESQ Score only support for sampling rate Fs = 8khz (defined as narrow band) or 16khz (defined as wide band) only so we have to resample it. The [8] cell provide a resampling method, while the [9] cell copy those files to another dictionary.

![Resampling before evaluate](https://github.com/Windyy-1007/Denoise-module-main/assets/138313978/35c1dc2d-30e3-49e0-b9e4-2c44b4699a39)

Run the first cell to import the files. Then run two following cells to evaluate in PESQ and STOI metrics, subsequencely. To evaluate both metrics and multiple files as once, run two last cells to go through evaluate process, and to retrun the results.
Onve the process is done succesfully, the output should return a table with 2 columns representing 2 methods, and n row with n is the number of evaluated audio file.


## Reference
We based on those github to denoise by FRCRN: \
https://github.com/alibabasglab/FRCRN/tree/main  \
https://github.com/modelscope/modelscope

## Author and contacts
1. Khai Tam \
2. Nguyen Huu Nam Phong. \
Contact if need help: phong.nguyenhuunam@hcmut.edu.vn


