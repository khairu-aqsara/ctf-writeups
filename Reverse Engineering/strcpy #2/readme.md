Udah selesai pada challenge pertama ? Nah coba lanjut ke challenge ke-2. Kalo yang pertama easy, berarti ke-2 juga easy :D

Download : https://mega.nz/#!Bxwi3ZrA!CAWqiGKKXVtVyDtrtQrdj9vRgue7nU9HkeRUYQb1HTs

```
strcpy2: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=c8acac5958de73bd15382dd8945efd8d4571b44e, for GNU/Linux 3.2.0, not stripped
```

Run 

```
$./strcpy2
Welcome to CTFR
Your flag is somewhere inside this application!
Also here is your flag if you still confusing how to retrieve it!
Flag : ZN\Ky{<�}ev6iewdmy6w5c7wv7z7vc76b{u~uih2s`   
```

Disass

```
__int64 sub_1451()
{
  __int64 v0; // rsi
  __int64 v1; // rdx
  __int64 result; // rax
  __int64 v3; // rcx
  unsigned __int64 v4; // rt1
  char v5; // [rsp+Fh] [rbp-141h]
  char v6; // [rsp+10h] [rbp-140h]
  char v7; // [rsp+30h] [rbp-120h]
  char v8; // [rsp+50h] [rbp-100h]
  char v9; // [rsp+70h] [rbp-E0h]
  char v10; // [rsp+90h] [rbp-C0h]
  char v11; // [rsp+B0h] [rbp-A0h]
  char v12; // [rsp+D0h] [rbp-80h]
  char v13; // [rsp+F0h] [rbp-60h]
  char v14; // [rsp+110h] [rbp-40h]
  unsigned __int64 v15; // [rsp+138h] [rbp-18h]

  v15 = __readfsqword(0x28u);
  sub_1240(&v5);
  sub_1200(&v6, &unk_2009, &v5);
  sub_11D0(&v5);
  sub_11C0(&v6, "RFTC");
  sub_1170(&v14, &v6);
  encrypt(&v7, &v14);
  sub_11F0(&v6, &v7);
  sub_1180(&v7);
  sub_1180(&v14);
  sub_11C0(&v6, "rt5{");
  sub_1170(&v14, &v6);
  encrypt(&v8, &v14);
  sub_11F0(&v6, &v8);
  sub_1180(&v8);
  sub_1180(&v14);
  sub_11C0(&v6, "w_yp0c_");
  sub_1170(&v14, &v6);
  encrypt(&v9, &v14);
  sub_11F0(&v6, &v9);
  sub_1180(&v9);
  sub_1180(&v14);
  sub_11C0(&v6, "r_ht1");
  sub_1170(&v14, &v6);
  encrypt(&v10, &v14);
  sub_11F0(&v6, &v10);
  sub_1180(&v10);
  sub_1180(&v14);
  sub_11C0(&v6, "s1_3sr3v3r_");
  sub_1170(&v14, &v6);
  encrypt(&v11, &v14);
  sub_11F0(&v6, &v11);
  sub_1180(&v11);
  sub_1180(&v14);
  sub_11C0(&v6, "43_");
  sub_1170(&v14, &v6);
  encrypt(&v12, &v14);
  sub_11F0(&v6, &v12);
  sub_1180(&v12);
  sub_1180(&v14);
  sub_11C0(&v6, "ys");
  sub_1170(&v14, &v6);
  encrypt(&v13, &v14);
  sub_11F0(&v6, &v13);
  sub_1180(&v13);
  sub_1180(&v14);
  sub_11C0(&v6, "}thg1r_");
  sub_1170(&v13, &v6);
  encrypt(&v14, &v13);
  sub_11F0(&v6, &v14);
  sub_1180(&v14);
  sub_1180(&v13);
  sub_1220("Welcome to CTFR\nYour flag is somewhere inside this application!");
  sub_1150("%s", "Also here is your flag if you still confusing how to retrieve it!\nFlag : ");
  v0 = sub_1160(&v6);
  sub_1150("%s", v0);
  sub_1180(&v6);
  result = 0LL;
  v4 = __readfsqword(0x28u);
  v3 = v4 ^ v15;
  if ( v4 != v15 )
    result = sub_11E0(&v6, v0, v1, v3);
  return result;
}
```

GDB
```
gdb -q strcpy2
pd main
b *main+75
```

Nilai Register 
```
RDX: 0x555555556009 --> 0x7472004354465200 ('')
RSI: 0x555555556009 --> 0x7472004354465200 ('')
```

```
gdb-peda$ x/8gx 0x555555556009
0x555555556009: 0x7472004354465200      0x3070795f77007b35
0x555555556019: 0x3174685f72005f63      0x337273335f317300
0x555555556029: 0x5f3334005f723376      0x6768747d00737900
0x555555556039: 0x57000000005f7231      0x7420656d6f636c65

gdb-peda$ x/s 0x555555556009
0x555555556009: ""

gdb-peda$ x/s 0x555555556019
0x555555556019: "c_"
```

Final
```
gdb-peda$ x/10s 0x555555556009
0x555555556009: ""
0x55555555600a: "RFTC"
0x55555555600f: "rt5{"
0x555555556014: "w_yp0c_"
0x55555555601c: "r_ht1"
0x555555556022: "s1_3sr3v3r_"
0x55555555602e: "43_"
0x555555556032: "ys"
0x555555556035: "}thg1r_"
0x55555555603d: "" 
```

Flag

```
CTFR{5tr_c0py_w1th_r3v3rs3_1s_34sy_r1ght}
```

