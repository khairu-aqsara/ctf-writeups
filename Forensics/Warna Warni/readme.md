Mimin diberi sebuah gambar Warna warni alias acak. Tapi mimin enggk paham maksud dari gambar ini, Dan juga mimin diberikan sebuah hint yang mengatakan "Maksimal 127", Coba para hacker bantu mimin translated kan :(

Download : https://mega.nz/#!woYXmSSJ!3Nb1tOTW1SLR6ImwNmquFwQiiiYCxyCrXc1as-BGgJo

Code
```
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
```

Flag
```
CTFR{r34d_r9b_1n_1m4g3_1s_aw3s0m3}
```