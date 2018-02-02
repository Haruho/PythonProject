#range用来取代一个等差的序列
for i in range(5):
    print(i) # 输出0  1  2  3  4 range并不包含括号中的数字。

print("======================================")
for j in range(5,10):  #输出5  6  7  8  9
    print(j)
print("======================================")

for k in range(0,10,2): #输出0  3  6  9 这里面range的第三个参数代表步长，也就是每隔几个取一次值
    print(k)
print("======================================")
for l in range (-10,-100,-30):   #步长也可是负数
    print(l)

print("======================================")
#可以结合len和range循环一个自定链表 可以使用enumerate()来代替
words = ['you','me','us','they']
for w in range(len(words)):
    print(w,words[w])

print('========================================')
print(list(enumerate(words))) #输出[(0, 'you'), (1, 'me'), (2, 'us'), (3, 'they')]

print('=========================================')
print(range(5))  #输出range（0，5） 可见这并不是一个列表，range只是用来迭代的函数
print('=========================================')
print(list(range(5)))  #输出0，1，2，3，4  通过list可以把range中的期望序列变化成序列。
