#!/usr/bin/env python3

class SingleLinkNode:
    def __init__(self, val,prev=None, pnext=None):
        self.value = val;
        self.pnext = None;
class MySingleLinkedList:
    def __init__(self):
        #Initialize your data structure here.
        self.size = 0
        self.head = SingleLinkNode(0)
#    def get(self, index: int) -> int:
    def get(self, index):
        #Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        print("get:", index)
        if not 0<=index<self.size:
            return -1
        node = self.head.pnext
        for i in range(index):
            node = node.pnext
        return node.value

#    def addAtHead(self, val: int) -> None:
    def addAtHead(self, val):
        """ Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.  """
        print("addhead:", val)
        newNode = SingleLinkNode(val)
        newNode.pnext = self.head.pnext
        self.head.pnext = newNode
        self.size += 1
#    def addAtTail(self, val: int) -> None:
    def addAtTail(self, val):
        """ Append a node of value val to the last element of the linked list.  """
        print("addtail:", val)
        node = self.head
        for i in range(self.size):
            node = node.pnext
        newNode = SingleLinkNode(val)
        node.pnext = newNode;
        self.size += 1
#    def addAtIndex(self, index: int, val: int) -> None:
    def addAtIndex(self, index, val):
        """ Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.  """
        print("addindex:", index, val)
        if index > self.size:
            return 
        if index < 0:
            return self.addAtHead(val)
        newNode = SingleLinkNode(val)
        prev = self.head
        for i in range(min(self.size, index)):
            prev = prev.pnext
        newNode.pnext = prev.pnext
        prev.pnext = newNode
        self.size += 1
#    def deleteAtIndex(self, index: int) -> None:
    def deleteAtIndex(self, index):
        """ Delete the index-th node in the linked list, if the index is valid.  """ 
        print("delete:", index)
        if 0<= index <self.size:
            prev = self.head
            for i in range(index):
                print("i:", i)
                prev = prev.pnext
                print("v:", prev.value)
            print("prev:", prev.value)
            cur = prev.pnext
            print("cur:", cur.value)
            prev.pnext = cur.pnext
            self.size -= 1
    def iter(self):
        node = self.head
        for i in range(self.size):
            node = node.pnext
            print("i,v:",i,node.value, end="|")
        print("size:", self.size)

class DoubleLinkNode:
    def __init__(self, val, prev=None, pnext=None):
        self.prev = prev
        self.value = val;
        self.pnext = pnext;
class MyDoubleLinkedList:
    def __init__(self):
        self.size = 0
        self.head = DoubleLinkNode(0)
        self.tail = DoubleLinkNode(0)
        self.head.pnext = self.tail
        self.tail.pnext = self.head
    def get(self, index):
        print("get:", index)
        if index < 0 or index >= self.size:
            return -1
        if index < self.size - index:
            curr = self.head
            for i in range(index+1):
                curr = curr.pnext
        else:
            curr = self.tail
            for i in range(self.size - index):
                curr = curr.prev
        return curr.value
    def addAtHead(self, val):
        print("addhead:", val)
        newNode = DoubleLinkNode(val)
        prevd = self.head
        if self.size == 0:
            pnextd = self.tail
        else:
            pnextd = self.head.pnext
        newNode.prev = prevd
        newNode.pnext = pnextd
        prevd.pnext = newNode
        pnextd.prev = newNode
        self.size += 1
    def addAtTail(self, val):
        print("addtail:", val)
        newNode = DoubleLinkNode(val)
        pnextd = self.tail
        if self.size == 0:
            prevd = self.head
        else: 
            prevd = self.tail.prev
        newNode.prev = prevd
        newNode.pnext = pnextd
        pnextd.prev = newNode
        prevd.pnext = newNode
        self.size += 1
    def addAtIndex(self, index, val):
        print("addindex:", index,val)
        if index > self.size: 
            return 
        if index < 0:
            return self.addAtHead(val)
        if index == self.size:
            return self.addAtTail(val)

        #判断从那边走快
        if index < self.size - index:
            prevd = self.head
            for i in range(index):
                prevd = prevd.pnext
            pnextd = prevd.pnext
        else:
            pnextd = self.tail
            for i in range(self.size - index):
                pnextd = pnextd.prev
            prevd = pnextd.prev

        self.size += 1
        newNode = DoubleLinkNode(val)
        newNode.prev = prevd
        newNode.pnext = pnextd
        prevd.pnext = newNode
        pnextd.prev = newNode
    def deleteAtIndex(self, index):
        print("delete:", index)
        if index<0 or index >= self.size:
            return

        #判断从那边走快
        if index < self.size - index:
            prevd = self.head
            for i in range(index):
                prevd = prevd.pnext
            pnextd = prevd.pnext.pnext
        else:
            pnextd = self.tail
            for i in range(self.size - index - 1):
                pnextd = pnextd.prev
            prevd = pnextd.prev.prev
        self.size -= 1
        prevd.pnext = pnextd
        pnextd.prev = prevd
    def iter(self):
        node = self.head
        for i in range(self.size):
            node = node.pnext
            print("i,v:",i,node.value, end="|")
        print("size:", self.size)

def main():
#    obj = MySingleLinkedList()
    obj = MyDoubleLinkedList()
    """
    obj.addAtHead(1)
    obj.addAtTail(5)
    obj.addAtIndex(1,3)
    obj.iter()
    print(obj.get(1))
    obj.iter()
    obj.deleteAtIndex(1)
    obj.iter()
    print(obj.get(1))
    obj.addAtIndex(2,4)
    obj.addAtIndex(1,2)
    obj.iter()
    obj.deleteAtIndex(7)
    obj.deleteAtIndex(-1)
    obj.deleteAtIndex(4)
    obj.iter()
    obj.deleteAtIndex(2)
    obj.iter()
    obj.deleteAtIndex(4)
    obj.iter()
    """
    obj.addAtIndex(0,100)
    obj.addAtIndex(0,200)
    obj.addAtIndex(1,500)
    print(obj.get(0),obj.get(1),obj.get(2), obj.get(3), obj.get(4))
if __name__ == '__main__':
    main()
