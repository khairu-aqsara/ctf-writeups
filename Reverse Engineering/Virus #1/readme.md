Mimin ada aplikasi virus ini, coba cari tau pengerjaan virus nya :D

Download : https://mega.nz/#!4s5QTZiI!nvFbga7KDXZBhJjjrDJlt7iHHl2t8kCxUKsNGrB66Ao

Ada beberapa fungsi menarik didalamnya

```C
ask(basic_string param_1)
main(void)
sleep(int param_1)
basic_string<char,std::char_traits<char>,std::allocator<char>> * want[abi:cxx11](void)
```

Psudeo Fungsi Main

```C
undefined8 main(void)

{
  basic_string<char,std::char_traits<char>,std::allocator<char>> local_78 [32];
  basic_string<char,std::char_traits<char>,std::allocator<char>> string_get_request [32];
  basic_string<char,std::char_traits<char>,std::allocator<char>> local_38 [40];
  
  curl = curl_easy_init();
  if (curl == 0) {
    puts("Some library not initialize sucessfully! Try to contact administrator.");
  }
  else {
    puts("Locating hacker server...");
    sleep(500);
    puts("Got it, now downloading virus...");
    want[abi:cxx11]();

    std::operator+((char *)string_get_request,(basic_string *)"http://web.ctf.rasyidmf.com/?virus=")
    ;
    ask((basic_string)0x88);
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
              (local_78);
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
              (string_get_request);
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
              (local_38);
    sleep(3000);
    puts("Initialize virus...");
    sleep(2000);
    puts("Virus has been installed in this computer.");
    sleep(1000);
    puts("Completing...");
    sleep(2000);
    printf("Done!");
  }
  return 0;
}
```

```bash
$ gdb -q virus1
gdb-peda$ pd main
0x0000000000001598 <+0>:	push   rbp
0x0000000000001599 <+1>:	mov    rbp,rsp
0x000000000000159c <+4>:	push   rbx
0x000000000000159d <+5>:	sub    rsp,0x68
0x00000000000015a1 <+9>:	call   0x1070 <curl_easy_init@plt>
0x00000000000015a6 <+14>:	mov    QWORD PTR [rip+0x4b73],rax        # 0x6120 <curl>
0x00000000000015ad <+21>:	mov    rax,QWORD PTR [rip+0x4b6c]        # 0x6120 <curl>
0x00000000000015b4 <+28>:	test   rax,rax
0x00000000000015b7 <+31>:	je     0x1698 <main+256>
0x00000000000015bd <+37>:	lea    rdi,[rip+0x1ddc]        # 0x33a0
0x00000000000015c4 <+44>:	call   0x11a0 <puts@plt>
0x00000000000015c9 <+49>:	mov    edi,0x1f4
0x00000000000015ce <+54>:	call   0x149f <sleep(int)>
0x00000000000015d3 <+59>:	lea    rdi,[rip+0x1de6]        # 0x33c0
0x00000000000015da <+66>:	call   0x11a0 <puts@plt>
0x00000000000015df <+71>:	lea    rax,[rbp-0x30]
0x00000000000015e3 <+75>:	mov    rdi,rax
0x00000000000015e6 <+78>:	call   0x1337 <want[abi:cxx11]()>
0x00000000000015eb <+83>:	lea    rax,[rbp-0x50]
0x00000000000015ef <+87>:	lea    rdx,[rbp-0x30]
0x00000000000015f3 <+91>:	lea    rsi,[rip+0x1dee]        # 0x33e8
0x00000000000015fa <+98>:	mov    rdi,rax
0x00000000000015fd <+101>:	call   0x17d9
0x0000000000001602 <+106>:	lea    rax,[rbp-0x70]
0x0000000000001606 <+110>:	lea    rdx,[rbp-0x50]
0x000000000000160a <+114>:	mov    rsi,rdx
0x000000000000160d <+117>:	mov    rdi,rax
0x0000000000001610 <+120>:	call   0x14cc
0x0000000000001615 <+125>:	lea    rax,[rbp-0x70]
0x0000000000001619 <+129>:	mov    rdi,rax
0x000000000000161c <+132>:	call   0x10e0
0x0000000000001621 <+137>:	lea    rax,[rbp-0x50]
0x0000000000001625 <+141>:	mov    rdi,rax
0x0000000000001628 <+144>:	call   0x10e0
0x000000000000162d <+149>:	lea    rax,[rbp-0x30]
0x0000000000001631 <+153>:	mov    rdi,rax
0x0000000000001634 <+156>:	call   0x10e0
0x0000000000001639 <+161>:	mov    edi,0xbb8
0x000000000000163e <+166>:	call   0x149f <sleep(int)>
0x0000000000001643 <+171>:	lea    rdi,[rip+0x1dc2]        # 0x340c
0x000000000000164a <+178>:	call   0x11a0 <puts@plt>
0x000000000000164f <+183>:	mov    edi,0x7d0
0x0000000000001654 <+188>:	call   0x149f <sleep(int)>
0x0000000000001659 <+193>:	lea    rdi,[rip+0x1dc0]        # 0x3420
0x0000000000001660 <+200>:	call   0x11a0 <puts@plt>
0x0000000000001665 <+205>:	mov    edi,0x3e8
0x000000000000166a <+210>:	call   0x149f <sleep(int)>
0x000000000000166f <+215>:	lea    rdi,[rip+0x1dd5]        # 0x344b
0x0000000000001676 <+222>:	call   0x11a0 <puts@plt>
0x000000000000167b <+227>:	mov    edi,0x7d0
0x0000000000001680 <+232>:	call   0x149f <sleep(int)>
0x0000000000001685 <+237>:	lea    rdi,[rip+0x1dcd]        # 0x3459
0x000000000000168c <+244>:	mov    eax,0x0
0x0000000000001691 <+249>:	call   0x1040 <printf@plt>
0x0000000000001696 <+254>:	jmp    0x16a4 <main+268>
0x0000000000001698 <+256>:	lea    rdi,[rip+0x1dc1]        # 0x3460
0x000000000000169f <+263>:	call   0x11a0 <puts@plt>
0x00000000000016a4 <+268>:	mov    eax,0x0
0x00000000000016a9 <+273>:	jmp    0x16d6 <main+318>
0x00000000000016ab <+275>:	mov    rbx,rax
0x00000000000016ae <+278>:	lea    rax,[rbp-0x50]
0x00000000000016b2 <+282>:	mov    rdi,rax
0x00000000000016b5 <+285>:	call   0x10e0
0x00000000000016ba <+290>:	jmp    0x16bf <main+295>
0x00000000000016bc <+292>:	mov    rbx,rax
0x00000000000016bf <+295>:	lea    rax,[rbp-0x30]
0x00000000000016c3 <+299>:	mov    rdi,rax
0x00000000000016c6 <+302>:	call   0x10e0
0x00000000000016cb <+307>:	mov    rax,rbx
0x00000000000016ce <+310>:	mov    rdi,rax
0x00000000000016d1 <+313>:	call   0x11e0 <_Unwind_Resume@plt>
0x00000000000016d6 <+318>:	mov    rbx,QWORD PTR [rbp-0x8]
0x00000000000016da <+322>:	leave  
0x00000000000016db <+323>:	ret 
```

Breakpoint setelah memanggil fungsi call  `0x1337 <want[abi:cxx11]()>` nilai return dari fungsi akan ada di register `$rax`

```bash
gdb-peda$ b *main+83
RAX: 0x7fffffffe590 --> 0x55555558e610
```

Nilai rax dikirimkan ke alamat `0x55555558e610` 

```bash
gdb-peda$ 
0x55555558e610:	"S0VZVkVSMlZOWjJES1RLSUtaVEZVMlNDR0ZSRzJVVEdNSktFNFpTT0pCSkdNWktVSUlZV0czQlpHQlJXVVVUTkxKVkVNMlRHS0U2VDI9PT0="
```

Dapetnya base64, dicoba decode dengan perintah 

```bash
echo "S0VZVkVSMlZOWjJES1RLSUtaVEZVMlNDR0ZSRzJVVEdNSktFNFpTT0pCSkdNWktVSUlZV0czQlpHQlJXVVVUTkxKVkVNMlRHS0U2VDI9PT0=" | base64 -d
```

hasilnya base Encode yang lain, pake tools https://github.com/mufeedvh/basecrack biar nyari basenya otomatis

```bash
python3 basecrack.py -b S0VZVkVSMlZOWjJES1RLSUtaVEZVMlNDR0ZSRzJVVEdNSktFNFpTT0pCSkdNWktVSUlZV0czQlpHQlJXVVVUTkxKVkVNMlRHS0U2VDI9PT0= --magic
```

hasilnya

```bash
[-] Encoded Base: S0VZVkVSMlZOWjJES1RLSUtaVEZVMlNDR0ZSRzJVVEdNSktFNFpTT0pCSkdNWktVSUlZV0czQlpHQlJXVVVUTkxKVkVNMlRHS0U2VDI9PT0=

[-] Iteration: 1

[-] Heuristic Found Encoding To Be: Base64

[-] Decoding as Base64: KEYVER2VNZ2DKTKIKZTFU2SCGFRG2UTGMJKE4ZSOJBJGMZKUIIYWG3BZGBRWUUTNLJVEM2TGKE6T2===

{{<<======================================================================>>}}

[-] Iteration: 2

[-] Heuristic Found Encoding To Be: Base32

[-] Decoding as Base32: Q1RGUnt5MHVfZjB1bmRfbTNfNHRfeTB1cl90cjRmZjFjfQ==

{{<<======================================================================>>}}

[-] Iteration: 3

[-] Heuristic Found Encoding To Be: Base64

[-] Decoding as Base64: CTFR{y0u_f0und_m3_4t_y0ur_tr4ff1c}

{{<<======================================================================>>}}

[-] Total Iterations: 3

[-] Encoding Pattern: Base64 -> Base32 -> Base64

[-] Magic Decode Finished With Result: CTFR{y0u_f0und_m3_4t_y0ur_tr4ff1c}

[-] Finished in 0.0031 seconds
```

Flag

```
CTFR{y0u_f0und_m3_4t_y0ur_tr4ff1c
```

