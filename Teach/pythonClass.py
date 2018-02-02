def scope_test():
    def do_locak():
        #local中不会修改spam的初始值
        spam ="loacl spam"
    def do_nonLoacl():
        nonlocal spam
        spam ="nonLoacl"
    def do_global():
        global spam
        spam = "Global spam"
    spam = "test spam"
    do_locak()
    print("声明本地变量之后...",spam)
    do_nonLoacl()
    print("在nonlocal声明之后..." , spam)
    do_global()
    print("声明全局变量之后....",spam)

scope_test()
print("IN global scope")
