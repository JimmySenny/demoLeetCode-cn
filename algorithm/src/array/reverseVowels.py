#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Solution:
    #def reverseVowels(self, s: str) -> str:
    def reverseVowels(self, s):
        # two pointer
        i, j = 0, len(s) - 1
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        lists = list(s)
        while i < j:
            if lists[i] in vowel:
                pass
            else:
                i += 1
                continue;

            if lists[j] in vowel:
                pass
            else:
                j -= 1
                continue;
    
            lists[i], lists[j] = lists[j], lists[i]
            i += 1
            j -= 1
        return ''.join(lists)

def main():
    s = Solution();

    string = "leetcode"
    print(s.reverseVowels(string))

if __name__ == '__main__':
    main();


