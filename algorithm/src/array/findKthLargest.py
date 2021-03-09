#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:
    #def findKthLargest(self, nums: List[int], k: int)-> int:
    def findKthLargest(self, nums, k):
        return sorted(nums,reverse=True)[k-1]


def main():
    s = Solution();
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    print( s.findKthLargest(nums,k) );

if __name__ == '__main__':
    main();
