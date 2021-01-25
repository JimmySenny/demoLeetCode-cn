#!/usr/bin/env  python3

class Solution:
#    def isHappy(self, n: int) -> bool:
    def isHappy(self, n):
        seen = set()
        """
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.sumDivMod(n)
        return 1 == n
        """
        while 1 != n:
            n = self.sumDivMod(n)
            if n in seen:
                return False
            seen.add(n)
        return False

    def sumDivMod(self, n):
        total_sum = 0
        while n > 0:
            n, dig = divmod(n, 10)
            total_sum += dig**2
        return total_sum


def main():
    s = Solution()
    print(s.isHappy(243))

if __name__ == '__main__':
    main()
