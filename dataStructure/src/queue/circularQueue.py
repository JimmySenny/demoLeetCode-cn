# -*- coding:utf-8 -*-

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.data = [0] * k;
        self.head = 0;
        self.tail = -1;
        self.size = k;
        self.currentSize = 0;

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if( self.currentSize >= self.size ):
            return False;

        self.currentSize += 1;
        self.tail += 1;
        self.tail = (self.tail)%self.size;
        self.data[self.tail] = value;
        return True;

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if( self.currentSize <= 0 ):
            self.head = 0;
            self.tail = -1;
            return False;

        self.currentSize -= 1;
        self.data[self.head%self.size] = -1;
        self.head += 1;
        return True;

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if( self.isEmpty ):
            return -1;
        
        return self.data[self.head%self.size];
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if( self.isEmpty ):
            return -1;
        
        return self.data[self.tail%self.size];
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if( self.currentSize == 0 ):
            return True;
        return False;

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if( self.currentSize == self.size ):
            return True;
        return False;
    
    def viewQueue(self):
        print(self.data);

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
def main():
    cq = MyCircularQueue(3);
    print(cq.head);
    print(cq.tail);
    cq.viewQueue();

    cq.enQueue(2);
    print(cq.head);
    print(cq.tail);
    cq.enQueue(3);
    cq.enQueue(4);
    print(cq.head);
    print(cq.tail);
    cq.enQueue(5);
    cq.viewQueue();

    cq.deQueue();
    cq.deQueue();
    cq.deQueue();
    cq.enQueue(6);
    print(cq.head);
    print(cq.tail);
    cq.viewQueue();
    
    cq.enQueue(7);
    cq.deQueue();
    cq.enQueue(8);
    cq.viewQueue();

    print(cq.head);
    print(cq.tail);SJPLBCHBKHIIQCLF

if __name__ == "__main__":
    main();