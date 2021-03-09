#!/usr/bin/env python3
# -*- codiong:utf-8 -*-

class Solution:
    #def moveZeroes(self, nums: List[int]) -> None:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        for i in range(len(nums)):
            if 0 == nums[i]:
                i += 1
            else:
                nums[j] = nums[i]
                i += 1
                j += 1
        print(nums)
        while j < len(nums):
            nums[j] = 0
            j += 1
        return nums

def main():
    s = Solution()
    nums = [0,1,0,3,12]
    print(s.moveZeroes(nums))
    

if __name__ == '__main__':
    main()
