Apa itu strcpy pada C++ ? strcpy adalah sebuah fungsi yang memindahkan / menduplikat / menambahkan karakter pada pointer yang di tentukan. Nah coba Reverse Attachment yang diberikan.

Download : https://mega.nz/#!skAxGaTD!4bcKaublTSHcqswF0HWbXIKhHDTNZVh1sfVcMug97Ho

```
strcpy: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=84ad1868f5880ba0c02230b397a89e9f7dfaa254, for GNU/Linux 3.2.0, not stripped
```

Dissasamble fungsi main
```
   0x00000000000011a9 <+0>:     endbr64 
   0x00000000000011ad <+4>:     push   rbp
   0x00000000000011ae <+5>:     mov    rbp,rsp
   0x00000000000011b1 <+8>:     sub    rsp,0x70
   0x00000000000011b5 <+12>:    mov    rax,QWORD PTR fs:0x28
   0x00000000000011be <+21>:    mov    QWORD PTR [rbp-0x8],rax
   0x00000000000011c2 <+25>:    xor    eax,eax
   0x00000000000011c4 <+27>:    lea    rax,[rbp-0x70]
   0x00000000000011c8 <+31>:    mov    DWORD PTR [rax],0x52465443
   0x00000000000011ce <+37>:    mov    WORD PTR [rax+0x4],0x7b
   0x00000000000011d4 <+43>:    lea    rax,[rbp-0x70]
   0x00000000000011d8 <+47>:    add    rax,0x5
   0x00000000000011dc <+51>:    mov    WORD PTR [rax],0x3433
   0x00000000000011e1 <+56>:    mov    BYTE PTR [rax+0x2],0x0
   0x00000000000011e5 <+60>:    lea    rax,[rbp-0x70]
   0x00000000000011e9 <+64>:    add    rax,0x7
   0x00000000000011ed <+68>:    mov    WORD PTR [rax],0x7973
   0x00000000000011f2 <+73>:    mov    BYTE PTR [rax+0x2],0x0
   0x00000000000011f6 <+77>:    lea    rax,[rbp-0x70]
   0x00000000000011fa <+81>:    add    rax,0x9
   0x00000000000011fe <+85>:    mov    WORD PTR [rax],0x5f
   0x0000000000001203 <+90>:    lea    rax,[rbp-0x70]
   0x0000000000001207 <+94>:    add    rax,0xa
   0x000000000000120b <+98>:    mov    DWORD PTR [rax],0x727473
   0x0000000000001211 <+104>:   lea    rax,[rbp-0x70]
   0x0000000000001215 <+108>:   add    rax,0xd
   0x0000000000001219 <+112>:   mov    DWORD PTR [rax],0x79703063
   0x000000000000121f <+118>:   mov    WORD PTR [rax+0x4],0x5f
   0x0000000000001225 <+124>:   lea    rax,[rbp-0x70]
   0x0000000000001229 <+128>:   add    rax,0x12
   0x000000000000122d <+132>:   mov    WORD PTR [rax],0x66
   0x0000000000001232 <+137>:   lea    rax,[rbp-0x70]
   0x0000000000001236 <+141>:   add    rax,0x13
   0x000000000000123a <+145>:   mov    DWORD PTR [rax],0x7d67346c
   0x0000000000001240 <+151>:   mov    BYTE PTR [rax+0x4],0x0
   0x0000000000001244 <+155>:   lea    rsi,[rip+0xdbe]        # 0x2009
   0x000000000000124b <+162>:   lea    rdi,[rip+0x2dee]        # 0x4040 <_ZSt4cout@@GLIBCXX_3.4>
   0x0000000000001252 <+169>:   call   0x1090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>                                                                                 
   0x0000000000001257 <+174>:   lea    rsi,[rip+0xdc2]        # 0x2020
   0x000000000000125e <+181>:   lea    rdi,[rip+0x2ddb]        # 0x4040 <_ZSt4cout@@GLIBCXX_3.4>
   0x0000000000001265 <+188>:   call   0x1090 <_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@plt>                                                                                 
   0x000000000000126a <+193>:   mov    eax,0x0
   0x000000000000126f <+198>:   mov    rdx,QWORD PTR [rbp-0x8]
   0x0000000000001273 <+202>:   xor    rdx,QWORD PTR fs:0x28
   0x000000000000127c <+211>:   je     0x1283 <main+218>
   0x000000000000127e <+213>:   call   0x10a0 <__stack_chk_fail@plt>
   0x0000000000001283 <+218>:   leave  
   0x0000000000001284 <+219>:   ret 
```

Psedeo Code
```
undefined8 main(void)

{
  long lVar1;
  long in_FS_OFFSET;
  
  lVar1 = *(long *)(in_FS_OFFSET + 0x28);
  std::operator<<((basic_ostream *)std::cout,"Welcome to CTFR\n");
  std::operator<<((basic_ostream *)std::cout,"Your Flag is somewhere inside this application\n");
  if (lVar1 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```

Flag ada dalam memory stack dan dibandingkan dengan inputan 
```
if (lVar1 != *(long *)(in_FS_OFFSET + 0x28)) { ... }
```

```
gdb -q strcpy
b *main+202
r 

[------------------------------------stack-------------------------------------]
0000| 0x7fffffffdd40 ("CTFR{34sy_strc0py_fl4g}")
0008| 0x7fffffffdd48 ("y_strc0py_fl4g}")
0016| 0x7fffffffdd50 --> 0x7d67346c665f79 ('y_fl4g}')
0024| 0x7fffffffdd58 --> 0x10000ffff 
0032| 0x7fffffffdd60 --> 0x7fffffffdd70 --> 0x2 
0040| 0x7fffffffdd68 --> 0x5555555552e9 (<_GLOBAL__sub_I_main+23>:      pop    rbp)
0048| 0x7fffffffdd70 --> 0x2 
0056| 0x7fffffffdd78 --> 0x55555555533d (<__libc_csu_init+77>:  add    rbx,0x1)
[------------------------------------------------------------------------------]
```

Flag
 
```
CTFR{34sy_strc0py_fl4g}
```

