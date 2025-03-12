# Denoise Tool
## TL, DR
How to use (razor language): open terminal and run 'pip install -r requirements.txt', then run .bat files, enter path and type then press run.

## Description
Speech denoising is the process of removing unwanted noise from speech signals while preserving the integrity of the speech itself. 
The problem of speech denoising arises when speech signals are corrupted by various types of noise, such as background noise, microphone noise, or electrical interference.

This project aim to denoise signal given input is the noisy signal expected output will give us the denoised signal and evaluate it. The module include 2 methods: Spectral subtraction and FRCRN.

## Prerequisites
To use the FRCNR module, you need to deploy Python environment and install the modules in requirements.txt \
Quick install can be implemented by 'pip install -r requirements.txt'
## Usage explaination
To use the module, locate to the folder that's contain the module. The folder's path should be somewhat similar to: "C:\...\URA-Tools\Denoise_Tool\FRCRN_denoise". \ 
Then, open "runner.bat" and paste the path inside the path textbox. The second parameter is the file type ("mov" or "mp4"). Click on this to toggle.
After running the runner, the denoised file then can be found in the same folder with its name added the word 'denoised'. \
Example of runner.bat
![image](https://github.com/user-attachments/assets/123d2b7d-ba9b-4361-92a4-130476fd8b9c)


## Reference
We based on those github to denoise by FRCRN: \
https://github.com/alibabasglab/FRCRN/tree/main  \
https://github.com/modelscope/modelscope

## Author and contacts
1. Khai Tam: Baseline codes and denoise tools. \
2. Nguyen Huu Nam Phong: Leverage the tool, add video related functions and ease the use. \
Contact if need help: phong.nguyenhuunam@hcmut.edu.vn


