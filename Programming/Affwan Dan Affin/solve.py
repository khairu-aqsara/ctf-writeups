import string, binascii
from textwrap import wrap

karakter = string.printable

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None

    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def getKeyParts(key):
    keyA = key // len(karakter)
    keyB = key % len(karakter)
    return (keyA, keyB)

def decryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    plaintext = ''
    modInverseOfKeyA = findModInverse(keyA, len(karakter))

    for symbol in message:
        if symbol in karakter:
            symbolIndex = karakter.find(symbol)
            plaintext += karakter[(symbolIndex - keyB) * modInverseOfKeyA % len(karakter)]
        else:
            plaintext += symbol
    return plaintext


message = "2a412a58316a3d6a41265f413c2658263626612657583577772a416a58762a21576a5f58614e575d583d6552582a412a587761264a413c265876512971374142523e3c42723e0d4142523e5742523e6077774f412f3e7e4f21572f5f3e52425f0d78"
message = wrap(message, 2)

flag=''
for x in message:
  ch = chr(int(x, 16))
  flag+=ch

for key in range(len(karakter) ** 2):
	keyA = getKeyParts(key)[0]
	if gcd(keyA, len(karakter)) != 1:
		continue

	decryptedText = decryptMessage(key, flag)
	if 'CTFR' in decryptedText:
		print('Key: %s' % (key))
		print('Decrypted : ' + decryptedText)
		break
	else:
		print('Mencoba Key: %s' % (key))