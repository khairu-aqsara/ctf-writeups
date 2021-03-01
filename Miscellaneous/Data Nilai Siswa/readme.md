Sebuah file yang berisi data-data nilai siswa pada SMK TI. Nah saking banyaknya dapat tersebut, Guru-guru pada menyerah untuk menghitung Grade mereka, maksud dari Grade nya seperti A,B,C,D. Tapi guru tersebut memberikan isyarat jika nilai siswa dibawah 60 akan mendapatkan C alias Tidak Lulus (Jika dibawah 40 akan mendapatkan D), sedangkan jika diatas 60 dan dibawah 75 akan mendapatkan B. Jika nilai tersebut diatas 75 sampai 100 maka akan mendapatkan A. Selain C / D akan Lulus dari ujian tersebut.

Download : https://mega.nz/#!V8x3RA5R!EJMgyP9GupzWOvTs0DiunTPQRtkgc0FsHjPT43U7g-Q

Konversi Nilai Dari Kiri Kekanan terus lanjut ke baris berikutnya, hasilnya QrC0de


Python Code
```
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
```

Command
```
python solve.py > flag.txt
```

flag 

```
CTFR{qr_c0d3_1n_5pr34d5h33t_w45_4m4z1n9}
```