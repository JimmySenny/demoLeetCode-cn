#!/usr/bin/env  python3

class Solution:
#    def containsDuplicate(self, nums: List[int]) -> bool:
    def containsDuplicate(self, nums):
        hashset = set()
        for i in range(len(nums)):
            if nums[i] in hashset:
                return True
            else:
                hashset.add(nums[i])
        return False

def main():
    s = Solution()
    nums = [1,1,1,3,3,4,3,2,4,2]
    print(s.containsDuplicate(nums))

if __name__ == '__main__':
    main()
