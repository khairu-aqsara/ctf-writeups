Untuk mendapatkan informasi tentang ulat bulu pada program ini kalian harus membeli lisensi nya, Coba bantu mimin bypass lisensi nya dong.

Download : https://mega.nz/#!R1pGWSSa!FQVnjI6KOgqt7gGyzsS0EsMf1iWPD2CGrASXrEg0Nmk

```asm
...
0x00000000000010c4 <+100>:   call   0x1040 <strlen@plt>
0x00000000000010c9 <+105>:   cmp    rax,0x23
0x00000000000010cd <+109>:   je     0x10f7 <main+151>
...
```

dari potongan code assembler, panjang flagnya `0x23` dalam hexadesimal atau `35` karakter dalam desimal,dicoba masukin sembarang karakter dengan panjang `0x23` hasilnya

```bash
Selamat datang di Aplikasi Ulat Bulu
Aplikasi ini berguna untuk anda agar dapat mendapatkan informasi tentang ulat bulut
Akan tetapi aplikasi ini berbayar, silahkan masukan key melewati argument pada aplikasi ini
Ulat adalah tahap larva dari anggota ordo Lepidoptera. Seperti kebanyakan penamaan umum, penggunaan istilah ini sebenarnya tidak konsisten, sebab larva lalat gergaji juga sering disebut sebagai ulat. Baik larva lepidopteran maupun larva symphytan sama-sama memiliki bentuk tubuh eruciform.
CTFR{c0ngr4t5_f0r_f1n15h_th15_ch4ll3ng3}
```

Setelah konfirmasi sama yang buat emang gitu ternyata.

Flag

```
CTFR{c0ngr4t5_f0r_f1n15h_th15_ch4ll3ng3}
```