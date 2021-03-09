#!/usr/bin/env python3
# -*- codiong:utf-8 -*-

class Solution:
    #def removeElement(self, nums: List[int], val: int) -> int:
    def removeElement(self, nums, val):
        i = 0
        j = 0
        for i in range(len(nums)):
            if val == nums[i]:
                i += 1
            else:
                nums[j] = nums[i]
                i += 1
                j += 1
        print(nums)
        return j

def main():
    s = Solution()
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(s.removeElement(nums,val))
    

if __name__ == '__main__':
    main()
