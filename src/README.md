# Create the MedSyn Conda environment
```
conda env create -f environment.yml
```
# Training of MedSyn
This is a one-key running bash, which will run both low-res and high-res. But the training can be done independently
```bash
sh run_train.sh
```
# Extract features from prompt
Refer to `./extract_text_feature/extract_text_feature.ipynb`

# Running inference

```bash
sh run_inference.sh
```

Our model pre-trained on UPMC dataset is available [here](https://drive.google.com/file/d/1AAlEN_dB7C0aVMJ81mKBlYnSqMVOk-tl/) (Application required).