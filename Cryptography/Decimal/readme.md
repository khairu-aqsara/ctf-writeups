Sistem bilangan desimal/persepuluhan adalah sistem bilangan yang menggunakan 10 macam angka dari 0,1, sampai 9. Setelah angka 9, angka berikutnya adalah 1 1, 1 2, dan seterusnya.

```
Flag : 67 84 70 82 123 52 115 99 49 49 95 99 48 100 51 125
```

Tools 
https://gchq.github.io/

Python Code

```
c= "67 84 70 82 123 52 115 99 49 49 95 99 48 100 51 125"
c = c.split(" ")
print(''.join([chr(int(x)) for x in c]))
```

Flag 

```
CTFR{4sc11_c0d3}
```