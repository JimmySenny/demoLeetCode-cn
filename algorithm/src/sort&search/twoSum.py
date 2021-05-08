#!/usr/bin/env  python3

class Solution:
#    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #针对有序序列
    def twoSumSort(self, nums, target):
        return self.twoSumBinarySearch(nums, target)
    def twoSumBinarySearch(self, nums, target):
        lenN = len(nums)
        for i in range(len(nums)):
            left, right = i + 1, lenN - 1
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] == target - nums[i]:
                    return [i+1, mid+1]
                elif nums[mid] > target - nums[i]:
                    right = mid - 1
                elif nums[mid] < target - nums[i]:
                    left = mid + 1
        return [-1,-1]
    def twoSumHash1(self, nums, target):
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
        return [-1,-1]                
    def twoSumHase2(self, nums, target):
        hashmap = {}
        #优化twoSumHash1
        for i,num in enumerate(nums):
            print("i,num",i,num)
            j = hashmap.get(target - num)
            if j is not None and i != j:
                return [i,j]
            #没有则添加
            #hashmap[num] = i
            hashmap.setdefault(num,i)
        return [-1,-1]                
def main():
    s = Solution()
    nums = [2,7,11,15]
    target = 9
    print(s.twoSumSort(nums,target))
    print(s.twoSumHash1(nums,target))
    print(s.twoSumHase2(nums,target))

if __name__ == '__main__':
    main()
