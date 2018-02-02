#for语句中的else 
for n in range(2,10):
    for x in range(2,n):
        if n %x == 0:
            print(n,'等于',x ,"*" ,n//x) #//应该是除号，得到的结果是int，/得到的结果是float
            break
    else:   #在for的语句中，因为和for有相同缩进
         print(n,'是素数')

print('=================================================')
#continue就个其他语言差不多了，会继续执行循环中的下一个
for num in range(2,10):
    if num % 2 == 0:
        print("even number" , num)
        continue
    print("number" , num)