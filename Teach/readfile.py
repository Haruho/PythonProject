#读取文件内容(All)
f = open('test.txt','r+')
#print(f.read())


#readline
#print(f.readline())
#循环输出
for line in f:
    print(line , end ='')



#想文件中写入  返回字符串长度  （new line）
print(f.write('Life goes on...'))
#写入的数据不是字符串的时候需要转换成字符串

#完成对文件的操作之后....
f.close()
#调用close（）之后再次操作文件会报错哦
