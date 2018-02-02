#python Hello world  第一个python脚本
#python中的标识符，这些标识符不能作为关键字
#['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
import keyword
keyword.kwlist

'''
多行注释1
'''

"""
多行注释2
"""

#python中的注释是以一个单井号来标识的
print("Hello World");

#python里面没有大括号   一个代码块中必须保持相同的缩进  否则报错。。。
if (3>5):
    print("True")
else:
    print("false")   #只有这一句话的时候随便加空格

    print("asd") #在这句话前面加一个空格就会报错
    #只要是从这里开始编辑语句  就全部算在else的代码块中
print("Hello Again");   #和上面的缩进不一样 所以这句话不在else的代码块中

#多行语句   在没有括号的语句中，雨果过长可以使用 \  来分割语句  在 {} [] () 中的语句不需要加斜杠


