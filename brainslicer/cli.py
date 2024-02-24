import argparse
from .slice import show_slice

def entry_point():
    parser = argparse.ArgumentParser(
        description="""
        Brainslicer is a command-line utility designed to aid in the examination of NIFTI 
        medical images.  It provides the following features:

        *   Slice Selection:  Display slices from axial, sagittal, or coronal planes.
        *   Brightness and Contrast Control: Fine-tune image appearance for better visualization.
        *   Colormap Customization: Choose from a variety of colormaps to highlight different 
            aspects of the image data.
        
        Usage: brainslicer [OPTIONS] image_file

        Example: brainslicer brain_scan.nii coronal 100 --colourmap hot --brightness 1.3

        For help, use: brainslicer --help or brainslicer -h

        Copyright © Aamir Sohail, 2024. 
        """
    )

    parser.add_argument("file_path", help="Path to the NIFTI file")

    # Plane selection
    parser.add_argument("plane", choices=['axial', 'a', 'sagittal', 's', 'coronal', 'c'], 
                        help="Plane of the slice")

    parser.add_argument("slice_number", type=int, help="Index of the slice")

    # Brightness and contrast 
    parser.add_argument("--brightness", "--b", type=float, default=1.0, 
                        help="Brightness adjustment factor (default: 1.0)")
    parser.add_argument("--contrast", "--con", type=float, default=1.0, 
                        help="Contrast adjustment factor (default: 1.0)")

    parser.add_argument("--colourmap", "--cmap", default='gray',
                        choices=['gray', 'viridis', 'plasma', 'inferno', 'magma', 'cividis', 
                                 'hot', 'bone', 'pink', 'spring', 'summer', 'autumn', 'winter',
                                 'cool', 'Wistia', 'copper', ...],  
                        help="Colourmap to use for displaying the slice (default: 'gray')")

    args = parser.parse_args()
    show_slice(
        file_path=args.file_path,
        plane=args.plane,
        slice_number=args.slice_number,
        brightness=args.brightness,
        contrast=args.contrast,
        colourmap=args.colourmap
    )

if __name__ == "__main__":
    entry_point()
