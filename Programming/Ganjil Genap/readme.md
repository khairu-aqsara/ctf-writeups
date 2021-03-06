Enkripsi menggunakan Angka Ganjil dan Genap, Silahkan di coba nih :D. Untuk cara enkripsi nya mimin sudah terapkan di Bagian filenya

Download : https://mega.nz/#!w5olAQzb!Zd6NS_zd5S2nX34DX732ogtVbc4dYVUjP5LMB27kn3k

Enkripsi

```
# Enkripsi :
# .**.*.*.*.**
# **.*.**.**
# *.**.*.*.**
# *.*.*.**.**
# .**.*****
# .**.*.***
# *.***.***
# .**.**.***
# *.*.*.****
# .*.*.*.***
# ****.***
# .*.**.***
# .*.*.*.***
# .*****.**
# .***.*.***
# **.*.***
# *.***.***
# *.*.**.***
# .*.*.*.***
# **.**.***
# .*****.**
# .***.*.***
# .**.*.***
# *.***.***
# **.*.***
# ****.***
# .*****.**
# .**.*.****
# .**.*.***
# *.*.*.****
# .*.**.****
# .*****.**
# .**.**.***
# **.*.***
# *.***.***
# .*.******

# Tata cara enkripsi :
# Setiap jumlah ascii yang memiliki sifat genap, maka hasil result bertambah "*". Kemudian di bagi 2
# hasil += "*"
# ascii = ascii / 2
# Sedangkan jika ascii memiliki sifat ganjil, maka hasil result bertambah ".". kemudian ditambah 1
# hasil += "."
# ascii = ascii + 1
# Hal tersebut di lakukan sampai nilai ASCII menjadi 1
# Contoh : 
# "C" akan menjadi ".**.*.*.*.**"
# "T" akan menjadi "*.***.***"
# "F" akan menjadi "*.**.*.*.**"
```

```
chars=[]
for x in range(48,126):
    hasil=''
    c=x
    while(c>1):
        if c > 1:
            if c % 2 == 0:
                hasil+='*'
                c=c/2
            else:
                hasil+='.'
                c=c+1
    chars.append({chr(x) : hasil})

desc=''

with open('enc.txt','r') as f:
    line = [ff.rstrip() for ff in f.readlines()]
    for enc in line:
        for keys in chars:
            key = [key for key, value in keys.iteritems() if value == enc]
            if len(key) > 0:
                desc+=key[0]
    
print desc
```

Flag
 
```
CTFR{3nkr1p51_g4nj1l_g3n4p_s3ru_k4n}
```
