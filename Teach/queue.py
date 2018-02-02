from collections import deque   #导入collections的deque模块，这个模块实现了队列的操作
queue = deque(["Eric","Jonh","Michael"])
queue.append("Terry")
queue.append("Graham")
#print(queue.popleft())   这是把队首的元素移除
print(queue.popleft())
print(queue)
