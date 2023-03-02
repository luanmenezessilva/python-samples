# Não funcionou

from rembg import remove
from PIL import Image

input_path = 'C:\\Rozac\\Pessoal\\Fontes\\python-samples\\src\\remove_background\\diamante_branco.jpg'
output_path = 'C:\\Rozac\\Pessoal\\Fontes\\python-samples\\src\\remove_background\\diamante_branco2.jpeg'


im = Image.open(input_path)
rgb_im = im.convert('RGB')
rgb_im.save(output_path)