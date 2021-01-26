#!/usr/bin/env  python3

import time
class Solution:
    #def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    def intersect(self, nums1, nums2):
        # 哈希表分别存储num1 的值和出现次数，再取交集
        hashmapnums1 = {}
        hashmapnums2 = {}
        res = []
        for i in range(len(nums1)):
            if nums1[i] in hashmapnums1:
                hashmapnums1[nums1[i]] += 1
            else:
                hashmapnums1[nums1[i]] = 1
        for i in range(len(nums2)):
            if nums2[i] in hashmapnums2:
                hashmapnums2[nums2[i]] += 1
            else:
                hashmapnums2[nums2[i]] = 1
        
        if len(hashmapnums1) < len(hashmapnums2):
            for k,v in hashmapnums1.iterms():
                if k in hashmapnums2:
                    hashmapnums1[k] = min(hashmapnums1[k],hashmapnums2[k])
                else:
                    hashmapnums1[k] = 0
            print(hashmapnums1)
            for k, v in hashmapnums1.iterms():
                if 0 == v:
                    continue
                else:
                    while v:
                        res.append(k)
                        v -= 1
        else:
            for k,v in hashmapnums2.items():
                if k in hashmapnums1:
                    hashmapnums2[k] = min(hashmapnums1[k],hashmapnums2[k])
                else:
                    hashmapnums2[k] = 0
            print(hashmapnums2)
            for k, v in hashmapnums2.items():
                if 0 == v:
                    continue
                else:
                    while v:
                        res.append(k)
                        v -= 1
        return res
    def intersect1(self, nums1, nums2):
        # 优化 # 将其中比较短的数组进行遍历储值和出现次数的hash，
        # 再遍历另一个数组，和hash的值判断得到结果
        hashmapnums = {}
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2, nums1
        res = []
        for i in range(len(nums1)):
            if nums1[i] in hashmapnums:
                hashmapnums[nums1[i]] += 1
            else:
                hashmapnums[nums1[i]] = 1
                pass
            pass
        for i in range(len(nums2)):
            if nums2[i] in hashmapnums:
                if hashmapnums[nums2[i]] > 0:
                    res.append(nums2[i])
                    hashmapnums[nums2[i]] -= 1
                    pass
                pass
            pass
        return res

def main():
    s = Solution()

    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]

    timeStamp1 = time.time()
    print(s.intersect(nums1,nums2))
    timeStamp2 = time.time()
    print(s.intersect1(nums1,nums2))
    timeStamp3 = time.time()
    """
    print(s.findRestaurantForce(list1,list2))
    timeStamp4 = time.time()
    """
    print(timeStamp2-timeStamp1)
    print(timeStamp3-timeStamp2)
    """
    print(timeStamp4-timeStamp3)
    """

if __name__ == '__main__':
    main()
