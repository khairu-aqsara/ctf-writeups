import pygame, random, string, time
from Crypto.Util.number import inverse
from pygame.locals import *
from pygame.surface import Surface
# VGA Required

pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
nonvertical = 3

def genChar():
    c = string.digits + string.ascii_letters
    return c[random.randint(0, len(c) - 1)]

def genNumber(min, max):
    res = []
    for x in range(min, max + 1):
        if x > 1:
            for i in range(2, x):
                if (x % i) == 0:
                    break
            else:
                res.append(x)
    return res

def draw(x, y, color, size):
    global screen
    s = Surface(size)
    s.fill(color)
    screen.blit(s, (x, y))

c = 0
def getObjColor(x):
    stor = ord(x)
    x = ord(x)
    if x >= 65 and x <= 90:
        x += 38
    elif x >= 97 and x <= 122:
        x += 50
    else:
        x += 8
    num = genNumber(stor - 64, stor)
    v1 = abs(num[4] - c)
    v2 = abs(num[6] + c)
    v3 = (v1 * v2) % 255
    return (v1 + v2, v3 ^ x, v3)

flag = 'CTFR{wh3n_y0u_h4t3_p1x3l_but_th4t_w45_t45k_y0u_mu5t_t0_s0lv3_1t}'


len_flag = len(flag)
max_height = int(round(height / len_flag))
usedheight = max_height

while True:
    screen.fill(0)

    usedheight = 0

    for ch in flag:
        target = ch
        for x in range(0, width, width / max_height):
            draw(x, usedheight, getObjColor(target), (width / max_height, max_height))
            c += 1
        c = 0
        usedheight += max_height

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)