#!/usr/bin/env  python3

import time
class Solution:
    #def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    def fourSumCount(self, A, B, C, D):
        # 通过分治 分为两组，一组计算两数和及对应的下标组，另一组对应负数
        hashmapSumAB = {}
        hashmapSumCD = {}
        ans = 0

        lens = len(A)
        for i in range(lens):
            for j in range(lens):
                sumab = A[i] + B[j]
                if sumab in hashmapSumAB.keys():
                    #hashmapSumAB[sumab].append((i,j))
                    hashmapSumAB[sumab] += 1
                else:
                    #hashmapSumAB[sumab] = [(i,j)]
                    hashmapSumAB[sumab] = 1

        #print(hashmapSumAB.items())
        for i in range(lens):
            for j in range(lens):
                sumcd = 0-(C[i] + D[j])
                print("i,j C D sumcd",i,j,C[i],D[j],sumcd)
                if sumcd in hashmapSumAB.keys():
                    #ans += len(hashmapSumAB[sumcd])
                    ans += hashmapSumAB[sumcd]
                    #若统计每组
                    #for k in range(len(hashmapSumAB[sumcd])):
        return ans
def main():
    s = Solution()
    nums1 = [ 1, 2]
    nums2 = [-2,-1]
    nums3 = [-1, 2]
    nums4 = [ 0, 2]

    timeStamp1 = time.time()
    print(s.fourSumCount(nums1,nums2,nums3,nums4))
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
