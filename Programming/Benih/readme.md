Mimin di berikan benih sama member nih, coba cari tau dari tersebut. Oiya jangan lupa nama benih nya "CTFR"

Download : https://mega.nz/#!AkByiJiA!HHYR3Zxrh52ueX0i4D2QyPIx4TX2mm1gSX6ztSMsnvY

Harus menggunakan Python 2 berdasarkan sumber 
https://stackoverflow.com/questions/38943038/difference-between-python-2-and-3-for-shuffle-with-a-given-seed

```
#!/home/kulikode/.pyenv/shims/python2

import random

encrypted = open("encrypt.txt", "r").read()

flag = ""
random.seed("CTFR")
for x in encrypted:
    flag += chr(ord(x) - random.randrange(0, 15))

print flag
```

Flag
```
CTFR{b3n1h_ul4r_p1t0n}
```