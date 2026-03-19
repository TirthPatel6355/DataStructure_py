# Using List.....
# stock_price_q= []
# stock_price_q.insert(0,254)
# stock_price_q.insert(0,100)
# stock_price_q.insert(0,2597)
# stock_price_q.pop()
# print(stock_price_q)

#  Using Collection.....

from collections import deque
# q=deque()
# q.appendleft(1)
# q.appendleft(2)
# q.appendleft(3)
# print(q.pop())
class Queue:
    def __init__(self):
        self.queue = deque()
    def enqueue(self, item):
        self.queue.appendleft(item)
    def dequeue(self):
        return self.queue.pop()
    def isEmpty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.dequeue()
print(q.queue)