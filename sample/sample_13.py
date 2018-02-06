#打印出所有的水仙花数
#三位数   个十百位的数的立方相加  等于该数本身
#153 = 1^3 + 5^3 + 3^3

#百位不能为0
for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            if(i*i*i + j*j*j + k*k*k == 100*i + 10*j+k):
                print('水仙花数有：',i,j,k)
