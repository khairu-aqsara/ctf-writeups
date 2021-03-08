Tadi sudah belajar kalkulasi yaa ? Sekarang Byte dehh

Download : https://mega.nz/#!R5gGxBDK!sK2xnzl6xGoWXxfDrRlGyIvD1pJeNQg-_SGpGk06Et0

kalo dilihat dari kodenya, semua bagian angka sebelah kanan itu ascii code, dengan beberapa kondisi, misalnya

```asm
cmp     al, 83
...
...
...
cmp     al, 101
...
...
...
cmp     al, 87
...
...
...
```

kemungkinan misalnya kondisi `byte ke [rbp-110] != 83` prosesnya berhenti 

```asm
movzx   eax, BYTE PTR [rbp-110]
cmp     al, 83
jne     .L2
mov     eax, 0
jmp     .L3
```

Dalam C bisa jadi kodenya jadi
```C
if(al != 83){
	return 0;
}
```

karena `.L3` hanya berisi

```asm
pop     rbp
ret
```

jika semua kondisi `else` dibuang jadinya

```python

f = [67,84,70,82,123,109,52,53,116,51,114,95,97,53,53,51,109,98,108,121,125]
for x in f:
  print(chr(x), end='')
```

Flag
```
CTFR{m45t3r_a553mbly}
```

