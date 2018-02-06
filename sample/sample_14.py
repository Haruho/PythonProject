#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

x = int(input("请输入一个正整数..."))
ys = []
a = ['a','v']
def fenjie(num):
    for i in range(2,num+1):
        if(num % i == 0 and num >= i):
            ys.append(i)
            #需要转换类型
            fenjie(int(num/i))
            break

fenjie(x)
print("*".join(str(ys)))
print('*'.join(a))
