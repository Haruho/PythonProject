#展示Python中列表的使用

#声明一个列表
x = [1,2,3]

#向列表的末尾添加一个元素
x.append("a")

y =[]
#将x中的元素全部添加到另一个列表里,原列表不变
y.extend(x)
#print(y)

#把一个元素插入到特定索引（从0开始）
x.insert(1,0)

#获取指定元素的索引
x.index("a")
print(x.index("a"))

#移除匹配的第一个元素
x.remove("a")

#移除指定位置的元素 并将其返回   没指定的话返回最后一个元素
x.pop(1)
#print(x.pop(1))


#每条都做麻烦  再就是一些基础的  类似clear（） 清空列表    count（x）获取x出现的次数
#sort（）排序     reverse（）反转列表   copy（）返回一个浅拷贝
print(x)
