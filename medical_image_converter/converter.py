# Conteúdo do arquivo converter.py
import pydicom
import nibabel as nib
import nrrd
from PIL import Image

class MedicalImageConverter:
    def __init__(self, input_path):
        self.input_path = input_path
        self.supported_formats = {
            '.dcm': self.load_dicom,
            '.nii': self.load_nifti,
            '.nii.gz': self.load_nifti,
            '.nrrd': self.load_nrrd
        }

    def convert_to_png(self, output_path):
        img = self.load_image()
        img.save(output_path + '.png')

    def convert_to_jpg(self, output_path):
        img = self.load_image()
        img.save(output_path + '.jpg')

    def load_image(self):
        file_ext = self.input_path.lower().split('.')[-1]
        if file_ext in self.supported_formats:
            return self.supported_formats[file_ext]()
        else:
            raise ValueError("Formato de imagem não suportado.")

    def load_dicom(self):
        ds = pydicom.dcmread(self.input_path)
        pixel_array = ds.pixel_array
        return Image.fromarray(pixel_array)

    def load_nifti(self):
        img = nib.load(self.input_path)
        data = img.get_fdata()
        return Image.fromarray(data.squeeze())

    def load_nrrd(self):
        data, header = nrrd.read(self.input_path)
        return Image.fromarray(data)
