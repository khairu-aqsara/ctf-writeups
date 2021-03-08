Masih lanjut dengan Assembly sebelumnya, Kali ini mimin tambahkan instruksi "cmp" atau compare, setara dengan if statement. Nah coba, kalkukasi lagi yaah

```
Flag : CTFR{0x(Hexadecimal)}
```

```
main:
        push    rbp
        mov     rbp, rsp
        mov     DWORD PTR [rbp-4], 70
        cmp     DWORD PTR [rbp-4], 79
        jle     .L2
        add     DWORD PTR [rbp-4], 20
        jmp     .L3
.L2:
        sub     DWORD PTR [rbp-4], 40
.L3:
        mov     eax, DWORD PTR [rbp-4]
        pop     rbp
        ret
```

Dalam C 

```
main(){
    int a = 70;
    if(79<=a){
       a+=20; 
    }else{
        a-=40;
    }

    return a; // printf("%x", a);
}
```

hasilnya

```
30 // Dalam Decimal
0x1e // Dalam Hexa
```

Flag 

```
CTFR{0x1e}
```

