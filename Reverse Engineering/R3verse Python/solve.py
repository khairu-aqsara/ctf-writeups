import dis

class Chal():
    def __init__(self):
        self.text = 'SCT?g]'
        
    def CreateKey(self):
        return 16
    
    def Decrypt(self,target):
        res = ''
        for x in range(len(target)):
            res += chr((x + ord(target[x])) ^ self.CreateKey())
        return res
    
    def Encrypt(self):
        target = self.text
        res = ''
        for x in range(len(target)):
            res += chr((ord(target[x]) ^ self.CreateKey()) - x)
        return res

dis.dis(Chal.Decrypt)

with open('encrypted.txt', 'r') as f:
    fs = f.read()
    a = Chal()
    print(a.Decrypt(fs))