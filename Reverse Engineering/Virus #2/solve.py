from flag import P,C,K

tes_k = [k >> 10 for k in K]

C = str(C)

tes_c = []
for x in tes_k:
	tes_c.append(int(C[:x]))
	C = C[x:]

for f in tes_c:
	for j in range(30,127):
		kunci = 0
		for i in range(0x739):
			if ((j * P[i] + P[i]) & 1 == 0):
				kunci+=1
		a = kunci * 0x10 * j
		b = a >> 0x1f
		fl = (a ^ b) - b
		if fl == f:
			print(chr(j), end='')
			break
