# Conteúdo do arquivo test_converter.py
import unittest
from medical_image_converter.converter import MedicalImageConverter

class TestMedicalImageConverter(unittest.TestCase):
    def test_conversion(self):
        input_file = "exemplo.dcm"
        output_file_png = "exemplo_convertido"
        output_file_jpg = "exemplo_convertido"

        converter = MedicalImageConverter(input_file)

        # Converter para PNG
        converter.convert_to_png(output_file_png)

        # Converter para JPG
        converter.convert_to_jpg(output_file_jpg)

        # Verificar se os arquivos foram criados
        self.assertTrue(os.path.exists(output_file_png + '.png'))
        self.assertTrue(os.path.exists(output_file_jpg + '.jpg'))

if __name__ == '__main__':
    unittest.main()
