#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:
    #def findKthLargest(self, nums: List[int], k: int)-> int:
    def findKthLargest(self, nums, k):
        return sorted(nums,reverse=True)[k-1]
    def findKthLargestMaxHeap(self, nums, k):
        # 构建大顶堆
        print(nums)
        self.buildMaxHeap(nums);
        print(nums)

        # 调整堆结构，第k值即为第k次调整
        for i in range(len(nums) - 1, len(nums) - k, -1):
        #for i in range(len(nums) - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.adjustHeap(nums, 0, i)
        print(nums)
        return nums[0]

    def buildMaxHeap(self, nums):
        for i in range(len(nums)//2 - 1, -1, -1):
            self.adjustHeap(nums, i, len(nums));

    def adjustHeap(self, nums, i, length):
        indexLeft = 2 * i + 1;
        indexRight = 2 * i + 2;
        indexMax = i;
        if(indexLeft < length and nums[indexLeft] > nums[indexMax]):
            indexMax = indexLeft;
        if(indexRight< length and nums[indexRight] > nums[indexMax]):
            indexMax = indexRight;
        if(indexMax != i):
            nums[i], nums[indexMax] = nums[indexMax], nums[i]
            self.adjustHeap(nums, indexMax, length);

def main():
    s = Solution();
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    #print( s.findKthLargest(nums,k) );
    print( s.findKthLargestMaxHeap(nums,k) );

if __name__ == '__main__':
    main();
