import os, glob
import SimpleITK as sitk

import numpy as np
from skimage.transform import resize
from joblib import Parallel, delayed

NUM_JOB = 2

def sub_job(batch_index):
    moving_img_list = list(glob.glob("./lung_mask_raw/*.nii.gz"))
    #moving_img_list = list(glob.glob("./airway_raw_nii/*.nii.gz"))
    #moving_img_list = list(glob.glob("./vessel_raw/*.nii.gz"))

    fixed_img = "./Patient_0111262324_Study_CT_CHEST_WITHOUT_CONTRAST_42526394_Series_2_DR_30_0.625_Reg_mask.nii.gz"

    for idx, moving_img in enumerate(moving_img_list):
        if idx % NUM_JOB != batch_index:
            continue
        subject_id = moving_img.split('/')[-1].split('.')[0]
        transform = "./transform_mask/"+subject_id+"_Reg_Atlas_Affine_0GenericAffine.mat"
        
        if not (os.path.exists(transform)) or (not os.path.exists(moving_img)):
            print(transform)
            print(moving_img)
            continue
            
        warped_img = "./moved_lung_mask_256/"+subject_id+"_Reg.nii.gz"
        #warped_img = "./moved_airway_256/"+subject_id+"_Reg.nii.gz"
        #warped_img = "./moved_vessel_256/"+subject_id+"_Reg.nii.gz"

        if os.path.exists(warped_img[:-7]+".npy"):
            continue
        run_result = os.system("antsApplyTransforms -d 3 -i "+moving_img+" -r "+fixed_img+\
                     " -o "+warped_img+" -n NearestNeighbor -t "+transform+" -f 0")

        if run_result == 0:
            result_img = sitk.ReadImage(warped_img)
            result_img = sitk.GetArrayFromImage(result_img)
            if idx == 0:
                print("img size:", result_img.shape) # (292, 316, 316)

            result_img = resize(result_img, (256, 256, 256), order=0, mode='constant', cval=0, preserve_range=True)

            np.save(warped_img[:-7]+".npy", result_img)
            os.unlink(warped_img)
            
if __name__ == '__main__':
    Parallel(n_jobs=NUM_JOB)(delayed(sub_job)(item) for item in range(NUM_JOB))
