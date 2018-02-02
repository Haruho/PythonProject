import sys
s=['1','2','3']
for arg in s:
    try:
        f = open(arg , 'r')
    except IOError:
        print('不能打开',arg)
    else:
        print('打开成功')
        f.close()

def test():
    print(1/0)
#检查try中调用的函数的异常
try:
    test()
except:
    print('函数有问题')


raise NameError("HGGGGGGGGGGGGGGG")
