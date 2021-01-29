#!/usr/bin/env  python3

import time
class Solution:
    #def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    def topKFrequent(self, nums, k):
        hashmapk = {}
        res = []
        for num in nums:
            if num in hashmapk.keys():
                hashmapk[num] += 1
            else:
                hashmapk[num] = 1
        # 对map value进行排序 一般调用快排
        top = sorted(hashmapk.items(),key=lambda hashmapk:hashmapk[1],reverse=True)
        print(type(hashmapk))

        for i in top:
            res.append(i[0])
        return res[:k]

def main():
    s = Solution()
    nums1 = [ 1, 2, 3, 4]
    nums2 = [-2,-1]
    nums3 = [-1, 2]
    nums4 = [ 0, 2]
    k = 2

    timeStamp1 = time.time()
    print(s.topKFrequent(nums1,k))
    timeStamp2 = time.time()
    """
    print(s.intersect1(nums1,nums2))
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
