import os
import nibabel as nib
import numpy as np
from PIL import Image, ImageEnhance

def load_slice(file_path, slice_number, plane='axial'):
    nii_img = nib.load(file_path)
    data = nii_img.get_fdata(dtype=np.float32)
    
    slice_selectors = {
        'axial': lambda d: d[:, :, slice_number],
        'sagittal': lambda d: d[slice_number, :, :],
        'coronal': lambda d: d[:, slice_number, :]
    }

    if plane.lower() in slice_selectors:
        selected_slice = slice_selectors[plane.lower()](data)
        selected_slice = np.rot90(selected_slice)
        # Normalize the slice to the range [0, 255] and convert to uint8
        normalized_slice = ((selected_slice - selected_slice.min()) / 
                            (selected_slice.max() - selected_slice.min()) * 255).astype(np.uint8)
        return normalized_slice
    else:
        raise ValueError("Invalid plane selection. Choose from 'axial', 'sagittal', or 'coronal'.")

def adjust_brightness_contrast(image, brightness=1.0, contrast=1.0):
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness)
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast)
    return image

def show_slice(file_path, plane, slice_number, brightness=1.0, contrast=1.0, colourmap='gray'):
    slice_img_array = load_slice(file_path, slice_number, plane)
    slice_img = Image.fromarray(slice_img_array)
    slice_img = adjust_brightness_contrast(slice_img, brightness, contrast)

    # Extract the original image name without extension
    original_image_name = os.path.splitext(os.path.basename(file_path))[0]
    
    # Generate the output file name
    output_file_name = f"{original_image_name}_{plane}_{slice_number}.png"
    
    # Define the output directory (you can adjust this path as needed)
    output_dir = "brainslices"
    os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it does not exist
    
    # Full path for the output image
    output_path = os.path.join(output_dir, output_file_name)

    # Save the image
    slice_img.save(output_path)
    print(f"Image saved as '{output_path}'.")

if __name__ == '__main__':
    # Example usage
    file_path = 'path/to/your/input/image.nii'
    plane = 'coronal'
    slice_number = 150
    show_slice(file_path, plane, slice_number)
