Sebelumnya sudah mengenal yang namanya Encode dan Decode Yaah ? Sekarang masih sama, cuman jika kamu melihatnya challenge ini sebagai unik, maka pelajaran bagi anda :D.

```
Flag : TKWI{j3t0eu_wc4x_n4j_t1gy3i_k3ok}
```

Tools (Caesar Cipher):
https://cryptii.com/

Flag:

```
CTFR{s3c0nd_fl4g_w4s_c1ph3r_t3xt}
```

Python Code:

```
def rotate(txt, key):
	def cipher(i, low=range(97,123), upper=range(65,91)):
		if i in low or i in upper:
		  s = 65 if i in upper else 97
		  i = (i - s + key) % 26 + s
		return chr(i)
	return ''.join([cipher(ord(s)) for s in txt])


for x in range(26):
  flag = rotate('TKWI{j3t0eu_wc4x_n4j_t1gy3i_k3ok}', x)
  if 'CTFR' in flag:
    print(flag)
    break
```