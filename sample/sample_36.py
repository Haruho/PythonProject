#求100之内的素数

a = []
b = []
#1不算素数
for i in range(2,101):
    a.append(i)
    for j in range(2,i):
        if(i % j == 0):
        #    print(i,'不是素数')
            if(i not in b):
                b.append(i)
for k in a:
    if(k not in b):
        print(k,'是素数')
