#!/usr/bin/env  python3

import time
class Solution:
#    def isIsomorphic(self, s: str, t: str) -> bool:
    def isIsomorphic(self, s, t):
        # 双哈希map
        lens = len(s)
        """
        if len(t) != lens:
            return False
        """
        hashmaps2t = {}
        hashmapt2s = {}
        for i in range(lens):
            si = s[i]
            ti = t[i]
            if si in hashmaps2t:
                if ti != hashmaps2t.get(si):
                    return False
            else:
                hashmaps2t.setdefault(si,ti)
            if ti in hashmapt2s:
                if si != hashmapt2s.get(ti):
                    return False
            else:
                hashmapt2s.setdefault(ti,si)
        return True
    def isIsomorphic2(self, s, t):
        # 一哈希map 一哈希set
        # 用一个Map记录s串里已被映射的字母，用一个Set记录t串字母
        hashmaps2t = {}
        hashsett = set()
        for i in range(len(s)):
            si = s[i]
            ti = t[i]
            if si not in hashmaps2t:
                if hashsett.__contains__(ti):
                    return False
                hashmaps2t.setdefault(si,ti)
                hashsett.add(ti)
            else:
                if hashmaps2t.get(si) != ti:
                    return False
        return True

def main():
    s = Solution()

    str1 = "paper"
    str2 = "title"
    start = time.time()
    print(s.isIsomorphic(str1,str2))
    start2 = time.time()
    print(s.isIsomorphic2(str1,str2))
    end = time.time()
    print(end - start2, start2 - start)

if __name__ == '__main__':
    main()
