Sebuah aplikasi simpel yang hanya meminta flag dengan benar, Kalian seharusnya bisa menyelesaikan challenge ini tanpa harus membuka aplikasi tersebut :D.

Download : https://mega.nz/#!ZpoSCCwZ!9IVgZiwKW4F0gWirgIwYq3_iZ1gg42yDlf_eE4E65xQ

```
LogMe: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=6a3eec336b6f9e6a06777f5df7f8d7315b5580e4, for GNU/Linux 3.2.0, not stripped
```

Run
```
./LogMe      
Welcome to CTFR
Please Enter the Flag :
ABC
Wrong Flag!!!  
```

Psedeo Code Dengan Ghidra
```
undefined8 main(void)

{
  bool bVar1;
  basic_ostream *pbVar2;
  undefined8 uVar3;
  long in_FS_OFFSET;
  allocator<char> local_189;
  basic_string local_188 [32];
  basic_string local_168 [32];
  basic_string local_148 [32];
  basic_string local_128 [32];
  basic_string local_108 [32];
  basic_string local_e8 [32];
  basic_string local_c8 [32];
  basic_string local_a8 [32];
  basic_string local_88 [32];
  basic_string local_68 [32];
  basic_string local_48 [40];
  long local_20;
  
  local_20 = *(long *)(in_FS_OFFSET + 0x28);
  std::allocator<char>::allocator();
                    /* try { // try from 0010130f to 00101313 has its CatchHandler @ 001016a8 */
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string
            ((char *)local_188,(allocator *)&DAT_00102009);
  std::allocator<char>::~allocator(&local_189);
                    /* try { // try from 00101331 to 00101680 has its CatchHandler @ 001016c9 */
  std::operator<<((basic_ostream *)std::cout,"Welcome to CTFR\nPlease Enter the Flag :\n");
  std::operator>>((basic_istream *)std::cin,local_188);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::substr
            ((ulong)local_168,(ulong)local_188);
  bVar1 = std::operator==(local_168,"CTFR");
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
            ((basic_string<char,std::char_traits<char>,std::allocator<char>> *)local_168);
  if (bVar1 != false) {
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::substr
              ((ulong)local_148,(ulong)local_188);
    bVar1 = std::operator==(local_148,"5tr_c0m");
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
              ((basic_string<char,std::char_traits<char>,std::allocator<char>> *)local_148);
    if (bVar1 != false) {
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::substr
                ((ulong)local_128,(ulong)local_188);
      bVar1 = std::operator==(local_128,"{5tr_c0m");
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
                ((basic_string<char,std::char_traits<char>,std::allocator<char>> *)local_128);
      if (bVar1 != false) {
        std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::substr
                  ((ulong)local_108,(ulong)local_188);
        bVar1 = std::operator==(local_108,"c0mp4r3_w1th_5");
        std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
                  ((basic_string<char,std::char_traits<char>,std::allocator<char>> *)local_108);
        if (bVar1 != false) {
          std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::substr
                    ((ulong)local_e8,(ulong)local_188);
          bVar1 = std::operator==(local_e8,"r_c0mp4r3_");
          std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
          ~basic_string((basic_string<char,std::char_traits<char>,std::allocator<char>> *)local_e8);
          if (bVar1 != false) {
            std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::substr
                      ((ulong)local_c8,(ulong)local_188);
            bVar1 = std::operator==(local_c8,"r3_w1th_5ubstr1n");
            std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
            ~basic_string((basic_string<char,std::char_traits<char>,std::allocator<char>> *)local_c8
                         );
            if (bVar1 != false) {
              std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::substr
                        ((ulong)local_a8,(ulong)local_188);
              bVar1 = std::operator==(local_a8,"_c0mp4r3_w1t");
              std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
              ~basic_string((basic_string<char,std::char_traits<char>,std::allocator<char>> *)
                            local_a8);
              if (bVar1 != false) {
                std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::substr
                          ((ulong)local_88,(ulong)local_188);
                bVar1 = std::operator==(local_88,"_w1th_5ubstr1n9}");
                std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                ~basic_string((basic_string<char,std::char_traits<char>,std::allocator<char>> *)
                              local_88);
                if (bVar1 != false) {
                  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                  substr((ulong)local_68,(ulong)local_188);
                  bVar1 = std::operator==(local_68,"0mp4r3_w1th");
                  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                  ~basic_string((basic_string<char,std::char_traits<char>,std::allocator<char>> *)
                                local_68);
                  if (bVar1 != false) {
                    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                    substr((ulong)local_48,(ulong)local_188);
                    bVar1 = std::operator==(local_48,"R{5tr_c0mp4r");
                    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                    ~basic_string((basic_string<char,std::char_traits<char>,std::allocator<char>> *)
                                  local_48);
                    if (bVar1 != false) {
                      pbVar2 = std::operator<<((basic_ostream *)std::cout,"This is your flag : ");
                      std::operator<<(pbVar2,local_188);
                      uVar3 = 1;
                      goto LAB_00101686;
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
  std::operator<<((basic_ostream *)std::cout,"Wrong Flag!!!");
  uVar3 = 0;
LAB_00101686:
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
            ((basic_string<char,std::char_traits<char>,std::allocator<char>> *)local_188);
  if (local_20 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return uVar3;
}
```

Sebenarnya dengan membaca hasil decompilernya juga udah bisa ketahuan flagnya, tapi dengan GDB jauh jadi lebih simple, breakpoint disalah satu `<+184>:   lea    rax,[rbp-0x160]` kemudian menjalankan next instrucstion hingga `<main+187>:   lea    rax,[rbp-0x160]` seharusnya potongan-potongan flag sudah terinisialisasi sebelum dibandingkan, bisa di cek di nilai register RSI nya

```
gdb -q LogMe
pd main
b *main+187
ni
...
```

hasilnya jika dicek di RSI
```
gdb-peda$ x/8s $rsi
0x55555555603d: ""
0x55555555603e: "5tr_c0m"
0x555555556046: "{5tr_c0m"
0x55555555604f: "c0mp4r3_w1th_5"
0x55555555605e: "r_c0mp4r3_"
0x555555556069: "r3_w1th_5ubstr1n"
0x55555555607a: "_c0mp4r3_w1t"
0x555555556087: "_w1th_5ubstr1n9}"
```

Flag 

```
CTFR{5tr_c0mp4r3_w1th_5ubstr1n9}}
```