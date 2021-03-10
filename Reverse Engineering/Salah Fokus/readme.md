Sedikit Basic Encryption dengan function abal-abalan

Download : https://mega.nz/#!ks4BzA5b!ieG-RccWFiTuGVXd8B1qICt2YzYabetW0DUHYaiYSps

setelah di decompiler dengan ghidra, ternyata banyak banget fungsi yang di obuscated, tetapi ada beberapa fungsi yang tidak di obuscated, misalnya seperti

```bash
gdb-peda$ pd main
Dump of assembler code for function main:
   0x0000000000001f27 <+0>:     endbr64 
   0x0000000000001f2b <+4>:     push   rbp
   0x0000000000001f2c <+5>:     mov    rbp,rsp
   0x0000000000001f2f <+8>:     lea    rdi,[rip+0x1595]        # 0x34cb
   0x0000000000001f36 <+15>:    call   0x1070 <puts@plt>
   0x0000000000001f3b <+20>:    lea    rdi,[rip+0x15a4]        # 0x34e6
   0x0000000000001f42 <+27>:    call   0x1189 <encrypt>
   0x0000000000001f47 <+32>:    mov    eax,0x0
   0x0000000000001f4c <+37>:    pop    rbp
   0x0000000000001f4d <+38>:    ret    
End of assembler dump.
gdb-peda$ 
gdb-peda$ pd encrypt
Dump of assembler code for function encrypt:
   0x0000000000001189 <+0>:     endbr64 
   0x000000000000118d <+4>:     push   rbp
   0x000000000000118e <+5>:     mov    rbp,rsp
   0x0000000000001191 <+8>:     push   rbx
   0x0000000000001192 <+9>:     sub    rsp,0x28
   0x0000000000001196 <+13>:    mov    QWORD PTR [rbp-0x28],rdi
   0x000000000000119a <+17>:    mov    DWORD PTR [rbp-0x14],0x0
   0x00000000000011a1 <+24>:    jmp    0x1312 <encrypt+393>
   0x00000000000011a6 <+29>:    mov    eax,DWORD PTR [rbp-0x14]
   0x00000000000011a9 <+32>:    movsxd rdx,eax
   0x00000000000011ac <+35>:    mov    rax,QWORD PTR [rbp-0x28]
   0x00000000000011b0 <+39>:    add    rax,rdx
   0x00000000000011b3 <+42>:    movzx  eax,BYTE PTR [rax]
   0x00000000000011b6 <+45>:    cmp    al,0x40
   0x00000000000011b8 <+47>:    jle    0x1210 <encrypt+135>
   0x00000000000011ba <+49>:    mov    eax,DWORD PTR [rbp-0x14]
   0x00000000000011bd <+52>:    movsxd rdx,eax
   0x00000000000011c0 <+55>:    mov    rax,QWORD PTR [rbp-0x28]
   0x00000000000011c4 <+59>:    add    rax,rdx
   0x00000000000011c7 <+62>:    movzx  eax,BYTE PTR [rax]
   0x00000000000011ca <+65>:    cmp    al,0x5a
   0x00000000000011cc <+67>:    jg     0x1210 <encrypt+135>
   0x00000000000011ce <+69>:    mov    eax,DWORD PTR [rbp-0x14]
   0x00000000000011d1 <+72>:    movsxd rdx,eax
   0x00000000000011d4 <+75>:    mov    rax,QWORD PTR [rbp-0x28]
   0x00000000000011d8 <+79>:    add    rax,rdx
   0x00000000000011db <+82>:    movzx  eax,BYTE PTR [rax]
   0x00000000000011de <+85>:    movsx  eax,al
   0x00000000000011e1 <+88>:    lea    ecx,[rax+0x1]
   0x00000000000011e4 <+91>:    mov    eax,DWORD PTR [rbp-0x14]
   0x00000000000011e7 <+94>:    cdq    
   0x00000000000011e8 <+95>:    shr    edx,0x1b
   0x00000000000011eb <+98>:    add    eax,edx
   0x00000000000011ed <+100>:   and    eax,0x1f
   0x00000000000011f0 <+103>:   sub    eax,edx
   0x00000000000011f2 <+105>:   sub    ecx,eax
   0x00000000000011f4 <+107>:   mov    eax,DWORD PTR [rbp-0x14]
   0x00000000000011f7 <+110>:   cdqe   
   0x00000000000011f9 <+112>:   lea    rdx,[rax*4+0x0]
   0x0000000000001201 <+120>:   lea    rax,[rip+0x4e38]        # 0x6040 <ec>
   0x0000000000001208 <+127>:   mov    DWORD PTR [rdx+rax*1],ecx
   0x000000000000120b <+130>:   jmp    0x130e <encrypt+389>
   0x0000000000001210 <+135>:   mov    eax,DWORD PTR [rbp-0x14]
   0x0000000000001213 <+138>:   movsxd rdx,eax
   0x0000000000001216 <+141>:   mov    rax,QWORD PTR [rbp-0x28]
   0x000000000000121a <+145>:   add    rax,rdx
   0x000000000000121d <+148>:   movzx  eax,BYTE PTR [rax]
   0x0000000000001220 <+151>:   cmp    al,0x60
   0x0000000000001222 <+153>:   jle    0x127a <encrypt+241>
   0x0000000000001224 <+155>:   mov    eax,DWORD PTR [rbp-0x14]
   0x0000000000001227 <+158>:   movsxd rdx,eax
   0x000000000000122a <+161>:   mov    rax,QWORD PTR [rbp-0x28]
   0x000000000000122e <+165>:   add    rax,rdx
   0x0000000000001231 <+168>:   movzx  eax,BYTE PTR [rax]
   0x0000000000001234 <+171>:   cmp    al,0x7a
   0x0000000000001236 <+173>:   jg     0x127a <encrypt+241>
   0x0000000000001238 <+175>:   mov    eax,DWORD PTR [rbp-0x14]
   0x000000000000123b <+178>:   movsxd rdx,eax
   0x000000000000123e <+181>:   mov    rax,QWORD PTR [rbp-0x28]
   0x0000000000001242 <+185>:   add    rax,rdx
   0x0000000000001245 <+188>:   movzx  eax,BYTE PTR [rax]
   0x0000000000001248 <+191>:   movsx  eax,al
   0x000000000000124b <+194>:   lea    ecx,[rax+0x1]
   0x000000000000124e <+197>:   mov    eax,DWORD PTR [rbp-0x14]
   0x0000000000001251 <+200>:   cdq    
   0x0000000000001252 <+201>:   shr    edx,0x1c
   0x0000000000001255 <+204>:   add    eax,edx
   0x0000000000001257 <+206>:   and    eax,0xf
   0x000000000000125a <+209>:   sub    eax,edx
   0x000000000000125c <+211>:   add    ecx,eax
   0x000000000000125e <+213>:   mov    eax,DWORD PTR [rbp-0x14]
   0x0000000000001261 <+216>:   cdqe   
   0x0000000000001263 <+218>:   lea    rdx,[rax*4+0x0]
   0x000000000000126b <+226>:   lea    rax,[rip+0x4dce]        # 0x6040 <ec>
   0x0000000000001272 <+233>:   mov    DWORD PTR [rdx+rax*1],ecx
   0x0000000000001275 <+236>:   jmp    0x130e <encrypt+389>
   0x000000000000127a <+241>:   mov    eax,DWORD PTR [rbp-0x14]
   0x000000000000127d <+244>:   movsxd rdx,eax
   0x0000000000001280 <+247>:   mov    rax,QWORD PTR [rbp-0x28]
   0x0000000000001284 <+251>:   add    rax,rdx
   0x0000000000001287 <+254>:   movzx  eax,BYTE PTR [rax]
   0x000000000000128a <+257>:   cmp    al,0x2f
   0x000000000000128c <+259>:   jle    0x12e1 <encrypt+344>
   0x000000000000128e <+261>:   mov    eax,DWORD PTR [rbp-0x14]
   0x0000000000001291 <+264>:   movsxd rdx,eax
   0x0000000000001294 <+267>:   mov    rax,QWORD PTR [rbp-0x28]
   0x0000000000001298 <+271>:   add    rax,rdx
   0x000000000000129b <+274>:   movzx  eax,BYTE PTR [rax]
   0x000000000000129e <+277>:   cmp    al,0x39
   0x00000000000012a0 <+279>:   jg     0x12e1 <encrypt+344>
   0x00000000000012a2 <+281>:   mov    eax,DWORD PTR [rbp-0x14]
   0x00000000000012a5 <+284>:   movsxd rdx,eax
   0x00000000000012a8 <+287>:   mov    rax,QWORD PTR [rbp-0x28]
   0x00000000000012ac <+291>:   add    rax,rdx
   0x00000000000012af <+294>:   movzx  eax,BYTE PTR [rax]
   0x00000000000012b2 <+297>:   movsx  eax,al
   0x00000000000012b5 <+300>:   lea    ecx,[rax+0x1]
   0x00000000000012b8 <+303>:   mov    eax,DWORD PTR [rbp-0x14]
   0x00000000000012bb <+306>:   cdq    
   0x00000000000012bc <+307>:   shr    edx,0x1d
   0x00000000000012bf <+310>:   add    eax,edx
   0x00000000000012c1 <+312>:   and    eax,0x7
   0x00000000000012c4 <+315>:   sub    eax,edx
   0x00000000000012c6 <+317>:   sub    ecx,eax
   0x00000000000012c8 <+319>:   mov    eax,DWORD PTR [rbp-0x14]
   0x00000000000012cb <+322>:   cdqe   
   0x00000000000012cd <+324>:   lea    rdx,[rax*4+0x0]
   0x00000000000012d5 <+332>:   lea    rax,[rip+0x4d64]        # 0x6040 <ec>
   0x00000000000012dc <+339>:   mov    DWORD PTR [rdx+rax*1],ecx
   0x00000000000012df <+342>:   jmp    0x130e <encrypt+389>
   0x00000000000012e1 <+344>:   mov    eax,DWORD PTR [rbp-0x14]
   0x00000000000012e4 <+347>:   movsxd rdx,eax
   0x00000000000012e7 <+350>:   mov    rax,QWORD PTR [rbp-0x28]
   0x00000000000012eb <+354>:   add    rax,rdx
   0x00000000000012ee <+357>:   movzx  eax,BYTE PTR [rax]
   0x00000000000012f1 <+360>:   movsx  eax,al
   0x00000000000012f4 <+363>:   lea    ecx,[rax-0xf]
   0x00000000000012f7 <+366>:   mov    eax,DWORD PTR [rbp-0x14]
   0x00000000000012fa <+369>:   cdqe   
   0x00000000000012fc <+371>:   lea    rdx,[rax*4+0x0]
   0x0000000000001304 <+379>:   lea    rax,[rip+0x4d35]        # 0x6040 <ec>
   0x000000000000130b <+386>:   mov    DWORD PTR [rdx+rax*1],ecx
   0x000000000000130e <+389>:   add    DWORD PTR [rbp-0x14],0x1
   0x0000000000001312 <+393>:   mov    eax,DWORD PTR [rbp-0x14]
   0x0000000000001315 <+396>:   movsxd rbx,eax
   0x0000000000001318 <+399>:   mov    rax,QWORD PTR [rbp-0x28]
   0x000000000000131c <+403>:   mov    rdi,rax
   0x000000000000131f <+406>:   call   0x1080 <strlen@plt>
   0x0000000000001324 <+411>:   cmp    rbx,rax
   0x0000000000001327 <+414>:   jb     0x11a6 <encrypt+29>
   0x000000000000132d <+420>:   nop
   0x000000000000132e <+421>:   nop
   0x000000000000132f <+422>:   add    rsp,0x28
   0x0000000000001333 <+426>:   pop    rbx
   0x0000000000001334 <+427>:   pop    rbp
   0x0000000000001335 <+428>:   ret    
End of assembler dump.
```

Kalo di terjemahin dalam Bahasa C dengan tools Ghidra hasilnya

```c
undefined8 main(undefined8 param_1,int param_2)

{
  puts("Im not looking to anywhere");
  encrypt("Im not looking to anywhere\n",param_2);
  return 0;
}

void encrypt(char *__block,int __edflag)

{
  size_t sVar1;
  uint uVar2;
  int local_1c;
  
  local_1c = 0;
  while( true ) {
    sVar1 = strlen(__block);
    if (sVar1 <= (ulong)(long)local_1c) break;
    uVar2 = local_1c >> 0x1f;
    if ((__block[local_1c] < 'A') || ('Z' < __block[local_1c])) {
      if ((__block[local_1c] < 'a') || ('z' < __block[local_1c])) {
        if ((__block[local_1c] < '0') || ('9' < __block[local_1c])) {
          *(int *)(ec + (long)local_1c * 4) = __block[local_1c] + -0xf;
        }
        else {
          *(uint *)(ec + (long)local_1c * 4) =
               (__block[local_1c] + 1) - ((local_1c + (uVar2 >> 0x1d) & 7) - (uVar2 >> 0x1d));
        }
      }
      else {
        *(uint *)(ec + (long)local_1c * 4) =
             __block[local_1c] + 1 + ((local_1c + (uVar2 >> 0x1c) & 0xf) - (uVar2 >> 0x1c));
      }
    }
    else {
      *(uint *)(ec + (long)local_1c * 4) =
           (__block[local_1c] + 1) - ((local_1c + (uVar2 >> 0x1b) & 0x1f) - (uVar2 >> 0x1b));
    }
    local_1c = local_1c + 1;
  }
  return;
}
```

kalo dilihat-lihat, fungsi `main()` hanya memanggil fungsi `encrypt()`, dalam file binary juga tidak ditemukan fungsi-fungsi yang berkaitan dengan `decryptnya` nya kalo di sederhankan fungsi encryptnya kedalam versi `python`

```python
def encrypt(flag):
    panjang_flag = len(flag)
    i = 0
    enc_flag = []
    
    while(panjang_flag > i):
        shift_var = i >> 0x1f
        ord_flag = ord(flag[i])
        if ord_flag < ord('A') or ord('Z') < ord_flag:
            if ord_flag < ord('a') or ord('z') < ord_flag:
                if ord_flag < ord('0') or ord('9') < ord_flag:
                    cc = ord_flag - 0xf
                    enc_flag.append(cc)
                else:
                    cc = (ord_flag + 1) - ((i + (shift_var >> 0x1d) & 7) - (shift_var >> 0x1d))
                    enc_flag.append(cc)
            else:
                cc = ord_flag + 1 + ((i + (shift_var >> 0x1c) & 0xf) - (shift_var >> 0x1c))
                enc_flag.append(cc)
        else:
            cc = (ord_flag + 1) - ((i + (shift_var >> 0x1b) & 0x1f) - (shift_var >> 0x1b))
            enc_flag.append(cc)
        i+=1
    return enc_flag
```

jika dijalankan 
```python
test = encrypt('Im not looking to anywhere')
print(''.join([chr(x) for x in test]))
```
Hasilnya adalah

```
Jortztxyvu{updr~}om{o
```

sejauh ini sih kebutuhan dasar sudah ada, tinggal nyari dimana flag sebenarnya, setelah di cari-cari kemungkinan flag sebenarnya ada di fungsi `undefined8 gqIBObWeQSulobiTtXtNJbboY(undefined8 param_1,int param_2)` karena pada fungsi ini ada beberapa inisialisasi karakter dalam bentuk hexadecimal yang tidak ditemukan di fungsi yang lainnya.

```asm
gdb-peda$ pd gqIBObWeQSulobiTtXtNJbboY
Dump of assembler code for function gqIBObWeQSulobiTtXtNJbboY:
   0x00000000000016cc <+0>:     endbr64 
   0x00000000000016d0 <+4>:     push   rbp
   0x00000000000016d1 <+5>:     mov    rbp,rsp
   0x00000000000016d4 <+8>:     sub    rsp,0xe0
   0x00000000000016db <+15>:    mov    rax,QWORD PTR fs:0x28
   0x00000000000016e4 <+24>:    mov    QWORD PTR [rbp-0x8],rax
   0x00000000000016e8 <+28>:    xor    eax,eax
   0x00000000000016ea <+30>:    mov    DWORD PTR [rbp-0xe0],0x44
   0x00000000000016f4 <+40>:    mov    DWORD PTR [rbp-0xdc],0x54
   0x00000000000016fe <+50>:    mov    DWORD PTR [rbp-0xd8],0x45
   0x0000000000001708 <+60>:    mov    DWORD PTR [rbp-0xd4],0x50
   0x0000000000001712 <+70>:    mov    DWORD PTR [rbp-0xd0],0x6c
   0x000000000000171c <+80>:    mov    DWORD PTR [rbp-0xcc],0x79
   0x0000000000001726 <+90>:    mov    DWORD PTR [rbp-0xc8],0x7b
   0x0000000000001730 <+100>:   mov    DWORD PTR [rbp-0xc4],0x2a
   0x000000000000173a <+110>:   mov    DWORD PTR [rbp-0xc0],0x79
   0x0000000000001744 <+120>:   mov    DWORD PTR [rbp-0xbc],0x50
   0x000000000000174e <+130>:   mov    DWORD PTR [rbp-0xb8],0x77
   0x0000000000001758 <+140>:   mov    DWORD PTR [rbp-0xb4],0x2e
   0x0000000000001762 <+150>:   mov    DWORD PTR [rbp-0xb0],0x2d
   0x000000000000176c <+160>:   mov    DWORD PTR [rbp-0xac],0x79
   0x0000000000001776 <+170>:   mov    DWORD PTR [rbp-0xa8],0x2c
   0x0000000000001780 <+180>:   mov    DWORD PTR [rbp-0xa4],0x7e
   0x000000000000178a <+190>:   mov    DWORD PTR [rbp-0xa0],0x3a
   0x0000000000001794 <+200>:   mov    DWORD PTR [rbp-0x9c],0x50
   0x000000000000179e <+210>:   mov    DWORD PTR [rbp-0x98],0x33
   0x00000000000017a8 <+220>:   mov    DWORD PTR [rbp-0x94],0x78
   0x00000000000017b2 <+230>:   mov    DWORD PTR [rbp-0x90],0x50
   0x00000000000017bc <+240>:   mov    DWORD PTR [rbp-0x8c],0x76
   0x00000000000017c6 <+250>:   mov    DWORD PTR [rbp-0x88],0x30
   0x00000000000017d0 <+260>:   mov    DWORD PTR [rbp-0x84],0x2d
   0x00000000000017da <+270>:   mov    DWORD PTR [rbp-0x80],0x7e
   0x00000000000017e1 <+277>:   mov    DWORD PTR [rbp-0x7c],0x6e
   0x00000000000017e8 <+284>:   mov    DWORD PTR [rbp-0x78],0x2f
   0x00000000000017ef <+291>:   mov    DWORD PTR [rbp-0x74],0x6f
   0x00000000000017f6 <+298>:   mov    DWORD PTR [rbp-0x70],0x2d
   0x00000000000017fd <+305>:   mov    DWORD PTR [rbp-0x6c],0x72
   0x0000000000001804 <+312>:   mov    DWORD PTR [rbp-0x68],0x2e
   0x000000000000180b <+319>:   mov    DWORD PTR [rbp-0x64],0x50
   0x0000000000001812 <+326>:   mov    DWORD PTR [rbp-0x60],0x6f
   0x0000000000001819 <+333>:   mov    DWORD PTR [rbp-0x5c],0x30
   0x0000000000001820 <+340>:   mov    DWORD PTR [rbp-0x58],0x7a
   0x0000000000001827 <+347>:   mov    DWORD PTR [rbp-0x54],0x50
   0x000000000000182e <+354>:   mov    DWORD PTR [rbp-0x50],0x6b
   0x0000000000001835 <+361>:   mov    DWORD PTR [rbp-0x4c],0x2c
   0x000000000000183c <+368>:   mov    DWORD PTR [rbp-0x48],0x6a
   0x0000000000001843 <+375>:   mov    DWORD PTR [rbp-0x44],0x7d
   0x000000000000184a <+382>:   mov    DWORD PTR [rbp-0x40],0x36
   0x0000000000001851 <+389>:   mov    DWORD PTR [rbp-0x3c],0x50
   0x0000000000001858 <+396>:   mov    DWORD PTR [rbp-0x38],0x33
   0x000000000000185f <+403>:   mov    DWORD PTR [rbp-0x34],0x80
   0x0000000000001866 <+410>:   mov    DWORD PTR [rbp-0x30],0x50
   0x000000000000186d <+417>:   mov    DWORD PTR [rbp-0x2c],0x30
   0x0000000000001874 <+424>:   mov    DWORD PTR [rbp-0x28],0x30
   0x000000000000187b <+431>:   mov    DWORD PTR [rbp-0x24],0x2f
   0x0000000000001882 <+438>:   mov    DWORD PTR [rbp-0x20],0x34
   0x0000000000001889 <+445>:   mov    DWORD PTR [rbp-0x1c],0x6f
   0x0000000000001890 <+452>:   mov    DWORD PTR [rbp-0x18],0x65
   0x0000000000001897 <+459>:   mov    DWORD PTR [rbp-0x14],0x70
   0x000000000000189e <+466>:   mov    DWORD PTR [rbp-0x10],0x7e
   0x00000000000018a5 <+473>:   mov    DWORD PTR [rbp-0xc],0x6e
   0x00000000000018ac <+480>:   lea    rdi,[rip+0xec5]        # 0x2778
   0x00000000000018b3 <+487>:   call   0x1189 <encrypt>
   0x00000000000018b8 <+492>:   mov    eax,0x0
   0x00000000000018bd <+497>:   mov    rdx,QWORD PTR [rbp-0x8]
   0x00000000000018c1 <+501>:   xor    rdx,QWORD PTR fs:0x28
   0x00000000000018ca <+510>:   je     0x18d1 <gqIBObWeQSulobiTtXtNJbboY+517>
   0x00000000000018cc <+512>:   call   0x1090 <__stack_chk_fail@plt>
   0x00000000000018d1 <+517>:   leave  
   0x00000000000018d2 <+518>:   ret    
End of assembler dump.
```

kalo di coba jalanin dan ngasi breakpoint di beberapa bagian

```bash
gdb-peda$ b *main
Breakpoint 1 at 0x1f27
gdb-peda$ b *gqIBObWeQSulobiTtXtNJbboY+480
Breakpoint 2 at 0x18ac
gdb-peda$ r
gdb-peda$ jump *gqIBObWeQSulobiTtXtNJbboY
```
dan memerphatikan stack pada fungsi `gqIBObWeQSulobiTtXtNJbboY()` 

```bash
0000| 0x7fffffffdee0 --> 0x5400000044 ('D')
0008| 0x7fffffffdee8 --> 0x5000000045 ('E')
0016| 0x7fffffffdef0 --> 0x790000006c ('l')
0024| 0x7fffffffdef8 --> 0x2a0000007b ('{')
0032| 0x7fffffffdf00 --> 0x5000000079 ('y')
0040| 0x7fffffffdf08 --> 0x2e00000077 ('w')
0048| 0x7fffffffdf10 --> 0x790000002d ('-')
0056| 0x7fffffffdf18 --> 0x7e0000002c (',')
```

jadi bisa dipastikan flag yang asli ada dalam fungsi ini dalam bentuk ter-enkrip, jika kita keluarkan semua stringnya, karena panjang ruang untuk realflag ini `sub    rsp,0xe0` = `212` dalam decimal, jadi coba aja keluarin semua value dalam memory dari rentang `0x7fffffffdee0` s/d `0x7fffffffdee0 + 0xe0` 

```bash
gdb-peda$ x/212s $rsp
0x7fffffffdee0: "D"
0x7fffffffdee2: ""
0x7fffffffdee3: ""
0x7fffffffdee4: "T"
0x7fffffffdee6: ""
0x7fffffffdee7: ""
0x7fffffffdee8: "E"
0x7fffffffdeea: ""
0x7fffffffdeeb: ""
0x7fffffffdeec: "P"
0x7fffffffdeee: ""
0x7fffffffdeef: ""
0x7fffffffdef0: "l"
....
....
0x7fffffffdfb3: ""
0x7fffffffdfb4: "n"
```

atau sama dengan

```
DTEPly{*yPw.-y,~:P3xPv0-~n/o-r.Po0zPk,j}6P300/4oep~n
```


karena realflag kemungkinan sudah ketemu, dan tidak ditemukan juga fungsi untuk decrypt, jadinya di brute aja, berhubung karena fungsi `encrypt()` sudah ada.

```python
import sys
import time

c = [0x44,0x54,0x45,0x50,0x6c,0x79,0x7b,0x2a,0x79,0x50,0x77,0x2e,0x2d,0x79,0x2c,0x7e,0x3a,0x50,0x33,0x78,0x50,0x76,0x30,0x2d,0x7e,0x6e,0x2f,0x6f,0x2d,0x72,0x2e,0x50,0x6f,0x30,0x7a,0x50,0x6b,0x2c,0x6a,0x7d,0x36,0x50,0x33,0x80,0x50,0x30,0x30,0x2f,0x34,0x6f,0x65,0x70,0x7e,0x6e]

enc_flag = ''.join([chr(x) for x in c])

def enc(flag):
    panjang_flag = len(flag)
    i = 0
    enc_flag = []
    
    while(panjang_flag > i):
        shift_var = i >> 0x1f
        ord_flag = ord(flag[i])
        if ord_flag < ord('A') or ord('Z') < ord_flag:
            if ord_flag < ord('a') or ord('z') < ord_flag:
                if ord_flag < ord('0') or ord('9') < ord_flag:
                    cc = ord_flag - 0xf
                    enc_flag.append(cc)
                else:
                    cc = (ord_flag + 1) - ((i + (shift_var >> 0x1d) & 7) - (shift_var >> 0x1d))
                    enc_flag.append(cc)
            else:
                cc = ord_flag + 1 + ((i + (shift_var >> 0x1c) & 0xf) - (shift_var >> 0x1c))
                enc_flag.append(cc)
        else:
            cc = (ord_flag + 1) - ((i + (shift_var >> 0x1b) & 0x1f) - (shift_var >> 0x1b))
            enc_flag.append(cc)
        i+=1
    return enc_flag

printable = 'abcdefgijklmnopqrstuvwxyz0123456789{}_?!'
p = 'CTFR{'
for z in range(55):
    for a in printable:
        e = enc(p + a)
        pp = ''.join([chr(x) for x in e])
        if pp == enc_flag[:len(p) + 1]:
            p+=a
            sys.stdout.write('\r' + p)
            break
```

Flag

```
CTFR{st0p_l00k1n9_4t_p53ud0c0d3_n0w_f0cu5_4t_4553mbly}
```
