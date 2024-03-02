import os
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
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
    slice_img = adjust_brightness_contrast(Image.fromarray(slice_img_array), brightness, contrast)

    # Convert the PIL Image back to a NumPy array for display
    slice_img_for_display = np.asarray(slice_img)

    # Extract the original image name without extension
    original_image_name = os.path.splitext(os.path.basename(file_path))[0]

    # Build filename with suffixes
    suffixes = [
        f"_{slice_number}",
        f"_{plane}",
        f"_brightness_{brightness:.1f}",  # 2.0 is a good default value
        f"_contrast_{contrast:.1f}",      # 1.5 is a good default value
        f"_{colourmap}"
    ]
    output_file_name = original_image_name + "".join(suffixes) + ".png"
    
    # Define the output directory (you can adjust this path as needed)
    output_dir = "brainslices"
    os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it does not exist
    
    # Full path for the output image
    output_path = os.path.join(output_dir, output_file_name)

    # Display and save the slice using Matplotlib
    fig, ax = plt.subplots()
    ax.imshow(slice_img_for_display, cmap=colourmap)  # Use the adjusted image for display
    ax.axis('off')  # Hide the axis

    # Save the figure
    fig.savefig(output_path, bbox_inches='tight', pad_inches=0)
    plt.close(fig)  # Close the figure to free memory

    print(f"Image saved as '{output_path}'.")

if __name__ == '__main__':
    # Example usage
    file_path = 'path/to/your/input/image.nii'
    plane = 'coronal'
    slice_number = 150
    show_slice(file_path, plane, slice_number)
