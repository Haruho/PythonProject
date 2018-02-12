#：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
week = ['m','w','f','M','W','F']
r_week = ['t','s','T','S']

a = ['h','u','a']
x = input('请输入第一个字母...')


def secondjudge():
    y = input('请输入第二个字母')
    if(y not in a):
        print('not week error')
    if(x == r_week[0] or x==r_week[2]):
        if(y == a[0]):
            print('Thursday')
        elif(y == a[1]):
            print('Tuesday')
    elif(x == r_week[1] or x == r_week[3]):
        if(y == a[1]):
            print('Sunday')
        elif(y == a[2]):
            print('Saturday')


if(x in week):
    if(x == week[0] or x==week[3]):
        print("Monday")
    elif(x == week[1] or x==week[4]):
        print('Wednesday')
    elif(x == week[2] or x == week[5]):
        print('Firday')
elif(x in r_week):
    secondjudge()
elif(x not in week and x not in r_week):
    print('not week error')
