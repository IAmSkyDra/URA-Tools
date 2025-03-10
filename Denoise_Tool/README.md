# Denoise Tool
## Description
Speech denoising is the process of removing unwanted noise from speech signals while preserving the integrity of the speech itself. 
The problem of speech denoising arises when speech signals are corrupted by various types of noise, such as background noise, microphone noise, or electrical interference.

This project aim to denoise signal given input is the noisy signal expected output will give us the denoised signal and evaluate it. The module include 2 methods: Spectral subtraction and FRCRN.

## Prerequisites
To use the FRCNR module, you need to deploy Python environment and install the modules in requirements.txt \
Quick install can be implemented by 'pip install -r requirements.txt'
## Usage explaination
To use the module, locate to the folder that's contain the module. The folder's path should be somewhat similar to: "C:\...\URA-Tools\Denoise_Tool\FRCRN_denoise". \ 
Then, open "runner.py" and paste the path inside the main.main() function to the path that contains the file that's need to be denoised. The second parameter of the main function represents the file type ("wav" or "mp4"). The audio files MUST be .wav file, while the video file MUST be .mp4 file.
After running the runner, the denoised file then can be found in the same folder with its name added the word 'denoised'. \
Example of runner.py

> 
> import main
> main.main(r"C:\Users\nghna\Downloads\Test","mp4")
>

## Reference
We based on those github to denoise by FRCRN: \
https://github.com/alibabasglab/FRCRN/tree/main  \
https://github.com/modelscope/modelscope

## Author and contacts
1. Khai Tam: Baseline codes and denoise tools. \
2. Nguyen Huu Nam Phong: Leverage the tool, add video related functions and ease the use. \
Contact if need help: phong.nguyenhuunam@hcmut.edu.vn


