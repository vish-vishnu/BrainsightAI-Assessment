import os
import pydicom
import nibabel as nib
import matplotlib.pyplot as plt

# Create output folder
output_folder = "outputs_task2"
os.makedirs(output_folder, exist_ok=True)

# ------------------ SECTION A ------------------
dicom_folder = "dicom"

dicom_files = [
    os.path.join(dicom_folder, f)
    for f in os.listdir(dicom_folder)
    if f.endswith(".dcm")
]

datasets = [pydicom.dcmread(f) for f in dicom_files]

# Extract metadata
first = datasets[1]
print("Patient ID:", first.PatientID)
print("Study Date:", first.StudyDate)
print("Modality:", first.Modality)

# Count slices
print("Total DICOM slices:", len(datasets))

# Sort
datasets_sorted = sorted(datasets, key=lambda x: int(x.InstanceNumber))

# ------------------ SECTION B ------------------

# Load NIFTI file
nifti_path = "image.nii.gz"
img = nib.load(nifti_path)

# Get data
data = img.get_fdata()
middle_slice = data[:, :, data.shape[2] // 2]

# Print details
print("Shape (dimensions):", data.shape)
print("Data type:", data.dtype) 

# Display middle slice
plt.imshow(middle_slice, cmap="gray")
plt.title("Middle Slice")
plt.axis("off")
plt.savefig(os.path.join(output_folder, "middle_slice.png"))
plt.show()

# ------------------ SECTION C ------------------
if len(datasets_sorted) == data.shape[2]:
    print("Result: CONSISTENT")
else:
    print("Result: MISMATCH")