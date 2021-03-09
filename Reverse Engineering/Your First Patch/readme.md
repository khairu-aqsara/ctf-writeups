Belum pernah patching binary ? Nah kalo belum nih kalian coba-coba, Btw dengan adanya ilmu "Patch Binary" kalian bisa melakukan bypass terhadap lisensi key pada sebuah program berbayar. Oleh karena itu, dengan kalian menyelesaikan challenge ini diharapkan harus teliti dalam pembuatan program desktop / linux.

Download : https://mega.nz/#!JthEAQJQ!zTbpky7AX14eLGQVAwcAFCCNakHA_m0BEfZNsQDyWOU

Pseudo code
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  puts("-= Welcome to CTFR =-");
  puts(
    "=> Kalian harus mengubah variabel 'patch' menjadi true agar mendapatkan flag!.\n"
    "=======================================");
  if ( (unsigned __int8)CheckMe() )
  {
    Decrypt(buffer);
    printf("Yeyyy! Kalian berhasil mengubah variabel tersebut, Nih flagnya %s", buffer);
  }
  else
  {
    puts("Kalian belum mengubah patch nya :(..");
  }
  return 0;
}


__int64 CheckMe(void)
{
  return 0LL;
}
```

hanya perlu merubah `if ( (unsigned __int8)CheckMe() )` atau `je 0x10ad`  menjadi `jne 0x10ad`

```bash
0x0000000000001060 <+0>:     sub    rsp,0x8
0x0000000000001064 <+4>:     lea    rdi,[rip+0xf99]        # 0x2004
0x000000000000106b <+11>:    call   0x1030 <puts@plt>
0x0000000000001070 <+16>:    lea    rdi,[rip+0xfa9]        # 0x2020
0x0000000000001077 <+23>:    call   0x1030 <puts@plt>
0x000000000000107c <+28>:    call   0x1230 <_Z7CheckMev>
0x0000000000001081 <+33>:    test   al,al
0x0000000000001083 <+35>:    je     0x10ad <main+77>
0x0000000000001085 <+37>:    lea    rdi,[rip+0x3034]        # 0x40c0 <buffer>
0x000000000000108c <+44>:    call   0x11b0 <_Z7DecryptPc>
0x0000000000001091 <+49>:    lea    rsi,[rip+0x3028]        # 0x40c0 <buffer>
0x0000000000001098 <+56>:    lea    rdi,[rip+0xff9]        # 0x2098
0x000000000000109f <+63>:    xor    eax,eax
0x00000000000010a1 <+65>:    call   0x1040 <printf@plt>
0x00000000000010a6 <+70>:    xor    eax,eax
0x00000000000010a8 <+72>:    add    rsp,0x8
0x00000000000010ac <+76>:    ret    
0x00000000000010ad <+77>:    lea    rdi,[rip+0x102c]        # 0x20e0
0x00000000000010b4 <+84>:    call   0x1030 <puts@plt>
0x00000000000010b9 <+89>:    jmp    0x10a6 <main+70>
```

Caranya pake radare
```
cp patchbin test
r2 -w test // load dalam mode write
aaa
Vp
```

Cari fungsi main (scroll2 aja) sampe posisi write berada di baris `00001083 7428 je 0x10ad` tekan `A` dan ganti menjadi `jne 0x10ad` Enter, kalo ada konfirmasi mau disimpan tekan `Y` lalu jalankan `./test` hasilnya

```bash
-= Welcome to CTFR =-
=> Kalian harus mengubah variabel 'patch' menjadi true agar mendapatkan flag!.
=======================================
Yeyyy! Kalian berhasil mengubah variabel tersebut, Nih flagnya CTFR{15_th4t_345y_wh3n_y0u_0nly_n33d_t0_p4tch_1t}  
```

Flag

```
CTFR{15_th4t_345y_wh3n_y0u_0nly_n33d_t0_p4tch_1t}
```