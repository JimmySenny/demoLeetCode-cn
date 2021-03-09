#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:
    #def sortColors(self, nums: List[int]) -> None:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        countRed = 0
        countWhite = 0
        countBlue = 0
        switchdic = {0:countRed,1:countWhite,2:countBlue}
        for num in nums:
            switchdic[num] += 1
        print(switchdic)
        for i in range(len(nums)):
            if i < switchdic[0]:
                nums[i] = 0
            elif i < switchdic[0]+switchdic[1]:
                nums[i] = 1
            else:
                nums[i] = 2
        return nums
    def sortColors2(self, nums):
        p0 = 0
        p1 = 0
        for i in range(len(nums)):
            print("pre",i,p0,p1,nums)
            if 1 == nums[i]:
                nums[p1],nums[i] = nums[i],nums[p1]
                p1 += 1
            elif 0 == nums[i]:
                nums[p0],nums[i] = nums[i],nums[p0]
                print("mid:",p0,p1,nums)
                if p0 < p1:
                    nums[p1],nums[i] = nums[i],nums[p1]
                p0 += 1
                p1 += 1
            print("aft:",p0,p1,nums)
        return nums


def main():
    s = Solution();
    nums = [2,0,2,1,1,0]
    print( s.sortColors(nums) );

    nums = [2,0,2,1,1,0]
    print( s.sortColors2(nums) );

if __name__ == '__main__':
    main();
