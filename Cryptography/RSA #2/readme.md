Some Baby RSA Here. Selesaikan yaah :D

```
c = [54936, 44165, 43788, 47332, 23993, 26956, 27917, 26956, 54434, 29636, 39354, 29477, 27917, 29636, 12626, 27917, 29477, 29636, 9331, 27917, 29477, 54434, 29636, 9331, 22640, 45837, 33284, 19382, 41280, 39004, 39004, 39004, 31084]
n = 55189
e = 7
```

Python Code
```
#solve.py
from Crypto.Util.number import *
import math
import gmpy2

c = [54936, 44165, 43788, 47332, 23993, 26956, 27917, 26956, 54434, 29636, 39354, 29477, 27917, 29636, 12626, 27917, 29477, 29636, 9331, 27917, 29477, 54434, 29636, 9331, 22640, 45837, 33284, 19382, 41280, 39004, 39004, 39004, 31084]
n = 55189
e = 7

N = gmpy2.mpz(n)
gmpy2.get_context().precision = 2048
a = int(gmpy2.sqrt(N))
a2 = a * a
b2 = gmpy2.sub(a2, N)
while not (gmpy2.is_square(b2)):
    a = a + 1
    b2 = a * a - N
b2 = gmpy2.mpz(b2)
gmpy2.get_context().precision = 2048
b = int(gmpy2.sqrt(b2))

p = a + b
q = a - b

phi = (p - 1) * (q - 1)
d = inverse(e, phi)

flag = ''

for f in c:
	r = pow(f, d, n)
	flag+=chr(r)

print(flag)
```

Flag 

```
CTFR{b4by_r54_w45_345y_3n0ugh???}
```