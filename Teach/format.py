#format的基本用法
print('we are {} who say {}'.format('kill','Ha'))

#可以选择format的参数
print('{0} and {1} are animals'.format('dog' ,'cat'))
print('{1} and {0} are animals'.format('dog' ,'cat'))


#也可以使用关键字参数
print('This {food} is {adjective}'.format(
    food = 'cake',adjective = 'wonderful'
))

#关键字参数和数字可以随意组合
print('I have {0},It is {1},what do you have? {test}?'.format(
    'apple','green' , test= 'Haha'
))
