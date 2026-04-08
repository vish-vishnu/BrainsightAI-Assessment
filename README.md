# Tech Support Assignment

## Task 1: NIFTI Processing
- Loaded T1-weighted image using nibabel
- Visualized using nilearn
- Overlayed mask on T1 image
- Output images saved in task1/outputs/

## Task 2: DICOM & NIFTI Processing
### DICOM:
- Read all .dcm files using pydicom
- Extracted Patient ID, Study Date, Modality
- Counted total slices
- Sorted using InstanceNumber

### NIFTI:
- Loaded NIFTI file
- Printed shape and data type
- Extracted middle slice
- Output saved in task2/outputs/

### Validation:
- Compared DICOM slices with NIFTI depth
- Output: CONSISTENT / MISMATCH

## Libraries Used:
- os
- pydicom
- nibabel
- nilearn
- matplotlib
