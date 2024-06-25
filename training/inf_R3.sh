#!/bin/bash

# Inference with two nodes, low-res
accelerate launch --multi_gpu --mixed_precision=fp16 --num_processes=2 --main_process_port=29816 video_diffusion_pytorch_low_res_continuous_time_improve_unet_seg_eval_given_prompt.py

# Inference with two nodes, high-res
accelerate launch --multi_gpu --mixed_precision=fp16 --num_processes=2 --main_process_port=29816 video_diffusion_pytorch_SR_continuous_no_temp_attn_and_text_seg_eval.py
