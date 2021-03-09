Gigi mimin bolong :( tolong di tambal donggg.

Download : https://mega.nz/#!UkB1EYyS!B1FoFxo999-M5Db4_vjR44qiZrqH4vYZzW-7d1W9xJs

Run
```bash
./tambalaku
=- Welcome to CTFR -=
=> Gigi aku ada yang bolong :(, Tolong di tambalkan
=> By_RasyidMF
Tambal Aku : <key>
```

Butuh Parameter untuk running

```bash
./tambalaku AAAAAAAAA                                                                                                    
=- Welcome to CTFR -=
=> Gigi aku ada yang bolong :(, Tolong di tambalkan
=> By_RasyidMF
=> Password Pertama Cocok!
=> Yaah tambalnya gagal :(
```

setelah di cek, aplikasi melakukan req ke alamat web, dan banyak fungsi-fungsi lainya yang kurang jelas fungsinya, ada beberapa fungsi yang menarik

```bash
gdb-peda$ info functions
0x0000000000001000  _init
....
0x00000000000010f0  main
0x00000000000015c0  WriteCallback(void*, unsigned long, unsigned long, void*)
0x0000000000001600  SendKey(char*)
0x0000000000001680  Decrypt(char*, int)
0x00000000000016b0  GetDec(char*)
....
```

dilihar dari list fungsi `Decrypt(char*, int)` sepertinya menarik

```c
void Decrypt(char *param_1,int param_2)

{
  long lVar1;
  
  lVar1 = 0;
  do {
    param_1[lVar1] = (byte)((int)lVar1 % param_2) ^ flag[lVar1];
    lVar1 = lVar1 + 1;
  } while (lVar1 != 0x34);
  return;
}
```

jika di konversi ke python bentuk sederhanya seperti
```python
def Decrypr(string, key):
	flag = ''
	for i in range(len(string)):
		flag+=chr((x % i) ^ ord(param[x]))
	return 0
```
tidak ada yang direturn dari fungsi ini, kemudian string juga tidak diketahui, cari string dengan gdb

```bash
gdb-peda$ pd Decrypt
0x0000000000001680 <+0>:     xor    ecx,ecx
0x0000000000001682 <+2>:     lea    r8,[rip+0x2a17]        # 0x40a0 <flag>
0x0000000000001689 <+9>:     nop    DWORD PTR [rax+0x0]
0x0000000000001690 <+16>:    mov    eax,ecx
0x0000000000001692 <+18>:    cdq    
0x0000000000001693 <+19>:    idiv   esi
0x0000000000001695 <+21>:    xor    dl,BYTE PTR [r8+rcx*1]
0x0000000000001699 <+25>:    mov    BYTE PTR [rdi+rcx*1],dl
0x000000000000169c <+28>:    add    rcx,0x1
0x00000000000016a0 <+32>:    cmp    rcx,0x34
0x00000000000016a4 <+36>:    jne    0x1690 <_Z7DecryptPci+16>
0x00000000000016a6 <+38>:    ret  
```

ternyata ada variable global `lea  r8,[rip+0x2a17]  # 0x40a0 <flag>` ternyata parameter pertama dari fungsi `Decrypt` adalah flagnya.

```bash
gdb-peda$ pd main
0x00005555555550f0 <+0>:     push   r12
...
0x00005555555552ee <+510>:   lea    rcx,[rip+0x2e0b]        # 0x555555558100 <buffer>
0x00005555555552f5 <+517>:   lea    rdx,[rip+0x2da4]        # 0x5555555580a0 <flag>
...
```

variable `<flag>` ada didalam stack setelah perulangan yang panjang, jadi di breakpoint aja di akhir fungsi main, dan cek nilai dari `<flag>`

```bash
gdb-peda$ b *main+970
gdb-peda$ r
gdb-peda$ x/10gx 0x5555555580a0
0x5555555580a0 <flag>:  0x5833347f51445543      0x3c796c537f3e617c
0x5555555580b0 <flag+16>:       0x306a765f207f2163      0x3f69567d377f5a6a
0x5555555580c0 <flag+32>:       0x4c7972247d6d5262      0x733266356f727134
0x5555555580d0 <flag+48>:       0x0000000076643939      0x0000000000000000
0x5555555580e0 <completed.0>:   0x0000000000000000      0x0000000000000000
gdb-peda$ p (int) flag
$2 = 0x51445543

```

`0x51445543` dalam hexa `43 = C, 55= U` dan seterusnya, karena dalam bentuk little endian penulisanya jadi terbalik, kalo dalam bentuk normal `0x43554451` sama dengan `CUDQ` kemungkinan besar ini bentuk enkripsi dari flagnya. Ambil semua string flag dan masukan dalam fungsi Decrypt

```bash
gdb-peda$ x/s 0x5555555580a0
0x5555555580a0 <flag>:  "CUDQ\177\064\063X|a>\177Sly<c!\177 _vj0jZ\177\067}Vi?bRm}$ryL4qro5f2s99dv"
```  

jika dmasukan dalam fungsi Decrypt

```python
def Decrypt():
	enc_flag = 'CUDQ\177\064\063X|a>\177Sly<c!\177 _vj0jZ\177\067}Vi?bRm}$ryL4qro5f2s99dv'
	for i in range(1,35):
	    flag = ''
	    for x in range(len(param)):
	        flag+=chr((x % i) ^ ord(param[x]))
	    print(f)
```

Flag

```
CTFR{15_th4t_aw3s0m3_wh3n_y0u_c4n_cr4ck_4ppl1c4t10n}
```