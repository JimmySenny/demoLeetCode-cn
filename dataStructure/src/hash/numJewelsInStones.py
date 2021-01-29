#!/usr/bin/env  python3

import time

class Solution:
    #def numJewelsInStones(self, jewels: str, stones: str) -> int:
    def numJewelsInStones(self, jewels, stones):
        hashsetJ = set(jewels)
        ans = 0
        for ch in stones:
            if ch in hashsetJ:
                ans += 1
        return ans


    

def main():
    J = "aA"
    S = "aAAbbbb"

    s = Solution()
    timeStamp1 = time.time()
    print(s.numJewelsInStones(J,S))
    timeStamp2 = time.time()
    """
    print(s.findDuplicateSubtrees1(root))
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
