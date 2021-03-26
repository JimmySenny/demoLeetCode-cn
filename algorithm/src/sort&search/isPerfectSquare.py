#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time

class Solution:
#    def isPerfectSquare(self, num: int) -> bool:
    def isPerfectSquareForce(self, num):
        #  暴力
        if(num < 2):
            return True;
        i = 2
        while i<=num//2:
            if i*i == num:
                return True;
            i += 1;
        return False;

    def isPerfectSquareBinarySearch(self, num):
        # 二分查找
        if(num < 2):
            return True;
        left = 2;
        right = num//2;
        while left <= right:
            x = left + (right-left+1)//2;
            guess = x * x;
            if guess == num:
                return True;
            if guess > num:
                right = x - 1;
            else:
                left = x + 1;
        return False;
    def isPerfectSquare(self, num):
        # 牛顿迭代
        if(num < 2):
            return True;
        x = num // 2
        while x*x > num:
            x = (x + num//x) // 2
        return x * x == num

def main():
    s = Solution();
    
    # 1 < num < 2^31 - 1
    num = 0
    print("num,result:", num,s.isPerfectSquareBinarySearch(num));
    num = 1
    print("num,result:", num,s.isPerfectSquareBinarySearch(num));
    num = 2
    print("num,result:", num,s.isPerfectSquareBinarySearch(num));
    num = 3
    print("num,result:", num,s.isPerfectSquareBinarySearch(num));
    num = 4
    print("num,result:", num,s.isPerfectSquareBinarySearch(num));
    num = 5
    print("num,result:", num,s.isPerfectSquareBinarySearch(num));

if __name__ == '__main__':
    main()
