Perasaan mimin kemarin udah pintar yaa kalian bisa menjawab sains yang pertama, kali ini mimin ada soal sains #2 untuk kalian coba artikan.

Referensi
https://esolangs.org/wiki/DNA-Sharp

```
Command	Brainfuck equivalent	C-equivalent	Symbols for symbol form
ATAT	>	pointer++ / newpointer++ ***	>
ATGC	<	pointer-- / newpointer-- ***	<
ATTA	+		+
ATCG	-		-
GCAT	. (Output as ASCII)		.
GCGC	, (ASCII input)		,
GCTA	[		[
GCCG	]		]
TAAT *		*pointer = *newpointer	= or := ****
TAGC *		*pointer += *newpointer	+=
TATA *		*pointer -= *newpointer	-=
TACG *		*pointer *= *newpointer	*=
CGAT *		*pointer /= *newpointer	/=
CGGC		. (Output as integer value)	~
CGTA		, (Integer input)	?
CGCG		- (NOP)	X**
```

Decoded
```
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>---.>----------------.<+++.>--.+++++++++++++++++++++++++++++++++++++++++.<--.>-------------.<----------------.>---------------.++++++++++++++++++++.-----------.<<+++++.>>++++++++++.--.<++++++++++++++++++++.>-----------------.++++++++++++++.<<++++++++++++++.>>+++++++++++.<+++++++++++++++++++++++.+++.>------.<<+++.>+++++++.>----.<---.---.>---.++++++++++++++++++.
```

Tools
```
https://www.dcode.fr/brainfuck-language
```

Flag
```
CTFR{Dn4_sh#rpH_m1x_br4infck}
```