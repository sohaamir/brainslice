import argparse
import matplotlib.pyplot as plt
from .slice import show_slice

def entry_point():
    all_colourmaps = plt.colormaps()

    parser = argparse.ArgumentParser(
        description="""
Brainslicer is a command-line utility designed to aid in the examination of NIFTI anatomical images. 
It provides the following features:

* Slice Selection: Display slices from axial, sagittal, or coronal planes.
* Brightness and Contrast Control: Fine-tune image appearance for better visualization.
* Colourmap Customization: Choose from a variety of colourmaps to highlight different aspects of the image data.

For more information and usage examples, use the -h or --help flags.

Copyright © Aamir Sohail, 2024.""",
        formatter_class=argparse.RawTextHelpFormatter  # Preserve formatting
    )

    # Required Arguments
    positional_group = parser.add_argument_group('Required arguments')
    positional_group.add_argument("file_path", help="Path to the NIFTI file")
    parser.add_argument("--plane", choices=['axial', 'sagittal', 'coronal'], 
                    help="Plane of the slice")
    positional_group.add_argument("slice_number", type=int, help="Index of the slice")

    # Optional Arguments
    optional_group = parser.add_argument_group('Optional arguments')
    optional_group.add_argument("--brightness", "-b", type=float, default=1.0, help="Brightness adjustment factor (default: 1.0)")
    optional_group.add_argument("--contrast", "-con", type=float, default=1.0, help="Contrast adjustment factor (default: 1.0)")
    optional_group.add_argument("--colourmap", "-cmap", default='gray', 
                        help="Colourmap to use for displaying the slice (default: 'gray').")
    optional_group.add_argument("--list-colourmaps", action="store_true", 
                        help="List all available colourmaps")


    args = parser.parse_args()
    # New logic: If the user wants to list all colourmaps, do that and exit
    if args.list_colourmaps:
        print("Available colormaps:", all_colourmaps)
        return  # Exit after listing colourmaps

    # Check if the provided colormap is valid
    if args.colourmap not in all_colourmaps:
        raise ValueError(f"Invalid colormap: {args.colourmap}. Please choose from a valid Matplotlib colormap.")



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
