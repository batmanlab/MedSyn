import glob
import SimpleITK as sitk
import numpy as np

HIGH_THRESHOLD = 600
LOW_THRESHOLD = -1024

#img_folder = './results/img_256/'
#save_folder = './results/img_256_postprocess/'
img_folder = './results/img_256_standard/'
save_folder = './results/img_256_standard_postprocess/'

for filename in glob.glob(img_folder+"*.nii.gz"):
    if ("airway" in filename) or ("lobe" in filename) or ("vessel" in filename):
        continue
    #if "cardiomegaly" not in filename:
    #if "bullae" not in filename:
    if "effusion" not in filename:
        continue

    img = sitk.ReadImage(filename)
    img = sitk.GetArrayFromImage(img)

    img[img>1]=1
    img[img<-1]=-1

    img = np.flip(img, 1)
    img = img*(HIGH_THRESHOLD-LOW_THRESHOLD) + LOW_THRESHOLD

    #print(img.min(), img.max())

    img = sitk.GetImageFromArray(img.astype(np.int16))
    sitk.WriteImage(img, save_folder+filename.split('/')[-1])
