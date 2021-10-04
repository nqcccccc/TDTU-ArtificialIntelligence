"""
Name: StacknQueue-lib.py
Author: Quoc Cuong Nguyen
Contact: cuongbo2000@icloud.com
Time: 04/10/2021 09:49
Desc:
"""

#1- Stack using deque
from collections import deque
stack = deque()
stack.append('a')
print(stack.pop())
print(stack)

#2- Stack using LifoQueue
from queue import LifoQueue
stack = LifoQueue(maxsize = 3)
print(stack.qsize())
stack.put('a')
print("Full: ", stack.full())
print("Size: ", stack.qsize())
print(stack.get())

#3- Queue by List ([])
queue = []
queue.append('a')
print(queue.pop(0))

#4- Queue by deque (collections)
from collections import deque
q = deque()
q.append('a')
print(q.popleft())

#5- Queue by Queue (queue)
from queue import Queue
q = Queue(maxsize = 3)
print(q.qsize())
q.put('a')
print(q.get())
print("\nFull: ", q.full())
print("\nEmpty: ", q.empty())

#6- Priority Queue
import heapq
li = [5, 7, 9, 1, 3]
heapq.heapify(li)
print(heap[0])
heapq.heappush(li,4)
print (heapq.heappop(li))
