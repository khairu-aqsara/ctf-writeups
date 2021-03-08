Belum pernah mendengar kalo .NET bisa di Obfuscate ? Nah klo blum ini pertama kalinya kalian mendengar. Saran dari mimin selesaikan challenge pertama kemudian yang ke-2 karena challenge ini akan membuat brain-damage klo tidak tau cara pemakaian decompilernya.

Download : https://mega.nz/#!V5hiBIwT!eOTz99UBvLdn6WHxyPhio1V52cIblyCgZgb2Gx0vfCA


Tools : 
https://github.com/khairu-aqsara/de4dot/actions/runs/632671809
https://devextras.com/decompiler/

Step :
1. Deobuscator File Obfuscate.NET.exe `de4dot-x64.exe Obfuscate.NET.exe`
2. Decompiler Dengan CodeReflect

```
private static void Main(string[] args)
{
    "CTFR{y0u_c4n_b34t_0bfu5c4t3_d0t_n3t???}";
    Console.WriteLine("Welcome CTFR");
    Console.WriteLine("Your flag is somewhere in this application");
    Console.ReadLine();
}
```

Flag

```
CTFR{y0u_c4n_b34t_0bfu5c4t3_d0t_n3t???}
```
