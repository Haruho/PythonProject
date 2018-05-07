#列表生成器
#通过循环快速创建列表

a = list(range(0,11))
print(a)

#列表创建器用[] 中括号包含
#添加条件的情况下
a = [x * x for x in range(0,11)]
print(a)

#双重迭代也可以  （更多的也有 但是不推荐使用了）
a = [m+n for m in "ABC" for n in "XYZ"]
print(a)

#添加判断条件    (输出偶数的平方根)
a = [x * x for x in range(0,11) if x%2 == 0]
print(a)

x = [1,2,3,4,5,'a','b','c','d','e']

#把一个列表里的数字和string分开存放
#a = [i if isinstance(i,str) else i for i in x]
a = [i for i in x if isinstance(i,str)]
b = [i for i in x if isinstance(i,str) == False]
print(a)
print(b)