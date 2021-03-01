Mimin berikan kalian sebuah gambar dengan chunk yang korup, bisakah kalian perbaiki :D

Download : https://mega.nz/#!lhx2lKbD!3ROFQcgvp5_nDyUfXPBLmyq84jwH8xM1ZcDT8WezEdk

```
pngcheck -v chunk.png
File: chunk.png (2943 bytes)
  invalid chunk name "" (00 00 00 00)
ERRORS DETECTED in chunk.png
```

dengan hexeditor bukan file png lain, dan bandingkan sekitar 120byte pertama

perbedaanya ada di
```
00000030: 0004 4241 4d41 0000 b18f 0bfc 6105 0000  ..BAMA......a...
```

seharusnya

```
00000030: 0004 6741 4d41 0000 b18f 0bfc 6105 0000  ..gAMA......a...
```

Flag:

```
CTFR{c0ngr4t5_f0r_f1x1n9_c0rrupt_1nv4l1d_chunk}
```