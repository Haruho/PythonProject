#输入某年某月某日判断这天是一年中的第几天
y = int(input("输入年份"))
m = int(input("输入月份"))
d = int(input("输入日期"))

suma = 0
x=[31,29,31,30,31,30,31,31,30,31,30,31]

def CountDay(isLeap):
    #这个变量一定要注意
    global suma
    for i in range(0,m):
        print(i)
        suma = x[i] + suma
    if(isLeap):
        print("这一年是闰年，这一天是这年的第",suma - (x[i] - d),'天')
    else:
        print("这一年不是闰年，这一天是这年的第",suma - (x[i] - d - 1),'天')



#判断是不是闰年

if(y%100 != 0 and y%4 == 0):
    CountDay(True)
elif(y%100 == 0 and y%400 ==0):
    CountDay(True)
else:
    CountDay(False)
