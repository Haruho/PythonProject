#求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字
#例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

import math
import sys
x = int(input('最大的数字有多少位？..'))
y = int(input('数字是几？'))
num = 0
s= 0
Tn = []
for i in range(1,x+1):
    num = y*(math.pow(10,i-1)) + num
    print(num)

#Tn = reduce(lambda x,y:x+y,Tn) reduce没定义。。。？？？
for i in Tn:
    s = s+i

print(s)
