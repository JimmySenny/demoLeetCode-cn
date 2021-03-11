#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Solution:
    #def isPalindrome(self, s: str) -> bool:
    def isPalindrome(self, s):
        # two pointer
        i, j = 0, len(s) - 1;
        while i < j:
            if 'a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z' or '0' <= s[i] <= '9':
                pass
            else:
                i += 1
                continue;

            if 'a' <= s[j] <= 'z' or 'A' <= s[j] <= 'Z' or '0' <= s[j] <= '9':
                pass
            else:
                j -= 1
                continue;

            if(s[i].upper() == s[j].upper() ):
                i += 1;
                j -= 1;
            else:
                return False;

        return True


def main():
    s = Solution();

    string = "A man, a plan, a canal: Panama"
    print(s.isPalindrome(string))

if __name__ == '__main__':
    main();


