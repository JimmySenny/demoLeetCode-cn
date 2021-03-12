#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:)

class Solution:
    #def guessNumber(self, n: int) -> int:
    def guessNumber(self, n):
        return self.binarySearch(n, 0, n)
    def binarySearch(self, x, left, right):
        guess = 0
        while left <= right:
            mid = left + (right - left) // 2
            print("l,r,m", left, right, mid)
            guess = self.guess(mid)
            if -1 == guess:
                right = mid - 1
            elif 1 == guess:
                left = mid + 1
            elif 0 == guess:
                return mid
        return -1;
    # 测试用
    def guess(self, num):
        pick = 6
        if pick == num:
            return 0
        elif pick < num:
            return -1
        else:
            return 1

def main():
    s = Solution()

    x = 10

    print(s.guessNumber(x))

if __name__ == '__main__':
    main()
