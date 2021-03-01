Mimin sebelumnya ada transaksi dengan orang lain, cuman mimin lupa alamatnya. Bisa kah carikan alamat yang mimin barusan transfer ? Oiya mimin ada note di buku juga "Thanks for selling 8 pcs of Program mate".

```
Hint : Jangan lupa tambahkan 0x
Alamat Mimin : N2786079738K6K44k3K0383i2500N062N90Jm089 Flag : 
```

Code
```
c = "N2786079738K6K44k3K0383i2500N062N90Jm089"
p = c
for x in c:
    if not x.isnumeric():
        shift = ord(x) ^ 8
        p = p.replace(x, chr(shift))
print(p.lower())
```


Flag:
```
CTFR{0xd8d1d7b55ec9bb115eb863ca01988829eef9cd9a}
```