Masih lanjut dengan file yang ada di First GDB, Coba cari di file tersebut instruksi yang menggunakan "pop", cukup salah satu saja. Untuk penjelasannya cek google karena mimin kurang bisa menjelaskan :D

Flag : CTFR{0x(Address tanpa 0 didepan 0x)}

```bash
gdb -q first_gdb
pd main

0x0000000000001189 <+0>:     endbr64 
0x000000000000118d <+4>:     push   rbp
0x000000000000118e <+5>:     mov    rbp,rsp
0x0000000000001191 <+8>:     lea    rdi,[rip+0xe71]        # 0x2009
0x0000000000001198 <+15>:    call   0x1090 <puts@plt>
0x000000000000119d <+20>:    lea    rdi,[rip+0xe7c]        # 0x2020
0x00000000000011a4 <+27>:    call   0x1090 <puts@plt>
0x00000000000011a9 <+32>:    mov    eax,0x0
0x00000000000011ae <+37>:    pop    rbp
0x00000000000011af <+38>:    ret
```

Flag
```
CTFR{0x11ae}
```