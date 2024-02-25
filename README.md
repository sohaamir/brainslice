# brainslicer

`brainslicer` is a Python package for automatically creating images from T1-anatomical NIFTIs.

It provides the following features:

* Slice Selection: Display slices from axial, sagittal, or coronal planes.
* Brightness and Contrast Control: Fine-tune image appearance for better visualization.
* Colourmap Customization: Choose from a variety of colourmaps to highlight different aspects of the image data.

usage: 
`brainslicer [-h] [--plane {axial,sagittal,coronal}] [--brightness BRIGHTNESS] [--contrast CONTRAST] [--colourmap COLOURMAP] [--list-colourmaps] file_path slice_number`

For more information and usage examples, use the `-h` or `--help` flags.

options:
```
  -h, --help                           show this help message and exit
  --plane {axial,sagittal,coronal}     Plane of the slice

Required arguments:
  file_path             Path to the NIFTI file
  slice_number          Index of the slice

Optional arguments:
  --brightness BRIGHTNESS, -b BRIGHTNESS      Brightness adjustment factor (default: 1.0)
  --contrast CONTRAST, -con CONTRAST          Contrast adjustment factor (default: 1.0)
  --colourmap COLOURMAP, -cmap COLOURMAP      Colourmap to use for displaying the slice (default: 'gray').
  --list-colourmaps                           List all available colourmaps
```
Colourmaps are those supported by `matplotlib.colormap`. See the `matplotlib` [website](https://matplotlib.org/stable/users/explain/colors/colormaps.html) for more information.

# brainslicer-ESGRAN

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sohaamir/brainslicer/blob/main/brainslicer_upscale.ipynb) 
[![Render Notebook](https://img.shields.io/badge/render-nbviewer-orange?logo=jupyter)](https://nbviewer.org/github/sohaamir/brainslicer/blob/main/brainslicer_upscale.ipynb)

Leveraging the significant advances made recently in upscaling images, `brainslicer-ESGRAN` is an integrated notebook that allows for users to both slice and upscale NIFTIs. 

The slices are upscaled using [`Real-ESRGAN`](https://arxiv.org/abs/2107.10833), a Generative Adversarial Network capable of recovering high resolution from low resolution images.

More information is provided in the `Colab` and `Jupyter` notebooks above.

## An example of brainslicer-ESGRAN
<img src="https://raw.githubusercontent.com/sohaamir/brainslicer/main/assets/brainslicer_example.png" width="100%">


