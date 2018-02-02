#python1001例
#1234组成互不相同切不重复的多少个三位数？

num = 0
#取左不取右
for i in range(1,5):
#    num = 100 * i
    for j in range(1,5):
        if(i!=j):
#            num = 100 * i + j*10
            for k in range(1,5):
                if(i != j and i!= k and j!=k):
                    num = 100 *i+10*j+k
                    print(num)
