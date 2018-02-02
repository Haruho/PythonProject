#输出字符串
#转化为字符串
s = 'hello world'
print(str(s))
print(repr(s))

print(str(1/7))

x = 10*3.25
y=200*200
a = 'the value of x is ' + repr(x) + ',and y is '+ repr(y) + '...'
print(a)
#repr给字符串添加了引号和反斜杠
hello = 'hello,world\n'
hellos = repr(hello)
print(hellos)

#repr()的参数可以是任何python类型
print(repr((x,y,('spam','eggs'))))
