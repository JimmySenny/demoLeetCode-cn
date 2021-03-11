#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:
    #def maxArea(self, height: List[int]) -> int:
    def maxArea(self, height):
        i, j = 0, len(height) - 1;
        ans = 0
        while i < j:
            area = min(height[i], height[j]) * (j - i);
            ans = max(ans, area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans

def main():
    s = Solution();

    height = [1,8,6,2,5,4,8,3,7]

    print(s.maxArea(height))

if __name__ == '__main__':
    main();


