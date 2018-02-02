#集合
#创建一个集合  注意集合是用大括号{}包裹起来的
#集合中不存在相同元素  下面这个集合中，第一个dog被忽略了。
animal = {'dog','pig','mouse','bird','dog'}
print(animal)


#判断元素是不是在集合中
#false
print('fly' in animal)

#true
print('pig' in animal)


#也可以使用set（）方法创建集合  注意是（）  不是{}
#自动消除了相同元素
a = set('abracadabra')
print(a)

b = set('alacazam')
#集合间的运算，就是合并，交际，补集等
#集合做差
print('a-b = ' , a - b)
print('b-a = ' , b-a)
print('=====================================================')
#求交集
print(a&b)
print('=====================================================')
#集合之和
print(a|b)
