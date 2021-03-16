#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time

class Solution:
    #def myPow(self, x: float, n: int) -> float:
    def myPowRecursion(self, x, n):
        """
        当我们要计算 x^n 时，
        1. 我们可以先递归地计算出 y = x^{ n/2 } ⌊n/2⌋ 向下取整
        2. 根据递归计算的结果，如果 n 为偶数，那么 x^n = y^2 
                               如果 n 为奇数，那么 x^n = y^2 * x 
        3. 递归的边界为 n = 0n=0，任意数的 00 次方均为 1
        每次递归都会使得指数减少一半，因此递归的层数为 O(\log n)O(logn)))

        """
        N = n
        return self.quickPowRe(x,N) if N >= 0 else 1.0 / self.quickPowRe(x, -N)

    def quickPowRe(self, x, N):
        if 0 == N:
            return 1.0
        y = self.quickPowRe(x, N//2)
        return y * y if N % 2 == 0 else y * y * x
    def myPowIteration(self, x, n):
        """
        由于递归需要使用额外的栈空间，我们试着将递归转写为迭代
        借助整数的二进制拆分，就可以得到迭代计算的方法
        """
        return self.quickPowIter(x,n) if n >= 0 else 1.0 / self.quickPowIter(x,n)
    def quickPowIter(self, x, N):
        ans = 1.0
        # 贡献的初始值为 x
        x_contribute = x
        # 在对 N 进行二进制拆分的同时计算答案
        while (N > 0):
            if (N % 2) == 1:
                # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                ans *= x_contribute
            # 将贡献不断地平方
            x_contribute *= x_contribute
            # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
            N //= 2 
        return ans


def main():
    s = Solution()

    x = 2.0
    n = 8

    print("PowRecursion:",s.myPowRecursion(x,n))
    print("PowIteration:",s.myPowIteration(x,n))

if __name__ == '__main__':
    main()
