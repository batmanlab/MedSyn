# Pre-process Data for training MedSyn

The data preprocessing pipeline consists of six steps, listed as following:

### Step 1: Segment lung from CT scans, because we use lung mask for registration

```bash
python 1_seg_lung.py --img_folder path_to/
```
The ``Patient_0111262324_Study_CT_CHEST_WITHOUT_CONTRAST_42526394_Series_2_DR_30_0.625_Reg_mask.nii.gz`` file is the lung mask of the Atlas image.
We use [lungmask](https://github.com/JoHof/lungmask) to segment lung.

### Step 2: Run registration

```bash
python 2_run_registration.py
```

We use registration on the lung mask for faster convergence and more robust performance. This is the most time-consuming step, it takes about 7 min per sample.

We use [ANTs](https://stnava.github.io/ANTs/) for image registration.

### Step 3: Apply registration transform to images

```bash
python 3_transform_image.py
```

### Step 4: Run vessel segmentation

```bash
python 4_run_vessel_seg.py
```

We use [TotalSegmentator](https://github.com/wasserth/TotalSegmentator) for vessel segmentation.

### Step 5:  Apply registration transform to lung masks

```bash
python 5_transform_lung_mask.py
```

### Step 6:  Run airway segmentation

```bash
sh 6_run_airway_segment.sh
```
We use [NaviAirway](https://github.com/AntonotnaWang/NaviAirway) for airway segmentation.