# Conteúdo do arquivo setup.py
from setuptools import setup, find_packages

setup(
    name='medical_image_converter',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    description='A library for converting medical images to PNG and JPG formats.',
    long_description=open('README.md').read(),
    install_requires=[
        'pydicom',
        'nibabel',
        'nrrd',
        'Pillow'
    ],
)
