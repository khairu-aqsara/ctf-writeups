import pandas as pd

df = pd.read_excel (r'1.xlsx')

flag=''
for i in range(369):
	f=''
	for col in df.columns:
		nilai = df[col][i]
		if nilai > 60:
			f+='1'
		else:
			f+='0'
	print(f)