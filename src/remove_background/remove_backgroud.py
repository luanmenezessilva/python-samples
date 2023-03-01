from rembg import remove
from PIL import Image

# input_path = 'diamante_branco.jpg'
input_path = 'C:\Rozac\Pessoal\Fontes\python-samples\src\diamante_branco.jpg'
output_path = 'C:\Rozac\Pessoal\Fontes\python-samples\src\diamante_branco2.jpg'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)