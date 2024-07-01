#!/bin/bash

# Training with two nodes, low-res training
accelerate launch --multi_gpu --mixed_precision=fp16 --num_processes=2 --main_process_port=29816 train_low_res.py

# Training with two nodes, high-res training
accelerate launch --multi_gpu --mixed_precision=fp16 --num_processes=2 --main_process_port=29816 train_super_res.py
