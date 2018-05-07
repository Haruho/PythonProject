#list列表 和 tuple元祖的区别

a = [1,2,3,4,5,6,7,8]

#输出列表长度
print("list长度是：" , len(a))
#输出最后一个元素  倒数输出元素就用负数
print("list的最后一个元素是：" , a[-1])
#list可变  append向list中最后一位添加一个元素
a.append(9)
print("向list中添加一个元素（9）" , a)

#向list中的  1 索引  处  添加  0 元素
a.insert(1,0)
print(a)

#删除最后一个元素 使用pop()
a.pop()
print("使用pop()删除最后一个元素",a)

#删除任意索引的元素 use pop(i)
print("删除索引为1的元素之前" ,a)
a.pop(1)
print("删除索引为1的元素之后" ,a)


#改变某一个元素的值  直接索引赋值
a[0] = 10
print("第一个元素由0改为10",a)

#list元素可以是int str 甚至是另一个数组
b = [1,2,3,[4,5]]
print("列表b的长度是：",len(b))
print("列表b的第四个元素是：",b[3])