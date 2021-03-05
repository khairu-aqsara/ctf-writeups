#!/home/kulikode/.pyenv/shims/python2

import random

encrypted = open("encrypt.txt", "r").read()

flag = ""
random.seed("CTFR")
for x in encrypted:
    flag += chr(ord(x) - random.randrange(0, 15))

print flag