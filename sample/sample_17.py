#统计输入的字符串中有几个字母数字符号空格

letter = 0
number = 0
space = 0
symbol = 0

x = str(input("请输入字符串..."))

for i in x:
    if i.isalpha():
        letter += 1
    elif i.isspace():
        space += 1
    elif i.isdigit():
        number += 1
    else:
        symbol += 1

print('字符串',x,'有',letter,'个字母/n'
      ,'有',space,'个空格/n',
      '有',number,'个数字/n',
      '有',symbol,'个符号')
