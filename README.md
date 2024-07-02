# MedSyn
Official PyTorch implementation for paper *MedSyn: Text-guided Anatomy-aware Synthesis of High-Fidelity 3D CT Images*, accepted by *IEEE Transactions on Medical Imaging*.

### [[Paper](https://arxiv.org/abs/2310.03559)] [[Project](https://batmanlab.github.io/medsyn.github.io/)]

<p align="center">
  <img width="70%" height="%70" src="figure/schematic.jpg">
</p>

## Table of Contents

1. [Environment Setup](#environment-setup)
2. [Pre-processing Data](#pre-processing-data)
3. [Training](#training)
4. [Inference](#inference)
5. [Additional Scripts](#additional-scripts)
6. [Generated Samples](#generated-samples)
7. [Citation](#citation)
8. [License and Copyright](#license-and-copyright)
9. [Contact](#contact)

## Environment Setup

## Pre-processing Data

Refer to the `preprocess` folder

## Training

Refer to the `src` folder

## Training

Refer to the `src` folder

## Inference

## Additional Scripts

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

## Contact
