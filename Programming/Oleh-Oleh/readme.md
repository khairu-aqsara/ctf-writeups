Mimin di beri oleh-oleh sama member nih, coba dicek.

Download : https://mega.nz/#!p8oHGQJS!epDcfet5nYurpY7EEigIR3Vlj-9zeRUHgNXLHUVnNSk

```
from PIL import Image
from pyzbar.pyzbar import decode

for i in range(168):
	string = decode(Image.open('Oleh-Oleh/{}.png'.format(i)))
	string = string[0].data
	print(string.decode(), end='')
```

Flag 

```
CTFR{0l3h_0l3h_k0k_q133r_c0d3}
```