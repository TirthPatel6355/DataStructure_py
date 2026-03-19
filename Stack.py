from collections import deque
# stack = deque()
# # print(dir(stack))
# stack.append(2)
# stack.append(3)
# stack.append(4)
# print(stack.pop())
class Stack:
    def __init__(self):
        self.stack = deque()
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def print_list(self):
        print(self.stack)
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)

s = Stack()
s.push(1)
s.push(2)
# print(s.peek())
# print(s.is_empty())
# print(s.stack)
print(s.size())