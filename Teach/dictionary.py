#字典
#创建一个字典
classNumber = {"Zhao":1,"Qian":2,"Sun":3,"li":4}
print(classNumber)
print("================================================")
#向字典中添加元素
classNumber["Zhou"] = 5
print(classNumber)
print("================================================")

#获取指定索引的值
print(classNumber["li"])
print("================================================")

#删除其中某一个值
del classNumber["Sun"]

print(classNumber)

#获取全部关键字 返回一个列表
print(list(classNumber.keys()))
#获取全部关键字并排序
print(sorted(list(classNumber)))
print("================================================")

#另一种创建字典的方式
print(dict([('time',1),('time2',2),("time3",3)]))
