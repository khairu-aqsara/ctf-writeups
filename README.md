# ctf-writeups
CTF Writeups

## Docker Images
```
docker pull wenkhairu/ctf-playground
docker run --rm -v ${PWD}:/playground --cap-add=SYS_PTRACE  --privileged --pid=host --name=ctf-box -d -i wenkhairu/ctf-playground
docker exec -it ctf-box /bin/bash
```

##
```
# disable ASLR
echo 0  > /proc/sys/kernel/randomize_va_space 
# enable ASLR
echo 2  > /proc/sys/kernel/randomize_va_space
```
