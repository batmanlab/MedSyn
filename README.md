# MedSyn
This repository is by [Li Sun][http://xuyanwu.github.io](https://lisun-ai.github.io/) and [Yanwu Xu](http://xuyanwu.github.io)
and contains the [PyTorch](https://pytorch.org) source code to
reproduce the experiments in our TMI paper [MedSyn: Text-guided Anatomy-aware Synthesis of High-Fidelity 3D CT Images](https://arxiv.org/abs/2310.03559).

# Data Preprocessing

Refer to the preprocessing folder

# Training and Inference

Refer to the training folder

# Generated Examples


| Low-Res|  High-Res
:-------------------------:|:-------------------------:
![](figure/low_res/40004330_Reg.gif)  |  ![](figure/high_res/40004330_Reg.gif)
![](figure/low_res/40013558_Reg.gif)  |  ![](figure/high_res/40013558_Reg.gif)
![](figure/low_res/40017881_Reg.gif)  |  ![](figure/high_res/40017881_Reg.gif)
![](figure/low_res/40019171_Reg.gif)  |  ![](figure/high_res/40019171_Reg.gif)

# Comparisons

<p align="center">
  <img width="75%" height="%75" src="https://github.com/batmanlab/MedSyn/blob/main/figure/visualize_slice_v3.pdf">
</p>

# Generation Conditioned on Reports

<p align="center">
  <img width="75%" height="%75" src="https://github.com/batmanlab/MedSyn/blob/main/figure/prompt_comparison.pdf">
</p>

# Generation Conditioned on Segmentation Mask

<p align="center">
  <img width="75%" height="%75" src="https://github.com/batmanlab/MedSyn/blob/main/figure/marginalization.pdf">
</p>


# If you find this repo useful please cite below:

```
@ARTICLE{10566053,
  author={Xu, Yanwu and Sun, Li and Peng, Wei and Jia, Shuyue and Morrison, Katelyn and Perer, Adam and Zandifar, Afrooz and Visweswaran, Shyam and Eslami, Motahhare and Batmanghelich, Kayhan},
  journal={IEEE Transactions on Medical Imaging}, 
  title={MedSyn: Text-guided Anatomy-aware Synthesis of High-Fidelity 3D CT Images}, 
  year={2024},
  doi={10.1109/TMI.2024.3415032}}
```
