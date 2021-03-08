main:
        push    rbp
        mov     rbp, rsp
        mov     BYTE PTR [rbp-112], 67
        mov     BYTE PTR [rbp-111], 84
        mov     BYTE PTR [rbp-110], 70
        movzx   eax, BYTE PTR [rbp-110]
        cmp     al, 83
        jne     .L2
        mov     eax, 0
        jmp     .L3
.L2:
        mov     BYTE PTR [rbp-109], 82
        mov     BYTE PTR [rbp-108], 123
        mov     BYTE PTR [rbp-107], 109
        mov     BYTE PTR [rbp-106], 52
        mov     BYTE PTR [rbp-105], 53
        mov     BYTE PTR [rbp-104], 116
        mov     BYTE PTR [rbp-103], 51
        movzx   eax, BYTE PTR [rbp-103]
        cmp     al, 101
        jne     .L4
        mov     BYTE PTR [rbp-103], 51
.L4:
        mov     BYTE PTR [rbp-102], 114
        mov     BYTE PTR [rbp-101], 95
        mov     BYTE PTR [rbp-100], 97
        mov     BYTE PTR [rbp-99], 53
        mov     BYTE PTR [rbp-98], 53
        movzx   eax, BYTE PTR [rbp-98]
        cmp     al, 87
        jne     .L5
        mov     BYTE PTR [rbp-97], 48
.L5:
        mov     BYTE PTR [rbp-97], 51
        mov     BYTE PTR [rbp-96], 109
        mov     BYTE PTR [rbp-95], 98
        mov     BYTE PTR [rbp-95], 108
        mov     BYTE PTR [rbp-95], 121
        mov     BYTE PTR [rbp-95], 125
        mov     eax, 0
.L3:
        pop     rbp
        ret
