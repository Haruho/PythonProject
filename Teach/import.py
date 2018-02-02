#import     from...import导入模块

#导入sys模块
#import sys
#print('===========Python Import mode==============')
#print('命令行参数为：')
#for i in sys.argv:
#    print(i)
#print('\n python的路径是',sys.path)


#导入sys中的argv和path
from sys import argv,path   #特定的成员
print('===========Python Import mode==============')
print('path',path)   #因为导入了path成员，所以在引用的时候不需要加sys

