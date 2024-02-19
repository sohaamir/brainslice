import argparse
from .slice import show_slice

def entry_point():
    parser = argparse.ArgumentParser(
        description="Display a NIFTI image slice with optional brightness and contrast adjustments."
    )
    parser.add_argument("file_path", help="Path to the NIFTI file")
    parser.add_argument("plane", choices=['axial', 'sagittal', 'coronal'], help="Plane of the slice")
    parser.add_argument("slice_number", type=int, help="Index of the slice")
    parser.add_argument("--brightness", type=float, default=1.0, help="Brightness adjustment factor (default: 1.0)")
    parser.add_argument("--contrast", type=float, default=1.0, help="Contrast adjustment factor (default: 1.0)")

    args = parser.parse_args()
    show_slice(
        file_path=args.file_path,
        plane=args.plane,
        slice_number=args.slice_number,
        brightness=args.brightness,
        contrast=args.contrast
    )

if __name__ == "__main__":
    entry_point()
