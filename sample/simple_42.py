# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

# ax2 + bx + c = 0

# 的两个解。
import math
def quadratic(a,b,c):
    if(b*b - 4*a*c)>0:
        return -b+math.sqrt(b*b-4*a*c) / 2*a ,  b+math.sqrt(b*b-4*a*c) / 2*a 
    elif(b*b - 4*a*c) == 0:
        return b+math.sqrt(b*b-4*a*c) / 2*a
    elif(b*b - 4*a*c) < 0:
        return "null"
    


if __name__ == '__main__':
    # a = int(input("a:"))
    # b = int(input("b:"))
    # c = int(input("c:"))
    a = 1
    b = 7
    c = 3
    print(quadratic(a,b,c))
