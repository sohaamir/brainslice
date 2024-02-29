from setuptools import setup, find_packages

setup(
    name='brainslicer',
    version='0.1.0',
    author='Aamir Sohail',
    description='A tool for displaying NIFTI image slices.',
    packages=find_packages(),
    install_requires=[
        'nibabel',
        'numpy',
        'Pillow',
    ],
    entry_points={
        'console_scripts': [
            'brainslicer=brainslicer.cli:entry_point',
        ],
    },
)
