#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import array;

class Solution:
    #def plusOne(self, digits:List[int]) -> List[int]:
    def plusOne(self, digits):
        for i in range(len(digits) -1, -1, -1):
            if( digits[i] != 9):
                digits[i] = digits[i] + 1;
                return digits;
            digits[i] = 0;
        digits = [1] + digits;
        return digits;

    def plusOneStr(self, digits):
        digits = digits[::-1];
        ans = []
        carry = 1
        i = 0
        while i < len(digits) or carry:
            n = digits[i] if i < len(digits) else 0
            n = n + carry
            carry = 1 if n > 9 else 0
            ans.append(int(n%10))
            i += 1

        return ans[::-1]

    
    def plusOneUniversal(self, digits):
        flag = 1;
        res = [];

        for i in range(len(digits)):
            num = digits.pop() + flag;
            if( num > 9 ):
                flag = 1;
                res.append(num%10);
            else:
                flag = 0;
                res.append(num);
        
        # 进位
        if( flag == 1 ):
            res.append(flag);
        #print(res);
        res.reverse();
        #print(res);
        return res;

    def plusOneConvert(self, digits):
        nums_str = "";
        for i in digits:
            nums_str = nums_str + str(i);
        print(nums_str);
        nums_int = int(nums_str) + 1;
        print(nums_int);
        res = [];
        for i in str(nums_int):
            res.append(int(i));
        return res;

    def plusOneLamda(self, digist):
        import functools;
        return [int(num) for num in str(functools.reduce(lambda x, y: x*10+y, digist) + 1)];


def main():
    List = [9,9,9];
    s = Solution();
    print(s.plusOne(List));

    List = [9,9,9];
    print(s.plusOneStr(List));

    List = [9,9,9];
    print(s.plusOneUniversal(List));

    List = [9,9,9];
    print(s.plusOneConvert(List));

    List = [9,9,9];
    print(s.plusOneLamda(List));
    
if __name__ == '__main__':
    main();

#1234567890ABCDEF
