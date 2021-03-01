%use masm
section .text
global _start
main:
  push   rbp
  mov    rbp, rsp
  mov    DWORD PTR [rbp-0x4], 0xc
  shl    DWORD PTR [rbp-0x4], 0xa
  sar    DWORD PTR [rbp-0x4], 0x5
  add    DWORD PTR [rbp-0x4], 0xa
  sub    DWORD PTR [rbp-0x4], 0xc2
  cmp    DWORD PTR [rbp-0x4], 0x190
  jg     0x2d
  add    DWORD PTR [rbp-0x4], 0x1
  jmp    0x1e
  sar    DWORD PTR [rbp-0x4], 0x2
  cmp    DWORD PTR [rbp-0x4], 0xff
  jg     0x40
  add    DWORD PTR [rbp-0x4], 0x1
  jmp    0x31
  cmp    DWORD PTR [rbp-0x4], 0x100
  jne    0xa3
  add    DWORD PTR [rbp-0x4], 0x1
  sub    DWORD PTR [rbp-0x4], 0x1
  add    DWORD PTR [rbp-0x4], 0x1
  sub    DWORD PTR [rbp-0x4], 0x1
  mov    eax, DWORD PTR [rbp-0x4]
  imul   eax, eax, 0x1a
  mov    DWORD PTR [rbp-0x4], eax
  mov    eax, DWORD PTR [rbp-0x4]
  imul   eax, eax, 0x368
  mov    DWORD PTR [rbp-0x4], eax
  mov    eax, DWORD PTR [rbp-0x4]
  imul   eax, eax, 0x9210a4
  mov    DWORD PTR [rbp-0x4], eax
  mov    eax, DWORD PTR [rbp-0x4]
  imul   eax, eax, 0x9210a4
  mov    DWORD PTR [rbp-0x4], eax
  mov    eax, DWORD PTR [rbp-0x4]
  imul   eax, eax, 0x9210a4
  mov    DWORD PTR [rbp-0x4], eax
  mov    eax, DWORD PTR [rbp-0x4]
  imul   eax, eax, 0x9210a4
  mov    DWORD PTR [rbp-0x4], eax
  mov    eax, DWORD PTR [rbp-0x4]
  jmp    0x11c
  add    DWORD PTR [rbp-0x4], 0x1
  mov    edx, DWORD PTR [rbp-0x4]
  mov    eax, edx
  shl    eax, 0x2
  add    eax, edx
  add    eax, eax
  mov    DWORD PTR [rbp-0x4], eax
  mov    eax, DWORD PTR [rbp-0x4]
  movsxd rdx, eax
  imul   rdx, rdx, 0x66666667
  shr    rdx, 0x20
  sar    edx, 0x2
  sar    eax, 0x1f
  mov    ecx, eax
  mov    eax, edx
  sub    eax, ecx
  mov    DWORD PTR [rbp-0x4], eax
  sar    DWORD PTR [rbp-0x4], 0xa
  mov    edx, DWORD PTR [rbp-0x4]
  movsxd rax, edx
  imul   rax, rax, 0x66666667
  shr    rax, 0x20
  sar    eax, 0x2
  mov    esi, edx
  sar    esi, 0x1f
  sub    eax, esi
  mov    ecx, eax
  mov    eax, ecx
  shl    eax, 0x2
  add    eax, ecx
  add    eax, eax
  sub    edx, eax
  mov    DWORD PTR [rbp-0x4], edx
  add    DWORD PTR [rbp-0x4], 0xa
  sub    DWORD PTR [rbp-0x4], 0xff
  mov    eax, DWORD PTR [rbp-0x4]
  imul   eax, eax, 0x64
  mov    DWORD PTR [rbp-0x4], eax
  mov    eax, DWORD PTR [rbp-0x4]
  pop    rbp
  ret    
