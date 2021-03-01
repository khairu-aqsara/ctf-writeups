Pada gambar ini terdapat flag yang disembunyikan di dalam hex tersebut. Tolong carikan yaah :(
Hint: Pakai Hexdump untuk menyelesaikan Challenge ini

Download: https://mega.nz/#!llQi1LCB!8qybw_QiJsiVB7xMCXyRMMGcJBGshSxTohTdvsRO8xE

Commands
```
xxd -s -0x40 kocheng_dipukul.png

000693f7: 0049 454e 44ae 4260 8243 0054 0046 0052  .IEND.B`.C.T.F.R
00069407: 007b 0068 0033 0078 005f 0064 0075 006d  .{.h.3.x._.d.u.m
00069417: 0070 005f 0031 006e 005f 0031 006d 0034  .p._.1.n._.1.m.4
00069427: 0067 0033 005f 0066 0031 006c 0033 007d  .g.3._.f.1.l.3.}
```

Flag

```
CTFR{h3x_dump_1n_1m4g3_f1l3}
```