chars=[]
for x in range(48,126):
    hasil=''
    c=x
    while(c>1):
        if c > 1:
            if c % 2 == 0:
                hasil+='*'
                c=c/2
            else:
                hasil+='.'
                c=c+1
    chars.append({chr(x) : hasil})

desc=''

with open('enc.txt','r') as f:
    line = [ff.rstrip() for ff in f.readlines()]
    for enc in line:
        for keys in chars:
            key = [key for key, value in keys.iteritems() if value == enc]
            if len(key) > 0:
                desc+=key[0]
    
print desc