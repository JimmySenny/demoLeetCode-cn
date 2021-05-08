#!/usr/bin/env  python3

import time

class Solution:
    #def findDuplicate(self, nums: List[int]) -> int:
    def findDuplicate(self, nums):
        # 1到n的数字放入n+1个位置
        i, lenN = 0, len(nums)
        # 对应位置放对应数字 满足num[i]==num[num[i]-1]
        while i < lenN:
            while i < lenN and nums[i] != nums[nums[i] - 1]:
                #nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
                a,b = nums [i], nums[nums[i]-1]
                nums[nums[i]-1] = a
                nums[i] = b
            i += 1

        for j in range(lenN):
            if j + 1 != nums[j]:
                return nums[j]
        return -1

def main():
    s = Solution()

    nums = [3,1,3,4,2]

    print(s.findDuplicate(nums));

    """
    print(timeStamp2-timeStamp1)
    print(timeStamp3-timeStamp2)
    """

if __name__ == '__main__':
    main()
