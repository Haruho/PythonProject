t = 12345,54321,'hello!'
print(t[0])

print(t)

#元祖可能是嵌套的结构

u = t,(1,2,3,4,5)
print(u)

#元祖元素不可变
#t[0] = 10

#创建包含可变元对象的元祖
v=([1,2,3] ,[3,2,1])
print(v)