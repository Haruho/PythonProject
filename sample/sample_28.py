#给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
num = input("请输入一个数")
#int不是迭代器所以不能for循环

l = 0
for i in num:
    l = l+1

#复制加上逆向循环
r_num = num[:]

#for i in r_num[::-1]:
    #print(i)

print('输入的数是',num,'长度是',l,'逆顺序是',r_num[::-1])

#感觉list[::-1]这个方式很慢

#http://blog.csdn.net/wanghuafengc/article/details/17914345这个博客中有几种倒叙的方法
