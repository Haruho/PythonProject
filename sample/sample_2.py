#企业发放的奖金根据利润提成。利润(I)
#低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按
#10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
#40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，
#可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？


I = int(input("请输入利润！"))
b = 0

if(I<=100000):
    b=I * 0.1
    print(b)
elif(100000<I<=200000):
    b = (I - 100000) * 0.075 + 100000 * 0.1
    print(b)
elif(200000<I<=400000):
    b = 10000 + 7500 + (I-200000)*0.05
    print(b)
elif(400000<I<600000):
    b=17500+ 10000 + (i-400000) * 0.03
    print(b)
elif(600000<I<=1000000):
    b=27500+12000+(I-600000)* 0.015
    print(b)
elif(I>1000000):
    b=39500+9000+(i-1000000)*0.01
    print(b)

#上面这个方法一点没经过大脑


II = [100000,200000,400000,600000,800000,1000000]
rat = [0.1,0.075,0.05,0.03,0.015,0.01]
bounds = 0
for i in range(0,6):
    if(I > II[i]):
