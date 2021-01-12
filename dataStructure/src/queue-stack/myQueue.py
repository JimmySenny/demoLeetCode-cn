#!/usr/bin/env python3

class MyQueue:
    def __init__(self):
        #Initialize your data structure here.
        self.stack1 = []
        self.stack2 = []
#    def push(self, x: int) -> None:
    def push(self, x):
        #Push element x to the back of queue.
        self.stack1.append(x)
#    def pop(self) -> int:
    def pop(self):
        #Removes the element from in front of queue and returns that element.
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        if self.stack2:
            x = self.stack2.pop()
        else:
            x = None
        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return x;
#    def peek(self) -> int:
    def peek(self):
        #Get the front element.
        if self.stack1:
            return self.stack1[0]
        else:
            return None;


#    def empty(self) -> bool:
    def empty(self):
        #Returns whether the queue is empty.
        if self.stack1:
            return False
        else:
            return True

    def printMyQueue(self):
        lens1 = len(self.stack1);
        for i in range(lens1):
            print(self.stack1[i],end=',')
        print()

class MyQueue2:
    def __init__(self):
        self.stackPush = []
        self.stackPop  = []
        self.front = None
        self.rear = None
    def empty(self):
        if self.stackPush or self.stackPop:
            return False;
        return True;
    def push(self, x):
        self.stackPush.append(x)
        self.rear = x;
    def pop(self):
        if not self.stackPop:
            while self.stackPush:
                self.stackPop.append(self.stackPush.pop())
        
        return self.stackPop.pop() if self.stackPop else None
    def peek(self):
        if self.stackPop:
            return self.stackPop[-1]
        else:
            return self.stackPush[0]
    def printMyQueue(self):
        if self.stackPop:
            lens = len(self.stackPop)
            i = lens - 1
            while i > 0:
                print(self.stackPop[i],end=',')
                i -= 1;
        lens = len(self.stackPush)
        for i in range(lens):
            print(self.stackPush[i],end=',')

        print()

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
def main():
    obj = MyQueue2()

    print(obj.empty())
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.printMyQueue()
    print("peek",obj.peek())
    print("pop",obj.pop())
    obj.push(4)
    print("isempty",obj.empty())

    obj.printMyQueue()
    print("pop",obj.pop())
    print("pop",obj.pop())
    print("pop",obj.pop())
    print("pop",obj.pop())
    print(obj.empty())
    obj.printMyQueue()

if __name__ == '__main__':
    main()
