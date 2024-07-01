#!/bin/bash

# Training with two nodes, low-res training
accelerate launch --multi_gpu --mixed_precision=fp16 --num_processes=2 --main_process_port=29816 video_diffusion_pytorch_low_res_continuous_time_improve_unet_seg.py

# Training with two nodes, high-res training
accelerate launch --multi_gpu --mixed_precision=fp16 --num_processes=2 --main_process_port=29816 video_diffusion_pytorch_SR_continuous_no_temp_attn_and_text_seg.py
