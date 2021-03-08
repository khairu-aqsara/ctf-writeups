strcpy kali ini lebih susah dengan sebelumnya, Pastikan sudah memahami compiler sebelumnya :D

Download : https://mega.nz/#!QlpEzaCY!YjbPlTOI7I7A9ApRVOkQ9Bxt292IRJDDi4en8NP6vqY

```bash
gdb-peda$ gdb -q strcpy3
gdb-peda$ pd main
gdb-peda$ b *main

...
...
...

gdb-peda$ x/100s 0x55555555a00a
0x55555555a00a:	"CTFR{"
0x55555555a010:	"c0ngr4ts_"
0x55555555a01a:	"h3h3"
0x55555555a01f:	"1s_s0m3_"
0x55555555a028:	"y0u_w1n_"
0x55555555a031:	"th3r3_"
0x55555555a038:	"th15_ch4ll3ng3}"
0x55555555a048:	"h0w_y0u_c4n_"
0x55555555a055:	"w1n_th1s_"
0x55555555a05f:	"w1th0ut_d3c0mp1l3r}"
0x55555555a073:	"f4k3_fl49_"
0x55555555a07e:	"but_y0u_c4n"
0x55555555a08a:	"s0lv3_"
0x55555555a091:	"h3h3}"
0x55555555a097:	"aw3s0m3}"
0x55555555a0a0:	"y0u_4r3_m45t3r}"
0x55555555a0b0:	"s00_34sy_r1ght???}"
0x55555555a0c3:	"c4t_th1s_f0r"
0x55555555a0d0:	"m4st3r_d3c0mp1ler}"
0x55555555a0e3:	"wh0_14m}"
0x55555555a0ec:	"th1s_1s_r34l_flag!!!}"
0x55555555a102:	"Welcome to CTFR\n"
```

Flag

```bash
CTFR{th3r3_1s_s0m3_f4k3_fl49_h3h3}
```