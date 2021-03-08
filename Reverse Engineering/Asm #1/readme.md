Pertama kali mendengar Assembly ? Coba kalkukasi dari instruksi dibawah ini.

```
Flag : CTFR{0x(Hexadecimal)}
```

```

main:
        push    rbp
        mov     rbp, rsp
        mov     DWORD PTR [rbp-4], 10
        add     DWORD PTR [rbp-4], 50
        sub     DWORD PTR [rbp-4], 100
        add     DWORD PTR [rbp-4], 1328
        mov     eax, DWORD PTR [rbp-4]
        pop     rbp
        ret
```

Dalam C
```
main(){
    int a = 10;
    a+=50;
    a-=100;
    a+=1328;
    return a; // atau printf("%x", a);
}

1288 // Dalam base 10
0x508 // Dalam base 16
```

Flag

```
CTFR{0x508}
```

