#类对象
class MyClass:
    '''类示例'''
    i = 123456
    def f(self):
        return 'hello world'

#上面类中的 i 和 函数f  以及文档注释都是这个类的属性
#通过 obj.name 来获取

print(MyClass.i)
print(MyClass.f)
print(MyClass.__doc__)

#也可以给属性赋值
MyClass.i=1111
print(MyClass.i)


#类的实例化  使用函数符号  也就是像函数那样调用类  再赋值给一个变量就行了
x = MyClass()
print(x.i)
#python中的类也有类似构造函数的部分，就是__init__()


class Complex:
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i = imagpart
#创建类的实例  函数中如果又__init__函数，那么他将会呗执行，可以以带有参数
x = Complex(3.0,-4.5)

print(x.r)
print(x.i)
