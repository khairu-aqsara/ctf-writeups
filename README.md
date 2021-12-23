# ctf-writeups
CTF Writeups

## Docker Images
```
docker pull wenkhairu/ctf-playground
docker run --cap-add=SYS_PTRACE  --privileged --pid=host --name=ctf-box -d -i wenkhairu/ctf-playground
```

##
```
# disable ASLR
echo 0  > /proc/sys/kernel/randomize_va_space 
# enable ASLR
echo 2  > /proc/sys/kernel/randomize_va_space
```
