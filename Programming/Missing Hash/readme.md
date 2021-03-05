Mimin lupa password hash mimin, bisa bantu carikan gakk :(.

Target SHA1 : e5e3a99270135d6af8cb2d671fb70db31abf50e2
Missing MD5 : e5a4601548?3e753eb?a6a484a?87c0?
Flag : CTFR{MD5}

```
import hashlib, string
charset = string.digits + string.ascii_lowercase
sha1 = 'e5e3a99270135d6af8cb2d671fb70db31abf50e2'
md5 = "e5a4601548{}3e753eb{}a6a484a{}87c0{}"

for a in charset:
  for b in charset:
    for c in charset:
      for d in charset:
        target = md5.format(a, b, c, d)
        if hashlib.sha1(flag.encode()).hexdigest() == sha1:
          print(flag)
          break

```

Flag 
```
CTFR{e5a4601548b3e753eb6a6a484af87c03}
```

