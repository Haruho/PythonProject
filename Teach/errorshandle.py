import sys
try:
    f = open("test.txt")
    s = f.readline()
    i=int(s.strip())
except OSError as err:
    print("OS Error：{0}".format(err))
except ValueError:
    print("不能吧data转化成int")
except:
    print("未处理uowu",sys.exc_info()[0])
    raise
