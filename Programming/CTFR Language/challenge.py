import random

# Global Storage With 1024 Size
temp = [0 for x in range(1024)]
used = 0
def push(x):
    global used
    temp[used] = int(x)
    used += 1
    return temp[used - 1]
def up(x):
    return x ** 8
def mul(x):
    return x ** 2
def add(x, val):
    return x + val
def desc(x, val):
    return x - val
def ret(x):
    return x
def mov(x, val):
    temp[x] = val
    return temp[x]

data = {
    "\x10": push,
    "\x11": up,
    "\x12": mul,
    "\x13": add,
    "\x14": desc,
    "\x15": ret,
    "\x16": mov
}

def exe(val):
    res = 0
    if "," in val:
        x = val.split((val[0]) + " ")[1]
        x = x.split(",")
        if len(x) > 2:
            res = data[val[0]](int(x[0]), int(x[1]))
        elif len(x) == 2:
            res = data[val[0]](int(x[0]))
    return res

flag = "TEST"

for x in range(len(temp)):
    if x == len(flag):
        exe("\x10 999999,")
        continue
    if x >= len(flag):
        exe("\x10 %s," % (random.randint(0, 9999)))
        exe("\x16 %s,%s," % (random.randint(len(flag) + 1, len(temp) - 1), random.randint(0, 877221)))
        continue
    char = ord(flag[x])
    command = x % len(data)
    if command == 0:
        exe("\x10 %s," % exe("\x13 %s,%s," % (char, exe("\x11 %s," % char))))
    elif command == 1:
        exe("\x10 %s," % (exe("\x12 %s," % char) + exe("\x13 %s,%s," % (char, exe("\x12 %s," % char)))))
    elif command == 2:
        exe("\x10 %s," % (char - exe("\x12 %s," % 5)))
    elif command == 3:
        exe("\x10 %s," % exe("\x13 %s,%s," % (exe("\x11 %s," % exe("\x14 23,10,")), exe("\x11 %s," % char))))
    elif command == 4:
        exe("\x10 %s," % exe("\x13 %s,%s," % (len(data), char)))
    elif command == 5:
        if (exe("\x11 %s," % x)) % 3 == 0:
            exe("\x10 %s," % exe("\x13 %s,%s," % (x, exe("\x11 %s," % char))))
        else:
            exe("\x10 %s," % exe("\x12 %s," % char))
    else:
        exe("\x10 %s," % exe("\x13 %s,%s," % (5881 * 4, exe("\x12 %s," % char))))

print(temp)