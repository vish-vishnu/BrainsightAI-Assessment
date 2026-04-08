import os
import nibabel as nib
from nilearn import plotting

# Create output folder
output_folder = "outputs_task1"
os.makedirs(output_folder, exist_ok=True)

# Load T1 image
t1_img = nib.load("dataset1/t1w.nii")

# Plot anatomical image and save
anat_display = plotting.plot_anat(t1_img, title="T1w Image")
anat_display.savefig(os.path.join(output_folder, "t1_image.png"))

# Load mask
mask_img1 = nib.load("dataset1/dmn.nii")
mask_img2 = nib.load("dataset1/language_sensaas.nii")
mask_img3 = nib.load("dataset1/primary_visual.nii")

# Overlay mask and save
display1 = plotting.plot_roi(mask_img1, bg_img=t1_img, title="Mask Overlay dmn")
display2 = plotting.plot_roi(mask_img2, bg_img=t1_img, title="Mask Overlay language")
display3 = plotting.plot_roi(mask_img3, bg_img=t1_img, title="Mask Overlay primary_visual")

# Save the overlay images
display1.savefig(os.path.join(output_folder, "mask_overlay_dmn.png"))
display2.savefig(os.path.join(output_folder, "mask_overlay_language.png"))
display3.savefig(os.path.join(output_folder, "mask_overlay_primary_visual.png"))
plotting.show()