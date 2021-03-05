from PIL import Image
from pyzbar.pyzbar import decode

for i in range(168):
	string = decode(Image.open('Oleh-Oleh/{}.png'.format(i)))
	string = string[0].data
	print(string.decode(), end='')