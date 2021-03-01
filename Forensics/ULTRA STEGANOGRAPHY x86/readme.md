Mimin diberi sebuah soal berupa file stegano feat reversing. dan di dalam file tersebut ada pesan tersembunyi yang harus di dapatkan. BTW ini bukan soal full reversing ya, tetapi soal Stegano/Forensic gitulah. semangat mencari!

Tools:
https://blog.yossarian.net/2020/08/16/Hiding-messages-in-x86-binaries-using-semantic-duals

```
curl https://sh.rustup.rs -sSf | sh
cargo install steg86
steg86 extract CTFR.flag
```

Flag
```
CTFR{St3gan0_r4s4_r3vers1ng_guy$}
```