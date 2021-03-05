Selama pandemi covid-19 kita harus menjaga kesehatan dan selalu cuci tangan.

Hint:
Karakter ke 1 sampai 19 adalah : Jaga kesehatan dan

```
encrypted = "J`e^\x1cf_l]_WiUa\x12UQ]\x0esdj^hp\x1a\\mZ_\x15hT`XQ]\x0eumrrg\x1bg^fZ[\\U[\x12aU]gea_o]i\x1a<gm_Y!$+\x11iPOh-\x1e?pr\x1am``i\x15]f\x12j_d` ej^c\x1b4\x19;K<GoV&c#Ng0tp\\o.f_W+dYS'^h$ha_bs`-Zn-f^*cq!\x12=_eS sml\x1cn_^\x18`j\x15Vhf\x11]PYe\x1fwlqm\x1afaeZ\x15[_ah\x10d^"
```

Code 
```
# Dari judul ini modulo 19
flag = ''
for i in range(len(encrypted)):
  flag+=chr(ord(encrypted[i]) + (i % 19))
print(flag)
```

Flag 

```
CTFR{c4r3_y0ur_s3lf_4nd_4lw4ys_cuc1_t4ng4n}
```