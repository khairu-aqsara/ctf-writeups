from PIL import Image

img = Image.open('warnawarni.png')
pixel = img.load()

width,height = img.size

flag =''

for x in range(width):
	for y in range(height):
		c = pixel[x,y][0]
		if c <127:
			flag+=chr(c)

print(flag)
#CTFR{r34d_r9b_1n_1m4g3_1s_aw3s0m3}
