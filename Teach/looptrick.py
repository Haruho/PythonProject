#新建一个字典
knights = {'gallahad':'the pure' , 'robin':'the brave'}
#items()方法显示 关键字和值
for i,v in knights.items():
    print(i,v)

print("===============================================")
#enumerate()可以同时显示列表中的索引和对应的值
for i,v in enumerate(['tic','tac','toe']):
    print(i,v)

print("===============================================")
#循环多个数组的时候，可以使用zip（）整体进行打包一起循环
question = ['name','quest','favorite color']
answer = ['lancelot','the holy grail','blue']
for q,a in zip(question,answer):
    print('what is your {0}? It is {1}.'.format(q,a))

print("===============================================")
#逆向循环数列
for i in reversed(range(1,10,2)):
    print(i)

print("===============================================")
#循环排序过后的序列
basket = ['apple','orange','apple','pear','orange','banana']
#注意这里把列表转换成了集合
for f in sorted(set(basket)):
    print(f)
print("===============================================")
#在循环中修改正在遍历的序列
words = ['cat','eats','catfoods']
#这里创建了一个words的副本，循环的是副本，修改的是原本的序列
for i in words[:]:
    if(len(i)>6):
        words.insert(0,i)
        print(words);
