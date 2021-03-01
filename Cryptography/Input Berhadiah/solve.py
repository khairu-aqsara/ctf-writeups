from pwn import *
from string import printable

blok_size = 32

def split_len(seq):
    return [seq[i:i+blok_size] for i in range(0, len(seq), blok_size)]

def find_diff(response, first_response):
    if response[2] == first_response[2]:
        return True
    else:
        return False


def cari_blok(response):
    new = []
    for i in range(0, len(response), blok_size):
        new.append(response[i:i+blok_size])
    return new


def cari_panjang_blok():
    known_byte = list()
    blok_awal = 8

    while True:
        con = remote('103.157.96.13',7790)
        con.recvuntil("Input: ")
        patokan = ''
        log.info("Mencari Blok Awal....")
        data = 'a' * (blok_awal -len(known_byte))
        data_length = len(data)
        con.sendline(data)
        res = con.recvuntil('\n')
        res = res.decode()
        res = res.replace('Input: ','')
        res = res.replace('\r\n','')
        res_length = len(res)
        blok = split_len(res)

        if res_length == 128:
            patokan = blok[1]
        elif res_length == 160:
            patokan = blok[2]

        log.info(str(blok))

        log.info("Panjang : {}".format(str(res_length)))
        log.success("Patokan : {}".format(patokan))

        printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;<=>?@[]^_`{|}~'

        for c in printable:
            pading_data = 'a' * (blok_awal - len(known_byte)) + ''.join(known_byte) + c
            print("Mencoba Karaketer {}".format(pading_data))
            con.sendline(pading_data)
            res = con.recvuntil('\n')
            res = res.decode()
            res = res.replace('Input: ','')
            res = res.replace('\r\n','')
            respon_blok = split_len(res)
            log.info(str(respon_blok))
            if patokan in respon_blok:
                log.success("Karakater ditemukan")
                log.success("Bloknya : {}".format(valid_check))
                print("Karakater : {}".format(hex(ord(c))))
                known_byte.append(c)
                break
        print(known_byte)
        if len(known_byte) > 8 :
            break
        con.close()
    print(known_byte)

def testing():
    printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;<=>?@[]^_`{|}~'


    dapet=''

    con = remote('103.157.96.13',7790)
    con.recvuntil("Input: ")
    data = 'B' * 44 + 'A' * 16 * 2
    con.sendline(data)
    res = con.recvuntil('\n')
    res = res.decode()
    res = res.replace('Input: ','')
    res = res.replace('\r\n','')
    blok_awal = split_len(res)
    print(len(res))
    print(str(blok_awal) + '\t' + data)

    num_padding = 63 # 15 # 31 # 
    know_char = 'CTFR{n4m4ny4_0r4cl3_p4dd1n9_4tt' #CTFR{n4m4ny4_0r4cl3_p4dd1n9_4tt4ck_y4?}

    if blok_awal[2:-3][-2:][0] == blok_awal[2:-3][-2:][1]:
        while 1:
            if len(know_char) >= 39:
                break

            padding = sendData(con, 'B' * 44 + 'A' * (num_padding - len(know_char)))
            for i in printable:
                hasil = sendData(con, 'B' * 44 + 'A' * (num_padding - len(know_char)) + know_char + i)
                if hasil[7] == padding[7]: # 4 5 7
                    know_char+=i
                    print(i)
                    break
                else:
                    print("----{}".format(i))
    else:
        print('NOPE')

    print(know_char)


def sendData(con, data):
    con.sendline(data)
    res = con.recvuntil('\n')
    res = res.decode()
    res = res.replace('Input: ','')
    res = res.replace('\r\n','')
    blok = split_len(res)
    log.info(''.join(blok))
    log.success(res)
    return blok

testing()