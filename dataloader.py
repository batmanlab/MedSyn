"""
Author: Duy-Phuong Dao
Email: phuongdd.1997@gmail.com (or duyphuongcri@gmail.com)
"""

import torch
import monai
from torch.utils.data import DataLoader

from monai.transforms import (
    Compose,
    LoadImaged,
    AddChanneld,
    ThresholdIntensityd,
    NormalizeIntensityd,
    SpatialPadd,
    RandFlipd,
    RandSpatialCropd,
    Orientationd,
    ToTensord,
    RandAdjustContrastd,
    RandAffined,
    RandRotated,
    RandZoomd,
    RandSpatialCropd,
    RandGaussianNoised,
    ConcatItemsd,
    SpatialCropd,
    CenterSpatialCropd,
    ScaleIntensityRanged,
    RandCropByLabelClassesd,
    Identityd
)


def get_transforms(args):
    train_target_transforms = Compose(
        [
            LoadImaged(keys=["image"]),
            AddChanneld(keys=["image"]),
            # Orientationd(keys=["image"], axcodes="RAS"),
            ThresholdIntensityd(keys=["image"], threshold=300, above=False),
            NormalizeIntensityd(keys=["image"], subtrahend=-362, divisor=662),
            RandFlipd(keys=["image"], prob=0.5, spatial_axis=0),
            RandZoomd(keys=["image"], prob=0.2, mode='area'),
            RandRotated(keys=["image"], prob=0.2, mode="bilinear", range_x=0.2, range_y=0.2,
                        range_z=0.2),
            RandSpatialCropd(
                keys=["image"], roi_size=[args.crop_size, args.crop_size, args.crop_size],
                max_roi_size=[args.crop_size, args.crop_size, args.crop_size], random_center=True, random_size=True,
            ),
            SpatialPadd(keys=["image"], spatial_size=[args.crop_size, args.crop_size, args.crop_size]),
            ToTensord(keys=["image"]),
        ]
    )
    return train_target_transforms


def get_transforms_normal(shape):
    train_target_transforms = Compose(
        [
            LoadImaged(keys=["image", "text"]),
            # Orientationd(keys=["image"], axcodes="IRP"),
            # ThresholdIntensityd(keys=["image"], threshold=300, above=False),
            # NormalizeIntensityd(keys=["image"], subtrahend=-362,divisor=662),
            # RandSpatialCropd(
            #     keys=["image"], roi_size=shape,
            #     max_roi_size=shape, random_center=True, random_size=False,
            # ),
            # SpatialPadd(keys=["image"], spatial_size=shape),
            ToTensord(keys=["image", "text"]),
        ]
    )

    return train_target_transforms


def get_transforms_normal_notext(shape):
    train_target_transforms = Compose(
        [
            LoadImaged(keys=["image"]),
            ToTensord(keys=["image"]),
        ]
    )

    return train_target_transforms


def get_transforms_normal_seg(shape):
    train_target_transforms = Compose(
        [
            LoadImaged(keys=["image", "lobe", "airway", "vessel", "text"]),
            # AddChanneld(keys=["image"]),
            # Orientationd(keys=["image"], axcodes="IRP"),
            # ThresholdIntensityd(keys=["image"], threshold=300, above=False),
            # NormalizeIntensityd(keys=["image"], subtrahend=-362,divisor=662),
            # RandSpatialCropd(
            #     keys=["image"], roi_size=shape,
            #     max_roi_size=shape, random_center=True, random_size=False,
            # ),
            # SpatialPadd(keys=["image"], spatial_size=shape),
            ToTensord(keys=["image", "lobe", "airway", "vessel", "text"]),
        ]
    )

    return train_target_transforms


def get_transforms_normal_seg_notext(shape):
    train_target_transforms = Compose(
        [
            LoadImaged(keys=["image", "lobe", "airway", "vessel"]),
            # AddChanneld(keys=["image"]),
            # Orientationd(keys=["image"], axcodes="IRP"),
            # ThresholdIntensityd(keys=["image"], threshold=300, above=False),
            # NormalizeIntensityd(keys=["image"], subtrahend=-362,divisor=662),
            # RandSpatialCropd(
            #     keys=["image"], roi_size=shape,
            #     max_roi_size=shape, random_center=True, random_size=False,
            # ),
            # SpatialPadd(keys=["image"], spatial_size=shape),
            ToTensord(keys=["image", "lobe", "airway", "vessel"]),
        ]
    )

    return train_target_transforms


def get_transforms_text():
    train_target_transforms = Compose(
        [
            LoadImaged(keys=["text"], reader='NumpyReader'),
            # AddChanneld(keys=["image"]),
            # Orientationd(keys=["image"], axcodes="IRP"),
            # ThresholdIntensityd(keys=["image"], threshold=300, above=False),
            # NormalizeIntensityd(keys=["image"], subtrahend=-362,divisor=662),
            # RandSpatialCropd(
            #     keys=["image"], roi_size=shape,
            #     max_roi_size=shape, random_center=True, random_size=False,
            # ),
            # SpatialPadd(keys=["image"], spatial_size=shape),
            ToTensord(keys=["text"]),
        ]
    )

    return train_target_transforms


def get_transforms_aug(shape, crop_shape):
    train_target_transforms = Compose(
        [
            LoadImaged(keys=["image", "text"]),
            AddChanneld(keys=["image"]),
            # RandGaussianNoised(keys=["image"], prob=0.5, std=0.1),
            RandZoomd(keys=["image"], prob=0.5, mode='area'),
            RandRotated(keys=["image"], prob=0.5, mode="bilinear", range_x=0.2, range_y=0.2,
                        range_z=0.2),
            SpatialPadd(keys=["image"], spatial_size=shape),
            RandSpatialCropd(
                keys=["image"], roi_size=crop_shape,
                max_roi_size=shape, random_center=True, random_size=False,
            ),
            ToTensord(keys=["image", "text"]),
        ]
    )

    return train_target_transforms


def get_transforms_aug_seg(shape, crop_shape):
    train_target_transforms = Compose(
        [
            LoadImaged(keys=["image", "lobe", "airway", "vessel", "text"]),
            AddChanneld(keys=["image", "lobe", "airway", "vessel"]),
            ConcatItemsd(keys=["image", "lobe", "airway", "vessel"], dim=0, name="image"),
            # RandGaussianNoised(keys=["image"], prob=0.5, std=0.1),
            RandZoomd(keys=["image"], prob=0.5, mode='area'),
            RandRotated(keys=["image"], prob=0.5, mode="bilinear", range_x=0.2, range_y=0.2,
                        range_z=0.2),
            SpatialPadd(keys=["image"], spatial_size=shape),
            RandSpatialCropd(
                keys=["image"], roi_size=crop_shape,
                max_roi_size=shape, random_center=True, random_size=False,
            ),
            ToTensord(keys=["image", "text"]),
        ]
    )

    return train_target_transforms


def get_transforms_aug_seg_notext(shape, crop_shape):
    train_target_transforms = Compose(
        [
            LoadImaged(keys=["image", "lobe", "airway", "vessel"]),
            AddChanneld(keys=["image", "lobe", "airway", "vessel"]),
            ConcatItemsd(keys=["image", "lobe", "airway", "vessel"], dim=0, name="image"),
            # RandGaussianNoised(keys=["image"], prob=0.5, std=0.1),
            RandZoomd(keys=["image"], prob=0.5, mode='area'),
            RandRotated(keys=["image"], prob=0.5, mode="bilinear", range_x=0.2, range_y=0.2,
                        range_z=0.2),
            SpatialPadd(keys=["image"], spatial_size=shape),
            RandSpatialCropd(
                keys=["image"], roi_size=crop_shape,
                max_roi_size=shape, random_center=True, random_size=False,
            ),
            ToTensord(keys=["image"]),
        ]
    )

    return train_target_transforms


def get_transforms_aug_seg_320(shape, crop_shape):
    train_target_transforms = Compose(
        [
            LoadImaged(keys=["image", "text"]),
            # AddChanneld(keys=["image"]),
            # RandGaussianNoised(keys=["image"], prob=0.5, std=0.1),
            RandZoomd(keys=["image"], prob=0.5, mode='area'),
            RandRotated(keys=["image"], prob=0.5, mode="bilinear", range_x=0.2, range_y=0.2,
                        range_z=0.2),
            SpatialPadd(keys=["image"], spatial_size=shape),
            RandSpatialCropd(
                keys=["image"], roi_size=crop_shape,
                max_roi_size=shape, random_center=True, random_size=False,
            ),
            ToTensord(keys=["image", "text"]),
        ]
    )

    return train_target_transforms


def get_transforms_seg_multiple():
    train_target_transforms = Compose(
        [
            LoadImaged(keys=["image", "image_sr", "lobe", "airway", "vessel", "text"]),
            AddChanneld(keys=["image_sr", "lobe", "airway", "vessel"]),
            ConcatItemsd(keys=["image_sr", "lobe", "airway", "vessel"], dim=0, name="image_sr"),
            ToTensord(keys=["image", "image_sr", "text"]),
        ]
    )

    return train_target_transforms


def worker_init_fn(worker_id):
    worker_info = torch.utils.data.get_worker_info()
    worker_info.dataset.transform.set_random_state(worker_info.seed % (2 ** 32))


def cache_transformed_text(train_files):
    train_transforms = get_transforms_text()
    train_ds = monai.data.CacheDataset(
        data=train_files, transform=train_transforms, cache_rate=0.0
    )
    return train_ds


def cache_transformed_train_data(train_files, shape):
    train_transforms = get_transforms_normal(shape)
    train_ds = monai.data.CacheDataset(
        data=train_files, transform=train_transforms, cache_rate=1.0
    )
    return train_ds

def cache_transformed_train_data_notext(train_files, shape):
    train_transforms = get_transforms_normal_notext(shape)
    train_ds = monai.data.CacheDataset(
        data=train_files, transform=train_transforms, cache_rate=1.0
    )
    return train_ds

def cache_transformed_train_data_marginalize(train_files, shape):
    train_transforms = get_transforms_seg_multiple()
    train_ds = monai.data.CacheDataset(
        data=train_files, transform=train_transforms, cache_rate=0.0
    )
    return train_ds


def cache_transformed_train_data_seg(train_files, shape):
    train_transforms = get_transforms_normal_seg(shape)
    train_ds = monai.data.CacheDataset(
        data=train_files, transform=train_transforms, cache_rate=0.0
    )
    return train_ds

def cache_transformed_train_data_seg_notext(train_files, shape):
    train_transforms = get_transforms_normal_seg_notext(shape)
    train_ds = monai.data.CacheDataset(
        data=train_files, transform=train_transforms, cache_rate=0.0
    )
    return train_ds


def cache_transformed_train_data_aug(train_files, shape, crop_shape):
    train_transforms = get_transforms_aug(shape, crop_shape)
    train_ds = monai.data.CacheDataset(
        data=train_files, transform=train_transforms, cache_rate=0.0
    )

    return train_ds

def cache_transformed_train_data_aug_seg(train_files, shape, crop_shape):
    train_transforms = get_transforms_aug_seg(shape, crop_shape)
    train_ds = monai.data.CacheDataset(
        data=train_files, transform=train_transforms, cache_rate=0.0
    )

    return train_ds

def cache_transformed_train_data_aug_seg_notext(train_files, shape, crop_shape):
    train_transforms = get_transforms_aug_seg_notext(shape, crop_shape)
    train_ds = monai.data.CacheDataset(
        data=train_files, transform=train_transforms, cache_rate=1.0
    )

    return train_ds

def cache_transformed_train_data_aug_seg_320(train_files, shape, crop_shape):
    train_transforms = get_transforms_aug_seg_320(shape, crop_shape)
    train_ds = monai.data.CacheDataset(
        data=train_files, transform=train_transforms, cache_rate=0.0
    )

    return train_ds


def get_transforms_2D():
    train_target_transforms = Compose(
        [
            LoadImaged(keys=["image", "text"]),
            AddChanneld(keys=["image"]),
            NormalizeIntensityd(keys=["image"], subtrahend=255 / 2.0, divisor=255 / 2.0),
            ToTensord(keys=["image", "text"]),
        ]
    )
    return train_target_transforms


def get_dataset_2D(train_files):
    train_transforms = get_transforms_2D()
    train_ds = monai.data.CacheDataset(
        data=train_files, transform=train_transforms, cache_rate=0.0
    )
    return train_ds
