#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:
    #def searchRange(self, nums: List[int], target: int) -> List[int]:
    def searchRange(self, nums, target):
        indexLeft = self.binarySearchBoundary(target, nums, "left")
        indexRight = self.binarySearchBoundary(target, nums, "right")
        return [indexLeft, indexRight]

    def binarySearchBoundary(self, target, nums, flag="left"):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            print("l,r,m", left, right, mid)
            if nums[mid] == target:
                if flag == "left":
                    right = mid - 1; # 锁定左边界
                else:
                    left = mid + 1; # 锁定右边界
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        if flag == "left":
            """ 左边界检查合法性 """
            if left >= len(nums) or nums[left] != target:
                return -1
            return left;
        else:
            """ 右边界检查合法性 """
            if right < 0 or nums[right] != target:
                return -1
            return right;


def main():
    s = Solution()

    """
    nums = [5,7,7,8,8,10]
    target = 8
    """
    nums = []
    target = 0

    print(s.searchRange(nums, target))

if __name__ == '__main__':
    main()
