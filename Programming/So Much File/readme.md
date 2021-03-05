File yang ada pada berangkas .zip ini sangat banyak sekali! Bantu mimin dapatkan arti dari file yang sangat banyak ini!!

Download : https://mega.nz/#!goQliKLa!VfwsnHSFyEW7C6SHcpUbHAG3BbL-EZAyImKW3RoFUc0

Hint:
Setiap satu file isinya 1 Karakter (size 1Kb) jadi tinggal di sort aja by size, delete smua zero Bytes and sort by file name, atau bisa pake perintah grep dikombinasikan dengan perintah bash untuk nyari karakternya

```
unzip Searchme.zip
cd Searchme
for i in $(ls -1 | sort -V); do grep '[0-9a-zA-Z_\{\}]' $i; done | tr -d '\n'
```

Flag
```
CTFR{pyth0n_5cr1pt_m4k3_you_34sy_t0_s0lv3_1t}
```