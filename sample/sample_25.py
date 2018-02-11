#求1+2!+3!+...+20!的和。
#阶乘
s = 1
#阶乘和
_sum = 0

for i in range(1,21):
    #算阶乘
    s = s * i
    #把阶乘累加
    _sum = s+ _sum

print(_sum)
