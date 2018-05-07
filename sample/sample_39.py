#向一个已经排好序的数组里添加一个数，并且按照之前的规则在此排序

a = [10,21,35,47,58,69]

#a.append(6)

#a.sort()

x = int(input("enter a number..."))
for i in a:
    if(i<x):
        a.insert(a.index(i),x)

print(a)
