#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:
    def removeDuplicates(self, nums):
        if( len(nums) < 2 ):
            return len(nums);
        j = 1;
        for i in range(1, len(nums)):
            print("i,nums[i],j,nums[j],nums[j-1]",i,nums[i],j,nums[j],nums[j-1])
            if nums[i] != nums[j-1]:
                nums[j] = nums[i];
                j += 1
        return j;

def main():
    l = [0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5];
    s = Solution();
    print( s.removeDuplicates(l));
    print(l);

if __name__ == '__main__':
    main();
