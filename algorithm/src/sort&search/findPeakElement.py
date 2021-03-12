#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:
    #def findPeakElement(self, nums: List[int]) -> int:
    def findPeakElement(self, nums):
        return self.binarySearchX(nums, 0, len(nums) - 1)
    def binarySearchX(self, nums, left, right):
        if left == right:
            return left
        mid = left + (right - left) // 2
        if nums[mid] > nums[mid+1]:
            return self.binarySearchX(nums, left, mid)
        return self.binarySearchX(nums, mid+1, right)
    def findPeakElement2(self, nums):
        return self.binarySearch2(nums, 0, len(nums) - 1)
    def binarySearch2(self, nums, left, right):
        while left < right:
            mid = left + (right - left)//2
            print("l,r,m:", left, right, mid)
            if nums[mid] > nums[mid+1]:
                right = mid + 1
            elif nums[mid] < nums[mid+1]:
                left = mid + 1
        return left
        

def main():
    s = Solution()

    #nums = [1,2,1,3,5,6,4]
    nums = [1]

    print(s.findPeakElement(nums))
    print(s.findPeakElement2(nums))

if __name__ == '__main__':
    main()
