#有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

Tn = []

#分母
a = 1
#分子
b= 2


#循环从3/2开始
for i in range(1,20):
    b = a+b
    a = b-a
    c = b/a
    Tn.append(c)
    print('第',i,'项是',b,'/',a)
#再加上第一项
print(sum(Tn) + 2/1)
