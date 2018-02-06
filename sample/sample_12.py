#判断101到200之间有几个素数
#????
#这么难吗？
x =[]
a = []
b =[]
for i in range(101,201):
    a.append(i)
    for k in range(2,i):
        if(i % k == 0 and x.count(i) < 1):
            #质数
            x.append(i)

#然后判断。。。。
#神麻烦。。。
for i in a:
    if i not in x:
        b.append(i)

print(b)
