words = ['cat','dog','pig','bird']

for w in words:
    #len(string) 取得字符串长度
    print(w,len(w))


    #迭代words的副本
for w in words[:]:
    if len(w) >3:
        #按照位置插入元素
            words.insert(0,w)
            print(words)
       
#for int i =1;i<10;i++:  i不存在无法循环
