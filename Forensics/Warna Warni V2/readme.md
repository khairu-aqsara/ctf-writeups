Hayuuu lanjut ke Warna Warni versi 2. Kali ini mimin beri 1000 Points dehh yang bisa nyelesain :D. Good Luck and Have fun.

Download : https://mega.nz/#!h0I0TTYS!wCbP8hCdPeA900f8PeD-m7Nt0Tcu9rXOzQPouIgoZYg

cari semua nilai green yang di apit oleh nilai 127

```
from PIL import Image
from pwn import *


gbr = Image.open('warnawarni2.png')
pixel = gbr.load()

lebar,tinggi = gbr.size

flag  = []

for x in range(lebar):
	for y in range(tinggi):
		if pixel[x,y][0] == 127 and pixel[x,y][2] == 127:
			flag.append(pixel[x,y][1])
```

hasilnya hex ga jelas, setelah coba-coba ternyata program assembly

```
print(disasm("".join([chr(x) for x in flag]), arch="amd64"))

main:
  push   rbp
  mov    rbp, rsp
  mov    DWORD PTR [rbp-0x4], 0xc
  shl    DWORD PTR [rbp-0x4], 0xa
  sar    DWORD PTR [rbp-0x4], 0x5
  add    DWORD PTR [rbp-0x4], 0xa
  sub    DWORD PTR [rbp-0x4], 0xc2
  cmp    DWORD PTR [rbp-0x4], 0x190
  jg     0x2d
  add    DWORD PTR [rbp-0x4], 0x1
  jmp    0x1e
  sar    DWORD PTR [rbp-0x4], 0x2
  cmp    DWORD PTR [rbp-0x4], 0xff
  jg     0x40
  add    DWORD PTR [rbp-0x4], 0x1
  jmp    0x31
  cmp    DWORD PTR [rbp-0x4], 0x100
  jne    0xa3
  add    DWORD PTR [rbp-0x4], 0x1
  sub    DWORD PTR [rbp-0x4], 0x1
  add    DWORD PTR [rbp-0x4], 0x1
  sub    DWORD PTR [rbp-0x4], 0x1
  mov    eax, DWORD PTR [rbp-0x4]
  imul   eax, eax, 0x1a
  mov    DWORD PTR [rbp-0x4], eax
  mov    eax, DWORD PTR [rbp-0x4]
  imul   eax, eax, 0x368
  mov    DWORD PTR [rbp-0x4], eax
  mov    eax, DWORD PTR [rbp-0x4]
  imul   eax, eax, 0x9210a4
  mov    DWORD PTR [rbp-0x4], eax
  mov    eax, DWORD PTR [rbp-0x4]
  imul   eax, eax, 0x9210a4
  mov    DWORD PTR [rbp-0x4], eax
  mov    eax, DWORD PTR [rbp-0x4]
  imul   eax, eax, 0x9210a4
  mov    DWORD PTR [rbp-0x4], eax
  mov    eax, DWORD PTR [rbp-0x4]
  imul   eax, eax, 0x9210a4
  mov    DWORD PTR [rbp-0x4], eax
  mov    eax, DWORD PTR [rbp-0x4]
  jmp    0x11c
  add    DWORD PTR [rbp-0x4], 0x1
  mov    edx, DWORD PTR [rbp-0x4]
  mov    eax, edx
  shl    eax, 0x2
  add    eax, edx
  add    eax, eax
  mov    DWORD PTR [rbp-0x4], eax
  mov    eax, DWORD PTR [rbp-0x4]
  movsxd rdx, eax
  imul   rdx, rdx, 0x66666667
  shr    rdx, 0x20
  sar    edx, 0x2
  sar    eax, 0x1f
  mov    ecx, eax
  mov    eax, edx
  sub    eax, ecx
  mov    DWORD PTR [rbp-0x4], eax
  sar    DWORD PTR [rbp-0x4], 0xa
  mov    edx, DWORD PTR [rbp-0x4]
  movsxd rax, edx
  imul   rax, rax, 0x66666667
  shr    rax, 0x20
  sar    eax, 0x2
  mov    esi, edx
  sar    esi, 0x1f
  sub    eax, esi
  mov    ecx, eax
  mov    eax, ecx
  shl    eax, 0x2
  add    eax, ecx
  add    eax, eax
  sub    edx, eax
  mov    DWORD PTR [rbp-0x4], edx
  add    DWORD PTR [rbp-0x4], 0xa
  sub    DWORD PTR [rbp-0x4], 0xff
  mov    eax, DWORD PTR [rbp-0x4]
  imul   eax, eax, 0x64
  mov    DWORD PTR [rbp-0x4], eax
  mov    eax, DWORD PTR [rbp-0x4]
  pop    rbp
  ret

```

Tools
```
https://defuse.ca/online-x86-assembler.htm
```

Generate Key berdasarkan Kode Assembly
```
def generate_key():
	key = 0xc
	key = key << 0xa
	key = key >> 0x5
	key = key + 0xa
	key = key - 0xc2

	while key <= 0x190:
		key+=1

	key = key >> 0x2

	while key <= 0xff:
		key+=1

	if key == 0x100:
		key = key + 1
		key = key - 1
		key = key + 1
		key = key - 1
		key = key * 0x1a
		key = key * 0x368
		key = key * 0x9210a4 * 0x9210a4 * 0x9210a4 * 0x9210a4
		return key
	else:
		return

key = generate_key()
final_flag = ''

for c in enc:
	ff = c/key 
	final_flag+=chr(ff)

print(final_flag)
```

Flag : 
```
Mimin sengaja menambahkan beberapa kalimat disini agar mencegah Bruteforce :D. Btw here is your flag : CTFR{4553mbly_1n5truct10n_1n51d3_1m4g3_1f_y0u_r34d_it}. Maaf nihh challenge nya di remake tross :(
```
