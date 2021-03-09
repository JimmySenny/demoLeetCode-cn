#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:
    #def removeDuplicates(self, nums: List[int]) -> int:
    def removeDuplicates(self, nums):
        if( len(nums) < 3 ):
            return len(nums);
        j = 2;
        for i in range(2,len(nums)):
            print("i,nums[i],j,nums[j],nums[j-2]",i,nums[i],j,nums[j],nums[j-2])
            if nums[i] != nums[j-2]:
                nums[j] = nums[i]
                j += 1
        
        return j;

def main():
    s = Solution();
    nums = [0,0,1,1,1,1,2,3,3]
    print( s.removeDuplicates(nums));
    print(nums);

if __name__ == '__main__':
    main();
