#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

def isBadVersion(version):
    x = 4
    if version >= x:
        return True
    return False

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.binarySearchLeft(n, 0, n)

    def binarySearchLeft(self, n, left, right):
        while left <= right:
            mid = left + (right - left) // 2
            print("l,r,m", left, right, mid)
            ver = isBadVersion(mid)
            if ver:
                right = mid - 1
            else:
                left = mid + 1
        if left > n:
            return -1
        return left

def main():
    s = Solution()

    num = 5
    print(s.firstBadVersion(num))

if __name__ == '__main__':
    main()
