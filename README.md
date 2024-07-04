# MedSyn
Official PyTorch implementation for paper *MedSyn: Text-guided Anatomy-aware Synthesis of High-Fidelity 3D CT Images*, accepted by *IEEE Transactions on Medical Imaging*.

### [[Paper](https://arxiv.org/abs/2310.03559)] [[Project](https://batmanlab.github.io/medsyn.github.io/)]

<p align="center">
  <img width="70%" height="%70" src="figure/schematic.jpg">
</p>

## Table of Contents

1. [Environment Setup](#environment-setup)
2. [Pretrained Checkpoint](#pretrained-checkpoint)
3. [Pre-processing Data](#pre-processing-data)
4. [Training](#training)
5. [Inference](#inference)
6. [Additional Scripts](#additional-scripts)
7. [Generated Samples](#generated-samples)
8. [Citation](#citation)
9. [License and Copyright](#license-and-copyright)
10. [Contact](#contact)

## Environment Setup

Refer to the `src` folder 

```
conda env create -f environment.yml
```
In addition to this, you need also install several packages by:

```
pip install monai==0.8.1
pip install accelerate
pip install importlib_metadata
pip install tqdm
pip install einops
pip install einops-exts
pip install ninja
conda install xformers -c xformers
```


## Pretrained Checkpoint

Refer to the `src` folder

Our checkpoint for model pre-trained on UPMC dataset is available [here](https://drive.google.com/file/d/1AAlEN_dB7C0aVMJ81mKBlYnSqMVOk-tl/) (Application required).

## Pre-processing Data

Refer to the `preprocess` folder

## Training

Refer to the `src` folder

This is a one-key running bash, which will run both low-res and high-res. But the training can be done independently
```bash
sh run_train.sh
```

## Inference

Refer to the `src` folder

`./extract_text_feature/extract_text_feature.ipynb`

## Additional Scripts

We give the inference for our text conditional generation in "prompt.ipynb" and the conditional generation with segmentation in "seg_conditional.ipynb"
## Generated Samples

| Low-Res|  High-Res
:-------------------------:|:-------------------------:
![](figure/low_res/40004330_Reg.gif)  |  ![](figure/high_res/40004330_Reg.gif)
![](figure/low_res/40013558_Reg.gif)  |  ![](figure/high_res/40013558_Reg.gif)
![](figure/low_res/40017881_Reg.gif)  |  ![](figure/high_res/40017881_Reg.gif)
![](figure/low_res/40019171_Reg.gif)  |  ![](figure/high_res/40019171_Reg.gif)

### Comparisons

<p align="center">
  <img width="75%" height="%75" src="figure/visualize_slice_v3.jpg">
</p>

### Generation Conditioned on Reports

<p align="center">
  <img width="75%" height="%75" src="figure/prompt_comparison.jpg">
</p>

### Generation Conditioned on Segmentation Mask

<p align="center">
  <img width="75%" height="%75" src="figure/marginalization.jpg">
</p>


## Citation

```
@ARTICLE{medsyn2024,
  author={Xu, Yanwu and Sun, Li and Peng, Wei and Jia, Shuyue and Morrison, Katelyn and Perer, Adam and Zandifar, Afrooz and Visweswaran, Shyam and Eslami, Motahhare and Batmanghelich, Kayhan},
  journal={IEEE Transactions on Medical Imaging}, 
  title={MedSyn: Text-guided Anatomy-aware Synthesis of High-Fidelity 3D CT Images}, 
  year={2024},
  doi={10.1109/TMI.2024.3415032}}
```

## License and Copyright

CC-BY-NC

## Contact
Yanwu Xu [yanwuxu@bu.edu],
Li Sun [lisun@bu.edu],
Kayhan Batmanghelich [batman@bu.edu]
