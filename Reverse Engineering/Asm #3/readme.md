Kali ini, ada penambahakan instruksi sar, sal dan imul. Coba kalkukasi yaah, Format flag sama seperti challenge sebelumnya.

```
Flag : CTFR{0x(Hexadecimal)}
```

```asm
main:
        push    rbp
        mov     rbp, rsp
        mov     DWORD PTR [rbp-4], 460
        sar     DWORD PTR [rbp-4], 2
        sal     DWORD PTR [rbp-4], 5
        mov     eax, DWORD PTR [rbp-4]
        and     eax, 1
        test    eax, eax
        jne     .L2
        add     DWORD PTR [rbp-4], 100
        jmp     .L3
.L2:
        mov     eax, DWORD PTR [rbp-4]
        imul    eax, eax, 100
        mov     DWORD PTR [rbp-4], eax
.L3:
        mov     eax, DWORD PTR [rbp-4]
        pop     rbp
        ret

```

Dalam C 

```c
int main(){
    int a;
    int b;

    a = 460;
    a = a >> 2;
    a = a << 5;
    if((a & 1) == 0){
        a+=100;
    }else{
        a = a * 100;
    }

    //printf("%d\n", a); // 3780
    //printf("%x\n", a); // ec4

}
```

Flag 

```
CTFR{0xec4}
```
