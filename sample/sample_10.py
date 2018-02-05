#优化时间输出
import time

#strftime是根据给定的format来输出时间tuple（元祖），return type string
#%Y-%m-%d_%H-%M-%S是时间格式
#Y表示年   m代表月份  M代表分钟 d代表天
#H代表小时  h代表月份英文缩写  S是秒
print(time.strftime('%Y-%m-%d_%H-%M-%S' , time.localtime(time.time())))

time.sleep(1)

print(time.strftime('%Y-%m-%d_%H-%M-%S' , time.localtime(time.time())))
