Sofa adalah tempat duduk yang nyaman, Semakin empuk semakin nyaman h3h3
Hint : Cari arti dari S0F0, Kemudian ambil 16 Byte / 32 Bit. Pastikan, Jangan ambil Size dari offset tersebut. Hasil tadi, kalkukasi dengan XOR yang sudah di berikan. Good Luck and Enjoy :D

Flag Enc:
```
435446527b7830725f773174685f7330665f63346462f56e3477324e73324e6633216582
```

Download : https://mega.nz/#!w8Yz2YgY!GE2tgYFnNqDs64XfPPqJoFi-fQjS9Q3z464H2Yn2Mdo

Cari Nilai Sofo dari Gambar pake JPEGSnoop

```
*** Marker: SOF0 (Baseline DCT) (xFFC0) ***
  OFFSET: 0x0000009A
  Frame header length = 17
  Precision = 8
  Number of Lines = 384
  Samples per Line = 512
  Image Size = 512 x 384
  Raw Image Orientation = Landscape
  Number of Img components = 3
    Component[1]: ID=0x01, Samp Fac=0x11 (Subsamp 1 x 1), Quant Tbl Sel=0x00 (Lum: Y)
    Component[2]: ID=0x02, Samp Fac=0x11 (Subsamp 1 x 1), Quant Tbl Sel=0x01 (Chrom: Cb)
    Component[3]: ID=0x03, Samp Fac=0x11 (Subsamp 1 x 1), Quant Tbl Sel=0x01 (Chrom: Cr)
```

Command
```
0x0000009A - 0x4 = 0x0000009E Karena 4 Byte pertama merupakan S0F0 Signature

xxd -s +0x0000009E -l 16 sofa.jpg
0000009e: 0801 8002 0003 0111 0002 1101 0311 01ff  ................
```

Tools
```
http://xor.pw/
```

Flag:
```
SOFO = 0801 8002 0003 0111 0002 1101 0311 01ff
CTFR{x0r_w1th_s0f_c4lcul4t3_s0_g00d}
```