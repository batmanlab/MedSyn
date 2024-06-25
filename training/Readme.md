# Create the MedSyn Conda Enviroment
```
conda env create -f medsyn.txt
```
# Training and Inference of MedSyn

We offer a one-key running bash, listed as follows:

### Step 1: Training the text-conditioned low-res and the high-res Unet
This is a one-key running bash, which will run both low-res and high-res. But the training can be done independently
```bash
sh run_R3.sh
```

### Step 2: Running inference

```bash
python 2_run_registration.py
```
