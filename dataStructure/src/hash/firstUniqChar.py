#!/usr/bin/env  python3

import time
class Solution:
    #def firstUniqChar(self, s: str) -> int:
    def firstUniqChar(self, s):
        # 哈希表 依次遍历 k 为char v 为index
        # 若出现第二次以上，则更新为-1供下次遍历识别
        hashmap = {}
        for i,k in enumerate(s):
            if k in hashmap:
                hashmap[k] = -1
            else:
                hashmap[k] = i
        # 第二次遍历找出 最小index
        minIndex = len(s)
        for k,v in hashmap.items():
            if -1 != v and v < minIndex:
                minIndex = v

        return minIndex

def main():
    s = Solution()

    string = "leetcode"


    timeStamp1 = time.time()
    print(s.firstUniqChar(string))
    timeStamp2 = time.time()
    """
    print(s.findRestaurant2(list1,list2))
    timeStamp3 = time.time()
    print(s.findRestaurantForce(list1,list2))
    timeStamp4 = time.time()
    """
    print(timeStamp2-timeStamp1)
    """
    print(timeStamp3-timeStamp2)
    print(timeStamp4-timeStamp3)
    """

if __name__ == '__main__':
    main()
