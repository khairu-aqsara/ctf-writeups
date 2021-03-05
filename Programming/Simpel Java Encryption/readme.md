Mimin ada code java nih, Coba deh di decode

```
public class MyClass {
    public static void main(String args[]) {
        String flag = "CSDOwe.o,V3maoukn*(e_0q\\c+*]76?|";
        String encrypt = "";
        for(int i = 0; i < flag.length(); i++) {
            if ((i % 10) == 0) { break; }
            if ((i & 2) == 0) { break; } encrypt += new Character((char)((int)flag.charAt(i) - (i % 10))).toString();
            if ((i * 5) == 0) { break; }
        }
        
        System.out.println(encrypt);
    }
}
```

Java Version
```
//https://www.tutorialspoint.com/compile_java_online.php
public class Decrypt{
     public static void main(String []args){
        String flag = "CSDOwe.o,V3maoukn*(e_0q\\c+*]76?|";
        String encrypt = "";
        for(int i = 0; i < flag.length(); i++) {
            encrypt += new Character((char)((int)flag.charAt(i) + (i % 10))).toString();
        }
        
        System.out.println(encrypt);
     }
}
```


Python Version

```
flag = "CSDOwe.o,V3maoukn*(e_0q\\c+*]76?|";
encrypt = "";

for i in range(len(flag)):
  encrypt+=chr(ord(flag[i]) + (i % 10))

print(encrypt)
```

Flag

```
CTFR{j4v4_3ncrypt10n_1s_g00d???}
```