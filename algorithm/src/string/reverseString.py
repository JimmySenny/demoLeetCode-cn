#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 切片
class Solution:
#    def reverseString(self, s: List[str]) -> None:
    def reverseString(self, s):
        #s = s[::-1];
        s[0::] = s[::-1];

def main():
    l = [ "h","e","l","l","o" ];
    s = Solution();
    print( s.reverseString(l) );
    print( l );

if __name__ == '__main__':
    main();
