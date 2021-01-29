#!/usr/bin/env python3

class Solution:
#    def lengthOfLongestSubstring(self, s: str) -> int:
    def isDuplicate( self, s, start, end, ch ):
        while start < end:
            if(s[start] == ch ):
                return True;
            start += 1
        return False

    def lengthOfLongestSubstringForce(self, s):
        #暴力
        lens = len(s)
        ans = 0
        i = 0
        j = 0
        while i < lens:
            while j < lens:
                if self.isDuplicate(s,i,j,s[j]):
                    break
                j += 1;
            ans = max( ans, j - i)
            if( lens - i < ans ):
                break;
            print(i,j,s[i:j])
            i += 1;
        print("max",ans)
        return ans;
    def lengthOfLongestSubstringWin(self, s):
        #滑动窗口
        if not s:
            return 0
        lookup = set()
        lens = len(s)
        ans = 0
        lp = 0 #左指针
        rp = 0 #右指针
        while lp < lens:
            if lp > 0:
                #碰到重复 左指针向右移动一格，移除一个字符
                lookup.remove(s[lp-1]);
            # 不断地移动右指针
            while rp < lens  and s[rp] not in lookup:
                lookup.add(s[rp])
                rp += 1
            # rp - 1 是实际的右边界
            # right - left + 1  长度即为 (rp - 1) - lp + 1==rp - lp
            ans = max(ans,rp - lp)
            # 切片时，右侧为right + 1 即为 rp - 1 + 1== rp
            print(lp,rp,s[lp:rp])
            lp += 1
        return ans;

def main():
    s = Solution();
    print(s.lengthOfLongestSubstringForce("abcabcbb"))
    print(s.lengthOfLongestSubstringForce("bbb"))
    print(s.lengthOfLongestSubstringForce("pwwkew"))
    print(s.lengthOfLongestSubstringForce(""))

    print(s.lengthOfLongestSubstringWin("abcabcbb"))
    print(s.lengthOfLongestSubstringWin("bbb"))
    print(s.lengthOfLongestSubstringWin("pwwkew"))
    print(s.lengthOfLongestSubstringWin(""))


if __name__ == '__main__':
    main()
