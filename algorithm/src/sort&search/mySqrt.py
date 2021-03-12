#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time

class Solution:
    #def mySqrt(self, x: int) -> int:
    def mySqrt(self, x):
        # 0, 1 平方的特例不适用二分
        if x < 2:
            return x;
        return self.binarySearch(x, 0, x // 2)
    def binarySearch(self, x, left, right):
        guess = 0
        while left <= right:
            mid = left + (right - left) // 2
            print("l,r,m", left, right, mid)
            guess = mid * mid
            if guess > x:
                right = mid - 1
            elif guess < x:
                left = mid + 1
            elif guess == x:
                left = mid + 1
        return right;

def main():
    s = Solution()

    x = 8

    print(s.mySqrt(x))

if __name__ == '__main__':
    main()
