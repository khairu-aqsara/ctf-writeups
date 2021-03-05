with open('apple.txt', 'r') as f:
	str1 = f.read()
	with open('coconut.txt', 'r') as f:
		str2 = f.read()

	maxlen=len(str2) if len(str1)<len(str2) else len(str1)
	result1=''
	result2=''

	for i in range(maxlen):
	  letter1=str1[i:i+1]
	  letter2=str2[i:i+1]
	  if letter1 != letter2:
	    result1+=letter1

	print(result1)