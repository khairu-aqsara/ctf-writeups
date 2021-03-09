Sebuah program yang melakukan enkripsi terhadap plaintext, termasuk special character seperti _{}#@! dan lain-lain. Cari tau bagaimana enkripsi nya di buat

Download : https://mega.nz/#!c4oDXApZ!ERS_s_PrEZdB5gjIpwgDtbBjADmOlL3mo88Kj4LyCyM

Run

```
-= Welcome to CTFR Virus #2 =-
-= Like the old day, Initialize... =-
-= Generate Key =-
-= Encrypting... =-
-= Your data has been encrypted! =-
```

kalo dilihat-lihat hasil encrypt hampir mirip dengan file flag.txt

Pseudo Code dari main

```C
undefined8 main(void)

{
  time_t tVar1;
  
  tVar1 = time((time_t *)0x0);
  srand((uint)tVar1);
  curl = curl_easy_init();
  if (curl == 0) {
    puts("Some library not initialize sucessfully! Try to contact administrator.");
  }
  else {
    puts("-= Welcome to CTFR Virus #2 =-");
    puts("-= Like the old day, Initialize... =-");
    sleep(2000);
    exec();
  }
  return 0;
}
```

Pseudo Code dari fungsi exec

```C
void exec(void)

{
  int iVar1;
  ulong uVar2;
  long lVar3;
  ulong uVar4;
  long lVar5;
  basic_string<char,std::char_traits<char>,std::allocator<char>> local_328 [32];
  basic_string<char,std::char_traits<char>,std::allocator<char>> local_308 [32];
  basic_string<char,std::char_traits<char>,std::allocator<char>> local_2e8 [32];
  basic_string<char,std::char_traits<char>,std::allocator<char>> local_2c8 [32];
  basic_string<char,std::char_traits<char>,std::allocator<char>> local_2a8 [47];
  allocator<char> local_279;
  basic_string local_278 [46];
  allocator<char> local_24a;
  allocator<char> local_249;
  __cxx11 local_248 [32];
  basic_string local_228 [32];
  __cxx11 local_208 [47];
  allocator<char> local_1d9;
  __cxx11 local_1d8 [32];
  __cxx11 local_1b8 [32];
  basic_string local_198 [32];
  __cxx11 local_178 [47];
  allocator<char> local_149;
  basic_string local_148 [32];
  basic_string<char,std::char_traits<char>,std::allocator<char>> local_128 [32];
  basic_string local_108 [32];
  basic_string<char,std::char_traits<char>,std::allocator<char>> local_e8 [32];
  basic_string local_c8 [32];
  basic_string<char,std::char_traits<char>,std::allocator<char>> local_a8 [32];
  basic_string local_88 [32];
  basic_string<char,std::char_traits<char>,std::allocator<char>> local_68 [39];
  allocator<char> local_41;
  long local_40;
  int *local_38;
  int *local_30;
  int local_24;
  int local_20;
  int local_1c;
  
  local_30 = (int *)g(0x739);
  puts("-= Generate Key =-");
  sleep(1000);
  puts("-= Encrypting... =-");
  sleep(1000);
  std::allocator<char>::allocator();
                    /* try { // try from 00102834 to 00102838 has its CatchHandler @ 00102e56 */
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string
            ((char *)local_2a8,(allocator *)"CTFR{th15_3ncrypt10n_15_aw3s0m3_r19ht}");
  std::allocator<char>::~allocator(&local_279);
                    /* try { // try from 0010285c to 00102860 has its CatchHandler @ 00103075 */
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string
            (local_278);
                    /* try { // try from 00102872 to 00102876 has its CatchHandler @ 00102e73 */
  local_38 = (int *)c(local_30,(basic_string)0x88);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
            ((basic_string<char,std::char_traits<char>,std::allocator<char>> *)local_278);
  iVar1 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::size();
                    /* try { // try from 001028a4 to 001028a8 has its CatchHandler @ 00103075 */
  local_40 = sk(local_38,iVar1);
  std::allocator<char>::allocator();
                    /* try { // try from 001028d4 to 001028d8 has its CatchHandler @ 00102e8a */
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string
            ((char *)local_2c8,(allocator *)&DAT_00104067);
  std::allocator<char>::~allocator(&local_24a);
  std::allocator<char>::allocator();
                    /* try { // try from 0010290f to 00102913 has its CatchHandler @ 00102ea1 */
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string
            ((char *)local_2e8,(allocator *)&DAT_00104067);
  std::allocator<char>::~allocator(&local_249);
  local_1c = 0;
  while( true ) {
    uVar4 = SEXT48(local_1c);
    uVar2 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::size();
    if (uVar2 <= uVar4) break;
    lVar5 = (long)local_1c;
    lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::size();
    if (lVar5 == lVar3 + -1) {
                    /* try { // try from 00102992 to 00102996 has its CatchHandler @ 00103052 */
      std::__cxx11::to_string(local_248,*(int *)(local_40 + (long)local_1c * 4));
                    /* try { // try from 001029ab to 001029af has its CatchHandler @ 00102eb8 */
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=
                (local_2c8,(basic_string *)local_248);
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
                ((basic_string<char,std::char_traits<char>,std::allocator<char>> *)local_248);
    }
    else {
                    /* try { // try from 001029e3 to 001029e7 has its CatchHandler @ 00103052 */
      std::__cxx11::to_string(local_208,*(int *)(local_40 + (long)local_1c * 4));
                    /* try { // try from 00102a03 to 00102a07 has its CatchHandler @ 00102ee3 */
      std::operator+(local_228,(char *)local_208);
                    /* try { // try from 00102a1c to 00102a20 has its CatchHandler @ 00102ecf */
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=
                (local_2c8,local_228);
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
                ((basic_string<char,std::char_traits<char>,std::allocator<char>> *)local_228);
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
                ((basic_string<char,std::char_traits<char>,std::allocator<char>> *)local_208);
    }
    local_1c = local_1c + 1;
  }
  std::allocator<char>::allocator();
                    /* try { // try from 00102a6f to 00102a73 has its CatchHandler @ 00102efa */
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string
            ((char *)local_308,(allocator *)&DAT_00104067);
  std::allocator<char>::~allocator(&local_1d9);
  local_20 = 0;
  while( true ) {
    uVar4 = SEXT48(local_20);
    uVar2 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::size();
    if (uVar2 <= uVar4) break;
                    /* try { // try from 00102acb to 00102acf has its CatchHandler @ 0010303e */
    std::__cxx11::to_string(local_1d8,local_38[local_20]);
                    /* try { // try from 00102ae4 to 00102ae8 has its CatchHandler @ 00102f11 */
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=
              (local_308,(basic_string *)local_1d8);
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
              ((basic_string<char,std::char_traits<char>,std::allocator<char>> *)local_1d8);
    local_20 = local_20 + 1;
  }
  local_24 = 0;
  while (local_24 < 0x739) {
    if (local_24 == 0x738) {
                    /* try { // try from 00102b3d to 00102b41 has its CatchHandler @ 0010303e */
      std::__cxx11::to_string(local_1b8,local_30[0x738]);
                    /* try { // try from 00102b56 to 00102b5a has its CatchHandler @ 00102f28 */
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=
                (local_2e8,(basic_string *)local_1b8);
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
                ((basic_string<char,std::char_traits<char>,std::allocator<char>> *)local_1b8);
    }
    else {
                    /* try { // try from 00102b8e to 00102b92 has its CatchHandler @ 0010303e */
      std::__cxx11::to_string(local_178,local_30[local_24]);
                    /* try { // try from 00102bae to 00102bb2 has its CatchHandler @ 00102f53 */
      std::operator+(local_198,(char *)local_178);
                    /* try { // try from 00102bc7 to 00102bcb has its CatchHandler @ 00102f3f */
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=
                (local_2e8,local_198);
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
                ((basic_string<char,std::char_traits<char>,std::allocator<char>> *)local_198);
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
                ((basic_string<char,std::char_traits<char>,std::allocator<char>> *)local_178);
    }
    local_24 = local_24 + 1;
  }
  std::allocator<char>::allocator();
                    /* try { // try from 00102c1a to 00102c1e has its CatchHandler @ 00102f6a */
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string
            ((char *)local_328,(allocator *)&DAT_00104067);
  std::allocator<char>::~allocator(&local_149);
                    /* try { // try from 00102c46 to 00102c4a has its CatchHandler @ 0010302a */
  std::operator+((char *)local_128,(basic_string *)&DAT_0010406a);
                    /* try { // try from 00102c66 to 00102c6a has its CatchHandler @ 00102f95 */
  std::operator+(local_148,(char *)local_128);
                    /* try { // try from 00102c7f to 00102c83 has its CatchHandler @ 00102f81 */
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=
            (local_328,local_148);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
            ((basic_string<char,std::char_traits<char>,std::allocator<char>> *)local_148);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
            (local_128);
                    /* try { // try from 00102cba to 00102cbe has its CatchHandler @ 0010302a */
  std::operator+((char *)local_e8,(basic_string *)&DAT_00104071);
                    /* try { // try from 00102cda to 00102cde has its CatchHandler @ 00102fc0 */
  std::operator+(local_108,(char *)local_e8);
                    /* try { // try from 00102cf3 to 00102cf7 has its CatchHandler @ 00102fac */
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=
            (local_328,local_108);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
            ((basic_string<char,std::char_traits<char>,std::allocator<char>> *)local_108);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
            (local_e8);
                    /* try { // try from 00102d2e to 00102d32 has its CatchHandler @ 0010302a */
  std::operator+((char *)local_a8,(basic_string *)&DAT_00104076);
                    /* try { // try from 00102d4e to 00102d52 has its CatchHandler @ 00102fe8 */
  std::operator+(local_c8,(char *)local_a8);
                    /* try { // try from 00102d67 to 00102d6b has its CatchHandler @ 00102fd4 */
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=
            (local_328,local_c8);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
            ((basic_string<char,std::char_traits<char>,std::allocator<char>> *)local_c8);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
            (local_a8);
                    /* try { // try from 00102d9b to 00102d9f has its CatchHandler @ 0010302a */
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string
            (local_88);
  std::allocator<char>::allocator();
                    /* try { // try from 00102dbe to 00102dc2 has its CatchHandler @ 0010300d */
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string
            ((char *)local_68,(allocator *)"encrypted.txt");
                    /* try { // try from 00102dd1 to 00102dd5 has its CatchHandler @ 00102ffc */
  s((basic_string)0x98,(basic_string)0x78);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
            (local_68);
  std::allocator<char>::~allocator(&local_41);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
            ((basic_string<char,std::char_traits<char>,std::allocator<char>> *)local_88);
                    /* try { // try from 00102e01 to 00102e05 has its CatchHandler @ 0010302a */
  puts("-= Your data has been encrypted! =-");
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
            (local_328);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
            (local_308);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
            (local_2e8);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
            (local_2c8);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
            (local_2a8);
  return;
}
```

variable `local_30`  = return value dari fungsi `g()` dengan parameter 0x739 = 1849, string `CTFR{th15_3ncrypt10n_15_aw3s0m3_r19ht}` di encrypt dan disimpan dalam file `encrypted.txt`  string ini akan dijadikan argumen kedua dari pemanggilan fungsi `c()` kemudian akan me-return hasil perhitungannya dalam `array void * hasil` 

fungsi `sk( )` di panggil di dalam fungsi `exec()` dengan 2 argumen argumen pertama adalah return dari fungsi `c()` dan argumen ke dua panjang flag, dalam perulangan fungsi `sk()` array dari fungsi `c()` akan di `shift left 10` ini merupakan hasil `K=` dalam file `flag.txt` dan `encrypted.txt` 

```python
from encrypted import P,C,K

print([k >> 10 for k in K]) # kebalikan dari shift left <<
```

hasilnya

```
[7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7]
```

Coba Decrypt file `encrypted.txt` (rename jadi `encrypted.py` dan jadikan `P` dan `K` sebagai Array)

```python
from encrypted import P,C,K

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
```

hasilnya 

```
CTFR{th15_3ncrypt10n_15_aw3s0m3_r19ht}
```

Coba Decrypt `flag.txt` (rename jadi `flag.py` dan jadikan `P` dan `K` sebagai Array)

```python
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

```

hasilnya

```
m_3b_ll1w_u0y_n005{RFTC}r3l1pm0c3d_f0_r3t54
```

Flag

```
CTFR{y0u_w1ll_b3_m45t3r_d3c0mp1l3r}
```
