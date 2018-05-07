#对10个数进行排序。
a = [5,7,2,12,33,4,6,80,45,13]

b = []

def cheak():
    c = a[0]
    N = 10
    for i in range(0,N):
        if(a[i] < c):
            c = a[i]
            b.append(c)
            N = N-1
            cheak()


cheak()

print(b)
