import hashlib

flag = [28991082358309069L, 36347028628327788L, 30289190523606490L, 35481623184796174L, 53222434777194261L, 43270272176580700L, 21202433366524543L, 47597299394238770L, 20769730644758736L, 49760813003067805L, 20769730644758736L, 50626218446599419L, 49328110281301998L, 50626218446599419L, 22933244253587771L, 41106758567751665L, 47597299394238770L, 52357029333662647L, 22500541531821964L, 41106758567751665L, 46731893950707156L, 22500541531821964L, 44568380341878121L, 21202433366524543L, 41106758567751665L, 47597299394238770L, 24664055140650999L, 22067838810056157L, 45866488507175542L, 22500541531821964L, 49328110281301998L, 41106758567751665L, 42404866733049086L, 50626218446599419L, 49328110281301998L, 50626218446599419L, 47597299394238770L, 24664055140650999L, 41106758567751665L, 45001083063643928L, 22067838810056157L, 45001083063643928L, 22067838810056157L, 54087840220725875L]
dino = open("Dino.jpg", "r").read()

def hexConv(x):
	res = ""
	for i in x: res += hex(ord(i)).replace("0x", "")
	return int(res, 16)

def getMd5():
	md5 = hashlib.md5()
	d = open("Dino.jpg", "r").read()
	md5.update(d)
	return md5.hexdigest()

def getSign():
	return dino[0: 4]

getSize = 14591788 — (10 ** 5–7725 + 65537 + (~80) + (462210 / 2))

md5 = hexConv(getMd5()) >> 0xCD

getWave = getSize / ord('C')

key = int(hexConv(getSign())) + int(hexConv(getSize) + getWave + md5)

print("".join([chr(int(f/key)) for f in flag]))
