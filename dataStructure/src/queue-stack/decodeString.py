#!/usr/bin/env python3

class Solution:
#    def decodeString(self, s: str) -> str:
    def decodeString(self, s):
        #print(s)
        numStack = []
        strStack = []
        num = 0
        res = ""
        substr = ""
        for c in s:
            if c >= '0' and c <= '9':
                n = int(c)
                num = num * 10 + n;
            elif '[' == c:
                numStack.append(num)
                num = 0;
                strStack.append(res)
                res = ""
            elif ']' == c:
                cur_num = numStack.pop()
                lst_res = strStack.pop()
                #print("cur_num,lst_res,res",cur_num,lst_res,res)
                res = lst_res + cur_num * res
                #print("res",res)
            else:
                res += c
                pass
        return res

def main():
    s = Solution()

    print(s.decodeString("3[a]2[bc]"))
    print(s.decodeString("3[a2[c]]"))
    print(s.decodeString("2[abc]3[cd]ef"))
    print(s.decodeString("abc3[cd]xyz"))

if __name__ == '__main__':
    main()
