#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time

class Solution:
    #def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    def intersection(self, nums1, nums2):
        return self.intersectionBinarySearch(nums1,nums2)
    def intersectionBinarySearch(self, nums1, nums2):
        ans = []
        nums1 = sorted(nums1)
        print("nums1:", nums1)
        for num in nums2:
            print("num:", num)
            if num in ans:
                continue;
            if -1 != self.binarySearch(num, nums1,0, len(nums1)-1):
                ans.append(num)
        return ans

    def binarySearch(self, target, nums, left, right):
        ans = -1
        while left <= right:
            mid = left + (right - left) // 2
            print("l,r,m:",left, right, mid, nums[mid])
            time.sleep(1)

            if target == nums[mid]:
                ans = mid;
                break
            elif nums[left] > target or nums[right] < target:
                break

            if nums[mid] > target:
                right = mid -1;
            elif nums[mid] < target:
                left = mid + 1
        return ans
    def intersection2(self, nums1, nums2):
        # 为了降低空间复杂度，首先遍历较短的数组
        # 并在哈希表中记录每个数字以及对应出现的次数，
        # 然后遍历较长的数组得到交集
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

    #nums1 = [4,9,5]
    #nums2 = [9,4,9,8,4]
    nums1 = [2,1]
    nums2 = [1,1]
    print(s.intersection(nums1, nums2))

    print(s.intersection(nums1, nums2))
if __name__ == '__main__':
    main()
