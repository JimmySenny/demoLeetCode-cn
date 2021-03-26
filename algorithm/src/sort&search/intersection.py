#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time

class Solution:
    #def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    def intersection(self, nums1, nums2):
        return self.intersectionBinarySearch(nums1,nums2)
    def intersectionBinarySearch(self, nums1, nums2):
        ans = []
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

def main():
    s = Solution()

    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(s.intersection(nums1, nums2))

if __name__ == '__main__':
    main()
