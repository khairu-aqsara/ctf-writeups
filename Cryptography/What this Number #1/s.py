deci = "255465504989093787248104537982969745474445259944896331123851542522026611778579085886"
hexa = "21AA23293DBA3419AFB318B91ABA2F983719AFBB9A1AAF9AB418B33A2FB9189CB43A3E"
hexa = binascii.unhexlify(hexa)
for c in hexa:
  print(c, end=' ')

print("\n")

def shift(s, n):
     return ( s + n ) % 256

shif_kali_dua = [33,61,62,25,175,26,24,47,187,156]
kali = [170,35,41,186,52,179,185,152,55,154,180,58]

for x in hexa:
  if x in shif_kali_dua:
    c = shift(x * 2, 1)
  elif x in kali:
    c = (x * 2) % 256
  else:
    c = 0x41

  print(chr(c), end='')