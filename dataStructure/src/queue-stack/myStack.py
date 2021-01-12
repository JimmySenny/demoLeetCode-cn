#!/usr/bin/env python3

class MyStack:
    # one queue implement
    def __init__(self):
        #Initialize your data structure here.
        self.queue = []
        self.rear = None
#    def push(self, x: int) -> None:
    def push(self, x):
        #Push element x onto stack.
        self.queue.append(x)
        self.rear = x
#    def pop(self) -> int:
    def pop(self):
        #Removes the element on top of the stack and returns that element.
        lens = len(self.queue)
        i = 0
        while i < lens - 1:
            # front -> rear
            self.rear = self.queue.pop(0)
            self.queue.append(self.rear)
            i += 1
        return self.queue.pop(0) if self.queue else None
#    def top(self) -> int:
    def top(self):
        #Get the top element.
        return self.rear
#    def empty(self) -> bool:
    def empty(self):
        #Returns whether the stack is empty.
        if self.queue:
            return False
        else:
            return True
    def printStack(self):
        for i in range(len(self.queue)):
            print(self.queue[i], end=',')
        print()

def main():
    obj = MyStack()
    print("isEmpty",obj.empty())
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.printStack()
    print("pop", obj.pop())
    print("pop", obj.pop())
    obj.push(4)
    obj.printStack()
    print("isEmpty",obj.empty())

if __name__ == '__main__':
    main()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
