```markdown
# Medical Image Converter

O Medical Image Converter é uma biblioteca Python que oferece funcionalidades para converter imagens médicas em formatos comuns, como PNG e JPG. Ele suporta vários formatos de entrada, incluindo DICOM, NIfTI e NRRD.

## Instalação

Você pode instalar o Medical Image Converter via pip. Execute o seguinte comando:

```bash
pip install medical_image_converter
```

## Uso

Aqui está um exemplo simples de como usar o Medical Image Converter para converter uma imagem médica de DICOM para PNG:

```python
from medical_image_converter.converter import MedicalImageConverter

input_file = "exemplo.dcm"
output_file_png = "exemplo_convertido"

converter = MedicalImageConverter(input_file)
converter.convert_to_png(output_file_png)
```

Você também pode converter para outros formatos, como JPG:

```python
output_file_jpg = "exemplo_convertido"
converter.convert_to_jpg(output_file_jpg)
```

## Suporte

Este pacote atualmente suporta os seguintes formatos de entrada:

- DICOM (.dcm)
- NIfTI (.nii, .nii.gz)
- NRRD (.nrrd)

E os seguintes formatos de saída:

- PNG (.png)
- JPG (.jpg)

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, novos recursos ou encontrar algum problema, sinta-se à vontade para abrir uma issue ou enviar um pull request no [repositório do GitHub](https://github.com/seu-usuario/medical_image_converter).

## Licença

Este projeto é licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.
```
