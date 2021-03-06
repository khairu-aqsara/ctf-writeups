Sesuai dengan namanya, mimin diberikan sebuah teks titik-titik yang sangat banyak sekali :(. Kalian bisa bantu cari tau arti dari titik titik itu kan...

Download : https://mega.nz/#!U1ZnUQiJ!8HEzYdSdVUHJ1ZNWLU4qxOF6qsiimLJheNmwfGG2ml0

```
with open('dot.txt', 'r') as fs:
	string_dot = fs.read()

	flag = []
	num = 0
	for i in string_dot:
		if i == ".":
			num+=1
		elif i == " ":
			flag.append(num)
			num = 0

	print("".join([chr(x) for x in flag]))
```

Atau

```
with open('dot.txt', 'r') as f:
    p = [line.rstrip() for line in f][0]
    string ="".join([chr(len(x)) for x in  p.split()])
    print(string, end='')
```

Flag

```
CTFR{b154_d1l1h4t_d4r1_juml4h_d0t_d0t_t3r53but_4d4l4h_4sc11_ch4r4ct3r}
```