#!/usr/bin/env python3

import time

class Solution:
#    def dailyTemperatures(self, T: List[int]) -> List[int]:
    def dailyTemperatures(self, T):
        #从左向右遍历 暴力
        i = 0;
        j = 0
        lent = len(T);
        ans = [0] * lent
        tmp = 0
        while i < lent - 1:
            tmp = T[i]
            j = i + 1;
            while j < lent:
                if T[j] > tmp:
#                    print("i,j,ans[i]",i,j,j - i)
                    ans[i] = j - i;
                    break;
                j += 1;                        
            i += 1
        return ans;                
    def dailyTemperaturesR(self, T):
        #从右向左遍历
        lent = len(T);
        ans = [0] * lent
        i = lent - 2;
        j = 0
        while i >= 0:
            #j += result[j]是利用已有的结果进行跳跃
            j = i + 1;
            while j < lent:
                if T[j] > T[i]:
                    ans[i] = j - i;
                    break
                if ans[j] == 0:
                    ans[i] = 0
                    break
                j += ans[j]
            i -= 1;
        return ans;
    def dailyTemperaturesStack(self, T):
        #递减栈
        lent = len(T);
        ans = [0] * lent
        stack = []
        i = 0
        tmp = 0
        while i < lent:
            while len(stack) > 0 and T[i] > T[stack[len(stack) - 1]]:
#                print("i,tmp,stack",i,stack[len(stack)-1],stack)
                tmp = stack[len(stack) - 1]
                stack.pop()
                ans[tmp] = i - tmp
            stack.append(i)
            i += 1;
        return ans;

def main():
    s = Solution();
    t = [73, 74, 75, 71, 69, 72, 76, 73]
    time1 = time.time()
    print(s.dailyTemperatures(t));
    time2 = time.time()
    print(s.dailyTemperaturesR(t));
    time3 = time.time()
    print(s.dailyTemperaturesStack(t));
    time4 = time.time()
    print("f1,f2,f3",time2 - time1, time3-time2,time4-time3)

if __name__ == '__main__':
    main()
