#模块练习

print('这是一条执行语句，仅在被导入的时候执行一次')

def fib(n):
    a,b = 0,1
    while b< n:
        print(b,end=' ')
        a,b = b,a+b
    print()

def fin2(n):
    result = []
    a,b = 0,1
    while b<n:
        result.append(b)
        a,b = b,a+b
    print(result)
