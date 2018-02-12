#练习函数调用。

def firstRun():
    print('FirstRun')
    SecondRun()

def SecondRun():
    print('SecondRun')


#函数定义写在运行语句的前面，否则会报没有定义的错误
firstRun()
