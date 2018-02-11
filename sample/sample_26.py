#利用递归方法求5!
#递归就是调用自己
num = int(input('请输入要计算阶乘的数...'))
result = 1

def jiecheng(num):
    global result
    if(num > 1):
        result = num * result
        #递归
        jiecheng(num - 1)

jiecheng(num)
print(num,'的阶乘是：',result)
