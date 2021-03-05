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