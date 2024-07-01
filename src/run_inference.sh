#!/bin/bash

# Inference with two GPUs, low-res
accelerate launch --multi_gpu --mixed_precision=fp16 --num_processes=2 --main_process_port=29816 eval_low_res_given_prompt.py

# Inference with two GPUs, high-res
accelerate launch --multi_gpu --mixed_precision=fp16 --num_processes=2 --main_process_port=29816 eval_super_res.py
