#斐波那契数列输出

x = int(input("请输入想要输出的费波纳茨数列个数..."))
def fio(n):
    a,b = 1,1
    for i in range(1,x):
        a = b
        b = a+b
    print(a,b)

fio(x)
