#导入刚才的filo.py
import filo
#调用
filo.fib(1000)

filo.fin2(100)

print(filo.__name__)
#也可以将函数声明成一个变量
fib = filo.fib
fib(500)

#把模块作为脚本使用
