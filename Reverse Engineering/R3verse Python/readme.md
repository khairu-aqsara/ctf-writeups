Python juga dapat di compile seperti Bahasa C++ atau lainnya. Dan tentunya dapat di Reverse, Nah coba dibuat ulang hasil disassemble ini menggunakan Python 3

Download : https://mega.nz/#!ElpwCD7Z!XrxtVkDn2h-zpmH-w_Kr67aN3L3Ftf2NCCcj9wbFxYk

Python Opcode

```asm
Disassembly of CreateKey:
  8           0 LOAD_CONST               1 (16)
              2 RETURN_VALUE

Disassembly of Decrypt:
 16           0 LOAD_CONST               1 ('')
              2 STORE_FAST               2 (res)

 17           4 LOAD_GLOBAL              0 (range)
              6 LOAD_GLOBAL              1 (len)
              8 LOAD_FAST                1 (target)
             10 CALL_FUNCTION            1
             12 CALL_FUNCTION            1
             14 GET_ITER
        >>   16 FOR_ITER                36 (to 54)
             18 STORE_FAST               3 (x)

 18          20 LOAD_FAST                2 (res)
             22 LOAD_GLOBAL              2 (chr)
             24 LOAD_FAST                3 (x)
             26 LOAD_GLOBAL              3 (ord)
             28 LOAD_FAST                1 (target)
             30 LOAD_FAST                3 (x)
             32 BINARY_SUBSCR
             34 CALL_FUNCTION            1
             36 BINARY_ADD
             38 LOAD_FAST                0 (self)
             40 LOAD_METHOD              4 (CreateKey)
             42 CALL_METHOD              0
             44 BINARY_XOR
             46 CALL_FUNCTION            1
             48 INPLACE_ADD
             50 STORE_FAST               2 (res)
             52 JUMP_ABSOLUTE           16

 19     >>   54 LOAD_FAST                2 (res)
             56 RETURN_VALUE

Disassembly of Encrypt:
 10           0 LOAD_FAST                0 (self)
              2 LOAD_ATTR                0 (text)
              4 STORE_FAST               1 (target)

 11           6 LOAD_CONST               1 ('')
              8 STORE_FAST               2 (res)

 12          10 LOAD_GLOBAL              1 (range)
             12 LOAD_GLOBAL              2 (len)
             14 LOAD_FAST                1 (target)
             16 CALL_FUNCTION            1
             18 CALL_FUNCTION            1
             20 GET_ITER
        >>   22 FOR_ITER                36 (to 60)
             24 STORE_FAST               3 (x)

 13          26 LOAD_FAST                2 (res)
             28 LOAD_GLOBAL              3 (chr)
             30 LOAD_GLOBAL              4 (ord)
             32 LOAD_FAST                1 (target)
             34 LOAD_FAST                3 (x)
             36 BINARY_SUBSCR
             38 CALL_FUNCTION            1
             40 LOAD_FAST                0 (self)
             42 LOAD_METHOD              5 (CreateKey)
             44 CALL_METHOD              0
             46 BINARY_XOR
             48 LOAD_FAST                3 (x)
             50 BINARY_SUBTRACT
             52 CALL_FUNCTION            1
             54 INPLACE_ADD
             56 STORE_FAST               2 (res)
             58 JUMP_ABSOLUTE           22

 14     >>   60 LOAD_FAST                2 (res)
             62 RETURN_VALUE

Disassembly of __init__:
  6           0 LOAD_FAST                1 (text)
              2 LOAD_FAST                0 (self)
              4 STORE_ATTR               0 (text)
              6 LOAD_CONST               0 (None)
              8 RETURN_VALUE

None
```

Buat Python berdasarkan Opcode

```python
import dis

class Chal():
    def __init__(self):
        self.text = 'SCT?g]'
        
    def CreateKey(self):
        return 16
    
    def Decrypt(self,target):
        res = ''
        for x in range(len(target)):
            res += chr((x + ord(target[x])) ^ self.CreateKey())
        return res
    
    def Encrypt(self):
        target = self.text
        res = ''
        for x in range(len(target)):
            res += chr((ord(target[x]) ^ self.CreateKey()) - x)
        return res

dis.dis(Chal.Decrypt)
```

Reverse

```python
with open('encrypted.txt', 'r') as f:
    fs = f.read()
    a = Chal()
    print(a.Decrypt(fs))
```

Flag

```
CTFR{r3v3rs3_pyth0n_1s_34sy_r1ght???}
```

