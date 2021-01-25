#!/usr/bin/env  python3

class Solution:
#    def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum1(self, nums, target):
        hashmap = {}
        # 生成k为值v为下标的map
        # enumerate(nums)
        for i in range(len(nums)):
            hashmap[nums[i]] = i
            """
            hashmap.setdefault(nums[i], i)
            """
        for i in range(len(nums)):
            j = hashmap.get(target - nums[i])
            if j is not None and i != j:
                return [i,j]
    def twoSum2(self, nums, target):
        hashmap = {}
        #优化twoSum1
        for i,num in enumerate(nums):
            print("i,num",i,num)
            j = hashmap.get(target - num)
            if j is not None and i != j:
                return [i,j]
            #没有则添加
            #hashmap[num] = i
            hashmap.setdefault(num,i)
        
def main():
    s = Solution()
    nums = [2,7,11,15]
    target = 9
    print(s.twoSum1(nums,target))
    print(s.twoSum2(nums,target))

if __name__ == '__main__':
    main()
