#def ask_ok(prompt , retries = 4,complaint = 'Yes or no,plaese'):
#    while True:
#        ok = input(prompt)
#        if ok in ('y','yes','ye'):
#            return True
#        if ok in ('n','no','nop','nope'):
#            return False
#        retries = retries -1
#        if retries < 0:
#            raise OSError('Uncooperative user')
#        print(compile)

#ask_ok('Do you ewally want to quit?')

#ask_ok('OK to overwrite the file?' , 2)
##这三种形式都能调用到函数
#ask_ok('OK to overwrite the file?',2,'Only Yes or No')

def f(a,l=[]):
    l.append(a)
    return l
print(f(1))   #输出[1]
print(f(2))   #[1,2] 
print(f(3))   #[1,2,3]  说明l这个变量只初始化了一次


#这个函数定义了四个参数，一个是必选参数（第一个，没有赋值的），其余都是备选参数
def parrot(voltage,state = 'a stiff',action='voom',type = 'Norwegian Blue'):
    print("-- this parrot wouldn't ",action ,end = ' ')
    print('if you put' , voltage ,"volts through it")
    print("--Lovely plumage , the",type)
    print("--It's",state ,"!")

#parrot(1000)   这些调用方式都可以
#parrot(voltage = 1000)
#parrot(voltage = 100000,action= 'voooom')
#parrot(action='voooom',voltage = 100000)
#parrot("a million",'bereft of life','jump')对应前三个参数
#parrot('a thousand' , state= 'pushing up the daisies')
