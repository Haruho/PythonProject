def fin(n):
    '''这里是关于这个函数的文档说明'''
    #输出一段斐波那契数列
    a,b = 0,1
    while a<n:
       # print(a, end =' ')
        a,b = b,a+b
  #  print()

fin(2000)

x = 10
#带有返回值的函数
def fin1(n):
    x = 100
    result = []
    a,b = 0,1
    while a<n:
        result.append(a)
        a,b = b,a+b
    return result

f100 = fin1(100)
print(f100)
print(x)
