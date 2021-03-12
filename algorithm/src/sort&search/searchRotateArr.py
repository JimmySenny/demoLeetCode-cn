#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:
    #def search(self, nums: List[int], target: int) -> int:
    def search(self, nums, target):
        #首先找到旋转数组的k，重新排序数组
        k = self.genk(nums)
        self.sortRotateArr(nums, k)
        index = self.binarySearch(target,nums, 0, len(nums) - 1)
        print(k,nums, index)
        ans = -1
        if -1 != index:
            if index + k >= len(nums):
                ans = index + k - len(nums)
            else:
                ans = index + k
        return ans
    def search2(self, nums, target):
        #首先找到旋转数组的k，分别二分查找
        k = self.genk(nums)
        index1 = self.binarySearch(target, nums, 0, k-1)
        index2 = self.binarySearch(target, nums, k, len(nums)-1)
        if -1 == index1 and -1 == index2:
            return -1
        return index1 if index1 > index2 else index2
    def search2(self, nums, target):
        #直接二分查找
        return self.binarySearchX(target, nums, 0, len(nums)-1)
    def genk(self, nums):
        if len(nums) < 2:
            return 0
        for k in range(1,len(nums)):
            if nums[k-1] > nums[k]:
                return k
        return 0
    def sortRotateArr(self, nums, k):
        if k == 0:
            return;
        result = []
        for j in range( k, len(nums), 1):
            result.append(nums[j])
        for j in range(k):
            result.append(nums[j])
        print(result)
        for i in range(len(nums)):
            nums[i] = result[i]
    def binarySearch(self, target, nums, left, right):
        while left <= right:
            mid = left + (right - left) // 2
            #print("l,r,m", left, right, mid)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                return mid
        return -1;

    def binarySearchX(self, target, nums, left, right):
        while left < right:
            mid = left + (right - left) // 2
            print("l,r,m", left, right, mid)
            if nums[mid] == target:
                return mid
            # mid:right 有序
            if nums[mid] < nums[right]:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        if nums[left] == target:
            return left
        return -1;

def main():
    s = Solution()

    nums = [4,5,6,7,0,1,2]
    #nums = [1,3]
    #nums = [1]
    #nums = [3,1]
    target = 0

    print(s.search2(nums, target))

if __name__ == '__main__':
    main()
