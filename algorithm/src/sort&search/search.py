#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time

class Solution:
    #def search(self, nums: List[int], target: int) -> int:
    def search(self, nums, target):
        return self.binarySearch(target, nums, 0, len(nums) - 1)
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

    nums = [-1,0,3,5,9,12]
    target = 9

    print(s.search(nums, target))

if __name__ == '__main__':
    main()
