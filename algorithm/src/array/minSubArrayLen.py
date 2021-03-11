#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:
    #def minSubArrayLen(self, target: int, nums: List[int]) -> int:        
    def minSubArrayLen(self, target, nums):
        # 滑动窗口
        start, end = 0, 0;
        min_len = float("inf")
        total = 0 
        while end < len(nums):
            total += nums[end]
            end += 1
            # 当窗口的和大于目标值时，要让窗口前移
            while total >= target:
                print("--tot, start, end:", total, start, end)
                min_len = min(min_len, end - start)
                total -= nums[start]
                start += 1
            print("tot, start, end:", total, start, end)
        return 0 if min_len > len(nums) else min_len

def main():
    s = Solution();

    nums = [2,3,1,2,4,3]
    target = 7

    print(s.minSubArrayLen(target, nums))

if __name__ == '__main__':
    main();


