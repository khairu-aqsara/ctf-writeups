Kalian pinter sains kan ? Coba bantu mimin artikan ini dong.

```
CTAACTAAAAGTAGTACAATCACGACATTGAGAATCAGATTGATAACAATCACGAAAATCAATCCAATCACGTTGGTAAAAAGAATCCAGTTGCATACAATCCATAAAATCACGTTGCTCGCTCGGTTGCTATTCAATACATTGCTTAGTAAAACGTTGTTGCTAGTCCTTGGT{ATATCAATATCAATC_TCGATCACGACGTCTAGG_ATTTCAATCCATTCGCAC_CAGTCTTCAATCTGA}TTGGTGAATAAAACTTTGAGACATCCATTGAAAAGCAAA
```

Info :
https://raw.githubusercontent.com/JohnHammond/ctf-katana/master/img/dna_codes.png

python Code

```
dna = {
    'AAA':'a',
    'AAC':'b',
    'AAG':'c',
    'AAT':'d',
    'ACA':'e',
    'ACC':'f',
    'ACG':'g',
    'ACT':'h',
    'AGA':'i',
    'AGC':'j',
    'AGG':'k',
    'AGT':'l',
    'ATA':'m',
    'ATC':'n',
    'ATG':'o',
    'ATT':'p',
    'CAA':'q',
    'CAC':'r',
    'CAG':'s',
    'CAT':'t',
    'CCA':'u',
    'CCC':'v',
    'CCG':'w',
    'CCT':'x',
    'CGA':'y',
    'CGC':'z',
    'CGG':'A',
    'CGT':'B',
    'CTA':'C',
    'CTC':'D',
    'CTG':'E',
    'CTT':'F',
    'GAA':'G',
    'GAC':'H',
    'GAG':'I',
    'GAT':'J',
    'GCA':'K',
    'GCC':'L',
    'GCG':'M',
    'GCT':'N',
    'GGA':'O',
    'GGC':'P',
    'GGG':'Q',
    'GGT':'R',
    'GTA':'S',
    'GTC':'T',
    'GTG':'U',
    'GTT':'V',
    'TAA':'W',
    'TAC':'X',
    'TAG':'Y',
    'TAT':'Z',
    'TCA':'1',
    'TCC':'2',
    'TCG':'3',
    'TCT':'4',
    'TGA':'5',
    'TGC':'6',
    'TGG':'7',
    'TGT':'8',
    'TTA':'9',
    'TTC':'0',
    'TTG':' ',
    'TTT':'.'
}

enc = "CTAACTAAAAGTAGTACAATCACGACATTGAGAATCAGATTGATAACAATCACGAAAATCAATCCAATCACGTTGGTAAAAAGAATCCAGTTGCATACAATCCATAAAATCACGTTGCTCGCTCGGTTGCTATTCAATACATTGCTTAGTAAAACGTTGTTGCTAGTCCTTGGT{ATATCAATATCAATC_TCGATCACGACGTCTAGG_ATTTCAATCCATTCGCAC_CAGTCTTCAATCTGA}TTGGTGAATAAAACTTTGAGACATCCATTGAAAAGCAAA"
enc = enc.replace("_","").replace("{","").replace("}","")
enc = [enc[i:i+3] for i in range(0, len(enc), 3)]


print("".join([dna[x] for x in enc]))

```

Flag
```
CTFR{m1m1n_3ngg4k_p1nt3r_s41n5}
```