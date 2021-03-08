Arti dari Title diatas "Hanya Lompat" Mksdnya apaan yaa ? Coba deh di cari sendiri maksudnya dan coba Selesaikan selesaikan challenge dibawah ini.

Download : https://mega.nz/#!UtQCUBZS!CUccRHYu_lpWsfs0aLLqql0eNsd0n1Hv_cSP5wl2ezA


```
gdb -q jump
info functions

0x0000000000001000  _init
0x0000000000001080  __cxa_finalize@plt
0x0000000000001090  printf@plt
0x00000000000010a0  __cxa_atexit@plt
0x00000000000010b0  __stack_chk_fail@plt
0x00000000000010c0  std::ios_base::Init::Init()@plt
0x00000000000010d0  puts@plt
0x00000000000010e0  _start
0x0000000000001110  deregister_tm_clones
0x0000000000001140  register_tm_clones
0x0000000000001180  __do_global_dtors_aux
0x00000000000011c0  frame_dummy
0x00000000000011c9  flag()
0x00000000000012a4  main
0x00000000000012cb  __static_initialization_and_destruction_0(int, int)
0x0000000000001318  _GLOBAL__sub_I__Z4flagv
0x0000000000001340  __libc_csu_init
0x00000000000013b0  __libc_csu_fini
0x00000000000013b8  _fini
```

kalo jalanin aplikasinya ga manggil fungsi `flag()` sama sekali, dan ga ada bagian yang vulnerable, jadi sesuai judulnya jump aja ke fungsi `flag()`.

```
b *main
jump *flag
gdb-peda$ jump *flag
Continuing at 0x5555555551c9.
Here your flag : CTFR{why_n33d_d3c0mp1l3r_wh3n_y0u_c4n_jump}UUU[Inferior 1 (process 48) exited normally]
Warning: not running or target is remote
gdb-peda$ 
````

Flag

````
CTFR{why_n33d_d3c0mp1l3r_wh3n_y0u_c4n_jump}
```