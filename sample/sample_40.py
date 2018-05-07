#讲一个数组逆向输出
a = [1,2,3,4]

b = []
for x in range(list.__len__(a),0,-1):
    print(x)
    b.append(x)


print(b)
