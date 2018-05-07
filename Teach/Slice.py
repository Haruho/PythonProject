#切片操作
#切片操作针对list tuple 字符串都可以

#列表
x = [1,2,3,4,5,6,7,8,9]
print(x)

#截取列表(取不到右边)
print(x[0:3])

#倒着截取
print(x[-3:-1])

print(x[-3:])

#复制一个列表
print(x[::])

#取前三个
print(x[:3])
#取除了前三个的之外元素
print(x[3:])

#冒号左边的数字代表截取开始的位置，空就代表0
#冒号右边的数字代表截取截止到的位置，空代表结尾

#每隔两个数取一个  包含第一个
print(x[::2])

# ：：左边的数字代表截取开始的索引
#：：中间代表截取为止的索引
#：：右边代表截取的步长

#从索引1开始每个两个取一个元素
print(x[1::2])

#元组和字符串同样适用于上述操作  只不过返回的数据类型保持不变