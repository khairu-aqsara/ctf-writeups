Pertama kali mencoba reverse ? Tools yang disarankan adalah Ghidra, IDA Pro, Radare2, GDB. Untuk menyelesaikan ini anda harus mendownload file dibawah ini

Download : https://rasyidmf.com/assets/challenge/re/first_reverse/first_reverse

Identifier

```
file first_reverse 
first_reverse: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=346e6df5d783772fa9500e633c9bb5a1dbb5345c, for GNU/Linux 3.2.0, not stripped
```

```
strings first_reverse | grep CTFR
```

Flag
```
CTFR{f1rst_fl4g_f0r_r3v3rs3}
```