Ada sebuah code berbahasa Python dan disana memiliki teks yang sangat rahasia, akan tetapi kami tidak dapat membaca teks tersebut. Apakah kalian bisa bantu kami untuk mengdecode hasil enkripsi tersebut ?

Source

```
flag = ">OAMva,mnoZo,h.Z.i^mtkoZ,iZktoc+i:x"
encrypted = ""
for x in flag:
    encrypted += chr(ord(x) - 0x0000000005 % 0xFFFFFFFFFFF)

print encrypted
```

`n(x) % 0xFFFFFFFFFFF` hasilnya akan akan sama dengan nilai n(x)

Solve

```
flag = ">OAMva,mnoZo,h.Z.i^mtkoZ,iZktoc+i:x"
encrypted = ""
for x in flag:
    encrypted += chr(ord(x) + 0x0000000005)

print encrypted
```

Flag
```
CTFR{f1rst_t1m3_3ncrypt_1n_pyth0n?}
```