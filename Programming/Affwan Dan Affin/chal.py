import sys, string, binascii

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

def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit('Jika kunci A=1 Enkripsi terlalu lemah, silahkan pilih kunci lain')
    if keyB == 0 and mode == 'encrypt':
        sys.exit('Jika kunci B=0 Enkripsi terlalu lemah, silahkan pilih kunci lain')
    if keyA < 0 or keyB < 0 or keyB > len(karakter) - 1:
        sys.exit('Kunci A harus lebih besar dari 0 dan Kunci B harus berada diantara 0 dan %s.' % (len(karakter) - 1))
    if gcd(keyA, len(karakter)) != 1:
        sys.exit('Kunci A (%s) dengan jumlah karakter (%s) secara relative bukan angka prima. Pilih Kunci lain.' % (keyA, len(karakter)))

def encryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    ciphertext = ''
    for symbol in message:
        if symbol in karakter:
            symbolIndex = karakter.find(symbol)
            s = karakter[(symbolIndex * keyA + keyB) % len(karakter)]
            ciphertext += s
        else:
            ciphertext += symbol
    return binascii.hexlify(ciphertext.encode())

enc = encryptMessage(1990, "Halo Affwan")
print(enc)