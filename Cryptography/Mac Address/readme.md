Sebuah hacker mengambil Mac Address dari komputer korbannya, mereka mengatakan bahwa ada rahasia dari Mac Address tersebut , Coba bantu cari tau dong...

Download : https://mega.nz/#!gxwy1JDa!xHYmT9Ooa8NagprklupYAv_JEmuNGswGcKW5R0Ow9gk

code
```
import binascii

with open('result_mac_hacker.txt','r') as f:
    line = f.readlines()
    flag1 = []
    flag2 = []
    flag3 = []
    flag4 = []
    flag5 = []
    flag6 = []
    
    baris = 0
    for l in line:
        if baris % 4 == 0:
            l = l.strip()
            flag1.append(binascii.unhexlify(l[:2]).decode('latin'))
            flag2.append(binascii.unhexlify(l[3:5]).decode('latin'))
            flag3.append(binascii.unhexlify(l[6:8]).decode('latin'))
            flag4.append(binascii.unhexlify(l[9:11]).decode('latin'))
            flag5.append(binascii.unhexlify(l[12:14]).decode('latin'))
            flag6.append(binascii.unhexlify(l[15:17]).decode('latin'))
        baris+=1
        
        
    print(''.join([x for x in flag1[:-1]]))
    print("-------------------------------")
    print(''.join([x for x in flag2[:-1]]))
    print("-------------------------------")
    print(''.join([x for x in flag3[:-1]]))
    print("-------------------------------")
    print(''.join([x for x in flag4[:-1]]))
    print("-------------------------------")
    print(''.join([x for x in flag5[:-1]]))
    print("-------------------------------")
    print(''.join([x for x in flag6[:-1]]))
```


Flag:
```
CTFR{ju5t_r4nd0m_m4c_4ddr355}
```