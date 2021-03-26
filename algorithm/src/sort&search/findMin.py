#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:
    #def findMin1(self, nums: List[int]) -> int:
    # 不重复
    def findMin1Force(self, nums):
        #首先找到旋转数组的k，分别取最小 O(N)
        k = self.genk(nums)
        val1 = nums[0]
        val2 = nums[k]
        return min(val1,val2)
    def findMin1Sort(self, nums):
        #首先找到旋转数组的k，重新排序数组
        k = self.genk(nums)
        self.sortRotateArr(nums, k)
        print(k, nums)
        return nums[0]
    def findMin1BinarySearch(self, nums):
        # 二分搜索
        return self.binarySearch1(nums, 0, len(nums) - 1)
    def findMin2BinarySearch(self, nums):
    # 可重复
        return self.binarySearch2(nums, 0, len(nums) - 1)
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
    def binarySearch1(self, nums, left, right):
        while left < right:
            mid = left + (right - left) // 2
            print("l,r,m", left, right, mid)
            if nums[mid] == nums[right]:
                right = mid
            elif nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
        return nums[left]
    def binarySearch2(self, nums, left, right):
        while left < right:
            mid = left + (right - left)//2
            if nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
        return nums[left]
def main():
    s = Solution()

    nums1 = [4,5,6,7,0,1,2]
    nums2 = [4,4,4,4,4,4,4,4,0,0,1,2,3,4]

    print(s.findMin1Force(nums1))
    print(s.findMin1BinarySearch(nums1))
    print(s.findMin1Sort(nums1))

    print(s.findMin2BinarySearch(nums1))
if __name__ == '__main__':
    main()
