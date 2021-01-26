#!/usr/bin/env  python3

import time
class Solution:
    #def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    def containsNearbyDuplicate(self, nums, k):
        # 哈希表存储的值和下标列表，根据k判断是否在区间范围
        hashmapnums = {}
        res = []
        for i in range(len(nums)):
            if nums[i] in hashmapnums:
                hashmapnums[nums[i]].append(i)
            else:
                res = [i]
                hashmapnums[nums[i]] = res
        for v in hashmapnums.values():
            #print(v)
            lenv = len(v)
            i = 0
            while lenv - 1 > 0:
                #print("vi",v[i+1],v[i])
                if abs(v[i+1] - v[i]) <= k:
                    return True
                i += 1
                lenv -= 1
                pass
            pass
        return False
    def containsNearbyDuplicate1(self, nums, k):
        # 优化 哈希表存储的值和下标列表，在hash时就判断
        hashmapnums = {}
        for i in range(len(nums)):
            if hashmapnums.__contains__(nums[i]):
                if abs(i - hashmapnums[nums[i]]) <= k:
                    return True
            hashmapnums[nums[i]] = i
        return False

def main():
    s = Solution()

    nums = [1,2,3,1]
    k = 3

    timeStamp1 = time.time()
    print(s.containsNearbyDuplicate(nums,k))
    timeStamp2 = time.time()
    print(s.containsNearbyDuplicate1(nums,k))
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
