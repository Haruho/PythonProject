#定义函数的一些技巧

#正常定义个一个函数
def power1(x):
    return x*x

#当计算n次方的时候  改进这个函数
def power2(x,n=2):
    a = 1
    while n>0:
        a = a*x
        n = n-1
    return a
#将power2的参数n变成默认参数

#多个默认参数的函数
def student(name,sex,city = 'qth',age = 18):
    print("name" , name)
    print("sex",sex)
    print("city",city)
    print("age",age)

def addEnd(a=[]):
    a.append("End")
    return a;


#可变参数
def getSum(*numbers):
    sum =0
    for i in numbers:
        sum = sum + i
    return sum

#关键字参数
def singin(name,password,**detail):
    if('country' in detail):
        pass
    print("name",name)
    print('password',password)
    print(detail)

#命名关键字参数
#存在可变参数nickname  后面的country和job就算作命名关键字参数了
def namedpatr(name,*nickname,country,job):
    print(name,nickname,country,job)
#没有可变参数，必须添加分隔符 *  
def namedpatr1(name,*,country,job):
    print(name,country,job)

if __name__ == '__main__':
    # print(power2(2,4))
    # print(power2(2))
    # student('xl',0)
    # student('xm',1,'sys')
    # student('xh',0,age=19)
   # l = ["a","b"]
   # addEnd(l)
   # print(l)
#    print(addEnd([]))
#    print(addEnd([]))
#    print(addEnd([]))
    # print(getSum([2,3,4]))
     #print(getSum(2,3,4))
     #singin('jack0','123',detail = ('US','Teacher'))
     #singin('jack','123',country = 'US',job= 'teacher')
     #namedpatr('1','asd','d','c',country = 'CHINA',job="work")
     namedpatr1("zch",'China','programmer')