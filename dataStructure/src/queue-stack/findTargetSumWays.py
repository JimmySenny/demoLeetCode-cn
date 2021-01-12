#!/usr/bin/env python3

class Solution:
#    def findTargetSumWays(self, nums: List[int], S: int) -> int:
    def findTargetSumWays(self, nums, S):
        pass
    def findTargetSumWaysDP(self, nums, S):
        numsSum = sum(nums)
        lenNums = len(nums)
        t = numsSum * 2 + 1
        dp = [[ 0 for _ in range(t) ] for _ in range(lenNums) ]
        #初始化
        #首先初始化数组第0行。如果第一个元素为0，则dp[0][total]=2
        #(-0 和+0 都为0，所以先初始化为2) 比如 [0,1,2],
        #目标和为3，则有-0+1+2=3，+0+1+2=3 否则和为±nums[0] 的位置的方案数置为1
        if nums[0] == 0:
            dp[0][numsSum] = 2
        else:
            dp[0][numsSum - nums[0]] = 1
            dp[0][numsSum + nums[0]] = 1

        for i in range(lenNums):
            print(dp[i])
        print("init")

        for i in range(1,lenNums):
            for j in range(t):
                #dp[i][j] = dp[i-1][j-nums[i]] + dp[i-1][j+nums[i]] 
                l = j - nums[i] if j - nums[i] >= 0 else 0
                r = j + nums[i] if j + nums[i] < t else 0
                dp[i][j] = dp[i-1][l] + dp[i-1][r]
                print(l,r,dp[i][j], end=',')
            print("i,dp[i]",i,dp[i])

        for i in range(lenNums):
            print(dp[i])

        return dp[-1][numsSum + S]

def main():
    s = Solution()
    nums = [1, 1, 1, 1, 1]
    tag = 3
    print(s.findTargetSumWaysDP(nums,tag));

if __name__ == '__main__':
    main()
