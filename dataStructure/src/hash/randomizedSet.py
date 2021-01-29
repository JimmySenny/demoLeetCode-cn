#!/usr/bin/env  python3

import time
import random

class RandomizedSet:
    def __init__(self):
        #Initialize your data structure here.
        self.hashmap = {}
        self.listindex = []

    #def insert(self, val: int) -> bool:
    def insert(self, val):
        #Inserts a value to the set. Returns true if the set did not already contain the specified element.
        if val in self.hashmap:
            return False
        self.hashmap[val] = len(self.listindex)
        self.listindex.append(val)
        return True

    #def remove(self, val: int) -> bool:
    def remove(self, val):
        #Removes a value from the set. Returns true if the set contained the specified element.
        if val not in self.hashmap:
            return False
        valLast, idx = self.listindex[-1], self.hashmap[val]
        self.listindex[idx], self.hashmap[valLast] = valLast, idx

        self.listindex.pop()
        del self.hashmap[val]
        return True

    def getRandom(self) -> int:
        #Get a random element from the set.
        return random.choice(self.listindex)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

def main():
    obj = RandomizedSet()
    print(obj.insert(1))
    print(obj.insert(1))
    print(obj.insert(3))
    print(obj.insert(4))
    print(obj.insert(8))
    print(obj.remove(1))
    print(obj.remove(9))
    print(obj.getRandom())
    print(obj.getRandom())
    print(obj.getRandom())

if __name__ == '__main__':
    main()
