#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Solution:
    #def twoSum(self, numbers: List[int], target: int) -> List[int]:
    def twoSum(self, numbers, target):
        # two pointer
        i, j = 0, len(numbers) - 1;
        result = []
        while i < j:
            if numbers[i] + numbers[j] == target:
                result.append(i+1)
                result.append(j+1)
                break;
            elif numbers[i] + numbers[j] > target:
                j -= 1;
            else:
                i += 1;
        return result;
    def twoSum2(self, numbers, target):
        # hash
        hashmap = {}
        result = []
        for i, num in enumerate(numbers):
            j = hashmap.get(target - num);
            if j is not None  and i != j:
                result.append(j+1)
                result.append(i+1)
                break
            hashmap.setdefault(num,i)
        return result;
def main():
    s = Solution();

    numbers = [2,7,11,15]
    target = 18
    print(s.twoSum(numbers,target))
    print(s.twoSum2(numbers,target))

if __name__ == '__main__':
    main();


