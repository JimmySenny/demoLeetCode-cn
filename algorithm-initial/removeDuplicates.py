# -*- coding:utf-8 -*-

class Solution:
    def removeDuplicates(self, nums):
        if( len(nums) < 2 ):
            return len(nums);
        i = 0;
        for j in range(1, len(nums)):
            if( nums[i] != nums[j] ):
                #i++;
                i += 1;
                if( j != i ):
                    nums[i] = nums[j];
        
        return i+1;

def main():
    l = [0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5];
    s = Solution();
    print( s.removeDuplicates(l));
    print(l);

if __name__ == '__main__':
    main();