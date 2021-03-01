Mimin buat presentasi tentang CTFR, tapi kok malah korup yaa setelah teman mimin pegang :(, Bisa bantu perbaiki gaaa.

Download : https://mega.nz/#!sgQnBSxS!8sYkJxDYA99Eaub5CxnWQdVuus0XILHyiysuFtPSff0

Tools
```
https://poppler.freedesktop.org/
http://blog.alivate.com.au/poppler-windows/
```

Command
```
./pdfimages -list Presentation1.pdf

page   num  type   width height color comp bpc  enc interp  object ID x-ppi y-ppi size ratio
--------------------------------------------------------------------------------------------
   1     0 image     100   510  rgb     3   8  jpeg   no         9  0    21  1254 6188B 4.0%

./pdfimages -j Presentation1.pdf .
Syntax Warning: May not be a PDF file (continuing anyway)
```

Hasilnya Corrupted JPEG Image, perbaiki headernya jadi 

```
dari
FF FF FF FF 00 10 FF FF FF FF FF 01
menjadi
FF D8 FF E0 00 10 4A 46 49 46 00 01
```

Hasilnya gambar jpeg terbalik, pake image editor atau online tools untuk nge-flip

```
https://pinetools.com/flip-image
```

Flag : 

```
CTFR{c0ngr4t5_t0_f1x_th15_p3d33f}
```