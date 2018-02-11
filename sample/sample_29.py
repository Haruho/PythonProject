#有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。
#问第4个人岁数，他说比第3个人大2岁。
#问第三个人，又说比第2人大两岁。
#问第2个人，说比第一个人大两岁。
#最后问第一个人，他说是10岁。请问第五个人多大？

#这几题的目的在于让你学会怎么用递归

year = 10
nianling = 0
def fifthperson():
    global nianling
    for i in range(1,5):
        year = year + 2
        nianling = year
        fifthperson()

print(nianling)
