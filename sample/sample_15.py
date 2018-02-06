#利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

#逻辑运算符的嵌套是什么玩意？？？？

#逻辑运算符就是is not and or？
x = int(input('输入分数：'))

if(x >= 90):
    print("A")
elif(x>=60 and x<90):
    print("B")
elif(x<60):
    print("C")
