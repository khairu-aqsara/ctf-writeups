Bantu mimin perbaiki file korup dong, soalnya ada gambar privasi mimin

Download: https://mega.nz/#!U8AGnRYR!F_Q7Rr9SsFKzMR5S9acWje3S5F2VehheqlJA0-e3emo

Tools
```
https://en.wikipedia.org/wiki/List_of_file_signatures
https://en.wikipedia.org/wiki/Portable_Network_Graphics
Magic number	 : 89 50 4e 47 0d 0a 1a 0a
Hex Editor

```

Command
```
xxd -l 0x40 file_korup.png

00000000: 0000 0000 0000 0000 0000 000d 4948 4452  ............IHDR
00000010: 0000 011a 0000 0042 0802 0000 0007 7b8e  .......B......{.
00000020: c300 0000 0173 5247 4200 aece 1ce9 0000  .....sRGB.......
00000030: 0004 6741 4d41 0000 b18f 0bfc 6105 0000  ..gAMA......a...
```

```
xxd -l 0x40 fix_file_korup.png 

00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 011a 0000 0042 0802 0000 0007 7b8e  .......B......{.
00000020: c300 0000 0173 5247 4200 aece 1ce9 0000  .....sRGB.......
00000030: 0004 6741 4d41 0000 b18f 0bfc 6105 0000  ..gAMA......a...
```

Flag
```
CTFR{f1l3_c0rrupt_h4s_b33n_f1x3d}

