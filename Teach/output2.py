#平方立方表1
for x in range(1,11):
    #end = ‘ ’  代表每列之间有空格
    #rjust（）是把字符串输出到右对齐还有相应的ljust() center()
    #print(repr(x).rjust(2),repr(x*x).rjust(3),end=' ')
#    print(repr(x*x*x).rjust(4))
    print(x,x*x,x*x*x)


#平方立方表2
for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))

print('=====================================================')
#str.zfill()
print('12'.zfill(5))
#向数字前面添加0
print('-3.12'.zfill(7))
#字符串长度大于参数
print('3.14159265359'.zfill(5))
