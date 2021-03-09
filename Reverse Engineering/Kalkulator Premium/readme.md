Mimin ada aplikasi Kalkulator Premium yang bisa menghitung, Tapi dibutuhkan Key untuk masuknya. Bisa bantu mimin gak :(

Download : https://mega.nz/#!lwgCFYIT!oqD0K_25JoQFLuhrFeQTgOe_97tiIC4Ni1o3sqfullw

Psudeo Code Dengan Ghidra

```C

undefined8 main(int param_1,long param_2)

{
  bool bVar1;
  int iVar2;
  ulong uVar3;
  char *pcVar4;
  basic_ostream<char,std::char_traits<char>> *this;
  undefined8 uVar5;
  long lVar6;
  ulong uVar7;
  undefined8 *puVar8;
  undefined8 *puVar9;
  long in_FS_OFFSET;
  allocator<char> local_409;
  int local_408;
  int local_404;
  int local_400;
  int local_3fc;
  int local_3f8;
  int local_3f4;
  ulong local_3f0;
  basic_string local_3e8 [32];
  undefined8 local_3c8 [117];
  long local_20;
  
  local_20 = *(long *)(in_FS_OFFSET + 0x28);
  lVar6 = 0x74;
  puVar8 = &DAT_00102120;
  puVar9 = local_3c8;
  while (lVar6 != 0) {
    lVar6 = lVar6 + -1;
    *puVar9 = *puVar8;
    puVar8 = puVar8 + 1;
    puVar9 = puVar9 + 1;
  }
  *(undefined4 *)puVar9 = *(undefined4 *)puVar8;
  puts("Welcome to CTFR");
  puts("-= Calculator Premium -=");
  puts(
      "-= Before you using this, Enter password to do this. If you doesn\'t have it, Buy fromadmin.. -="
      );
  if (param_1 < 2) {
    puts("Enter key from argument : <key>");
  }
  else {
    local_408 = 0;
    local_3fc = 0xe9;
    local_404 = 0;
    std::allocator<char>::allocator();
                    /* try { // try from 00101425 to 00101429 has its CatchHandler @ 001016e7 */
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string
              ((char *)local_3e8,*(allocator **)(param_2 + 8));
    std::allocator<char>::~allocator(&local_409);
                    /* try { // try from 0010144a to 001016b3 has its CatchHandler @ 00101708 */
    bVar1 = std::operator!=(local_3e8,"");
    if (bVar1 == false) {
      puts("Enter key from argument : <key>");
    }
    else {
      lVar6 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::size();
      if (lVar6 != local_3fc) {
        printf("Invalid Key size! Your size : ");
        uVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::size()
        ;
        this = (basic_ostream<char,std::char_traits<char>> *)
               std::basic_ostream<char,std::char_traits<char>>::operator<<
                         ((basic_ostream<char,std::char_traits<char>> *)std::cout,uVar3);
        std::basic_ostream<char,std::char_traits<char>>::operator<<
                  (this,std::endl<char,std::char_traits<char>>);
                    /* WARNING: Subroutine does not return */
        exit(1);
      }
      local_400 = 0;
      while( true ) {
        uVar7 = SEXT48(local_400);
        uVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::size()
        ;
        if (uVar3 <= uVar7) break;
        pcVar4 = (char *)std::__cxx11::
                         basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[]
                                   ((ulong)local_3e8);
        local_3f8 = (int)*pcVar4;
        iVar2 = local_3f8 * 0x400;
        uVar7 = SEXT48(local_3f8);
        uVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::size()
        ;
        local_3f4 = ((int)(uVar7 % uVar3) - local_400) + iVar2;
        local_3f0 = (ulong)(local_3f8 + 0x854f6) + (long)((local_3f8 + 0x1f) * 2) +
                    (long)(local_3f8 * 2 + 1) + (long)(local_3f8 * 2 + 0x19) + (long)(local_3f8 * 2)
        ;
        if (local_3f0 == (long)(local_3f8 * 2)) {
          local_408 = local_408 + -10;
        }
        if (local_3f0 == (long)(local_3f8 * 2)) {
          local_408 = local_408 + 0x14;
        }
        if (local_3f4 == *(int *)((long)local_3c8 + (long)local_400 * 4)) {
          local_404 = local_404 + 1;
          if ((local_3f0 & 1) == 0) {
            local_408 = local_408 * 10;
          }
        }
        else {
          if (local_3f0 != 0x14) {
            puts("Invalid key!");
                    /* WARNING: Subroutine does not return */
            exit(1);
          }
        }
        local_400 = local_400 + 1;
      }
    }
    if (local_404 == local_3fc) {
      uVar5 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::c_str();
      printf("Here is your flag : %s\n",uVar5);
    }
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
              ((basic_string<char,std::char_traits<char>,std::allocator<char>> *)local_3e8);
  }
  if (local_20 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}

```

Yang Paling penting diperhatikan dibagian

```C
      ke = 0;
      while( true ) {
        loop_ke = SEXT48(ke);
        jml_char = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                   size();
        if (jml_char <= loop_ke) break;
        key_ke = (char *)std::__cxx11::
                         basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[]
                                   ((ulong)local_3e8);
        ord_key = (int)*key_ke;
        faktor_kali = ord_key * 0x400;
        loop_ke = SEXT48(ord_key);
        jml_char = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                   size();
        num_a = ((int)(loop_ke % jml_char) - ke) + faktor_kali;
        num_b = (ulong)(ord_key + 0x854f6) + (long)((ord_key + 0x1f) * 2) + (long)(ord_key * 2 + 1)
                + (long)(ord_key * 2 + 0x19) + (long)(ord_key * 2);
        if (num_b == (long)(ord_key * 2)) {
          local_408 = local_408 + -10;
        }
        if (num_b == (long)(ord_key * 2)) {
          local_408 = local_408 + 0x14;
        }
        if (num_a == *(int *)((long)local_3c8 + (long)ke * 4)) {
          panjang_kunci_dicari = panjang_kunci_dicari + 1;
          if ((num_b & 1) == 0) {
            local_408 = local_408 * 10;
          }
        }
        else {
          if (num_b != 0x14) {
            puts("Invalid key!");
            exit(1);
          }
        }
        ke = ke + 1;
      }
    if (panjang_kunci_dicari == panjang_kunci) {
      flag = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::c_str();
      printf("Here is your flag : %s\n",flag);
    }
```

Re Produce Ke Versi Python yang lebih simple

```python
arr_data = []
jumlah = 0xe9

for i in range(len(arr_data)):
	for ord_key in range(20,127):
		f = ((ord_key % jumlah) - i) + (ord_key * 0x400)
		if f == arr_data[i]:
			print(chr(ord_key), end='')
			break

```

sejauh ini data ga tau ada dimana, mau ga mau harus nyari arr_data dulu

```bash

gdb -q calculator
pd main

0x0000555555555349 <+0>:	endbr64 
0x000055555555534d <+4>:	push   rbp
0x000055555555534e <+5>:	mov    rbp,rsp
0x0000555555555351 <+8>:	push   r12
0x0000555555555353 <+10>:	push   rbx
0x0000555555555354 <+11>:	sub    rsp,0x410
0x000055555555535b <+18>:	mov    DWORD PTR [rbp-0x414],edi
0x0000555555555361 <+24>:	mov    QWORD PTR [rbp-0x420],rsi
0x0000555555555368 <+31>:	mov    rax,QWORD PTR fs:0x28
0x0000555555555371 <+40>:	mov    QWORD PTR [rbp-0x18],rax
0x0000555555555375 <+44>:	xor    eax,eax
0x0000555555555377 <+46>:	lea    rax,[rbp-0x3c0]
0x000055555555537e <+53>:	lea    rdx,[rip+0xd9b]        # 0x555555556120
0x0000555555555385 <+60>:	mov    ecx,0x74
0x000055555555538a <+65>:	mov    rdi,rax
0x000055555555538d <+68>:	mov    rsi,rdx
0x0000555555555390 <+71>:	rep movs QWORD PTR es:[rdi],QWORD PTR ds:[rsi]
0x0000555555555393 <+74>:	mov    rdx,rsi
0x0000555555555396 <+77>:	mov    rax,rdi
0x0000555555555399 <+80>:	mov    ecx,DWORD PTR [rdx]
0x000055555555539b <+82>:	mov    DWORD PTR [rax],ecx
0x000055555555539d <+84>:	lea    rax,[rax+0x4]
0x00005555555553a1 <+88>:	lea    rdx,[rdx+0x4]
0x00005555555553a5 <+92>:	lea    rdi,[rip+0xc75]        # 0x555555556021
```

Kalo dilihat dari hasil disassnya, setelah inisialisasi semua variable seharusnya arr_data ada di sekitaran `main+46` sampai ke `main+68` di breakpoint aja dari `main+46`

```bash

gdb-peda$ b *main+46
gdb-peda$ r
Breakpoint 1, 0x0000555555555377 in main ()
gdb-peda$ x/x $rax
0x0:	Cannot access memory at address 0x0
```

karena memory belum bisa diakses, lanjut aka ke instruksi selanjutnya

```bash
gdb-peda$ ni
...
RAX: 0x7fffffffe1e0 --> 0xffffffffffffffff
...
RDX: 0x7fffffffe698 --> 0x7fffffffe8a1
...
...
RIP: 0x55555555537e (<main+53>:	lea    rdx,[rip+0xd9b]        # 0x555555556120)
```

ini artinya kemungkinan variable `arr_data` sudah dibawa dari register `$rdx` kalo dijalanin sampe instruksi berikutnya, seharusnya `arr_data` sudah ada nilainya

```bash
gdb-peda$ ni
...
...
RDX: 0x555555556120 --> 0x1a06700010c43
...
...
...
RIP: 0x555555555385 (<main+60>:	mov    ecx,0x74)
```

kalo ditelusuri nilai dari register $rdx, Kemudian set print elements 0 karena default print gdb adalah 200, dan data yang ingin di print adalah 233 maka perlu di ubah ke lebih dari 233 atau dalam kasus ini 0 yang berarti unlimited. Setelah itu tinggal menprint datanya sebagai int[233].

```bash
gdb-peda$ x/2gx $rdx
0x555555556120:	0x0001a06700010c43	0x0001b0690001845f
gdb-peda$ x/gx $rdx
0x555555556120:	0x0001a06700010c43
gdb-peda$ set print elements 0
print /d (int[233]) * 0x555555556120
$3 = {68675, 106599, 99423, 110697, 110696, 103520, 112744, 105568, 103517, 32791, 107615, 112739, 107613, 32787, 102486, 107610, 100434, 119908, 99407, 
  118881, 32780, 102479, 103503, 112727, 105551, 99400, 112724, 32773, 100422, 103496, 116820, 100419, 99393, 117842, 107591, 117840, 32764, 103488, 
  112712, 109636, 116810, 107584, 114758, 117832, 107581, 32755, 117829, 103478, 102452, 103476, 116800, 106549, 99373, 112697, 99371, 45045, 32744, 66568, 
  109617, 99366, 112690, 32739, 118838, 103462, 118836, 99360, 114734, 107558, 32732, 108581, 107555, 109604, 99353, 32727, 109601, 99350, 110624, 107548, 
  99347, 112671, 32720, 100369, 103443, 112667, 103441, 116765, 32714, 100363, 103437, 112661, 103435, 116759, 32708, 99332, 121881, 99330, 111629, 32703, 
  102402, 103426, 112650, 105474, 99323, 112647, 32696, 114695, 103419, 111618, 113667, 105466, 116740, 99314, 111613, 99312, 112636, 32685, 68559, 43958, 
  43957, 32681, 102380, 107504, 106478, 99302, 116726, 99300, 114674, 109548, 99297, 112621, 32670, 108519, 99293, 112617, 105441, 99290, 112614, 32663, 
  117737, 99286, 111585, 114659, 99283, 107482, 32656, 111580, 103379, 111578, 100302, 119776, 99275, 118749, 32648, 114647, 107471, 109520, 107469, 
  116693, 99267, 112591, 32640, 117714, 99263, 109512, 107461, 118735, 32634, 59283, 69532, 46981, 32630, 67479, 118728, 121802, 32626, 106425, 103349, 
  116673, 103347, 32621, 107445, 117694, 32618, 123842, 113591, 119740, 116664, 32613, 104362, 110511, 99235, 105384, 32608, 59257, 32606, 68480, 85904, 
  71553, 83852, 125876, 50025, 54124, 97173, 118697, 106396, 50020, 117669, 97168, 101267, 106391, 53090, 110489, 110488, 52062, 112536, 105360, 52059, 
  97158, 106382, 53081, 116630, 102279, 97153, 52052, 112526, 48975, 119699, 58198, 106372, 64346, 64345, 64344, 127893}
```

hasilnya jika dijalankan
```
Challenge ini dibuat dengan berbasis enkripsi sederhana, Akan tetapi jika kalian bener bener awam dengan pemograman C++ diharapkan jangan sampai membuat pikiran sakit :D. Btw here is your flag : CTFR{15_th1s_ch4ll3ng3_h4rd_3n0u9h???}
```

Flag 

```
CTFR{15_th1s_ch4ll3ng3_h4rd_3n0u9h???}
```





