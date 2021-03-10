#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:
    #def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        # 尾插法
        i, j = m - 1, n - 1
        k = m + n - 1
        while k>=0:
            print(k,i,j)
            if i >= 0 and j >= 0:
                if nums1[i] > nums2[j]:
                    nums1[k] = nums1[i]
                    i -= 1
                else:
                    nums1[k] = nums2[j]
                    j -= 1
                k -= 1
            else:
                if j >= 0:
                    nums1[k] = nums2[j]
                    j -= 1
                else:
                    pass
                k -= 1
        return
    def merge2(self, nums1, m, nums2, n):
        # 尾插法
        i, j = m - 1, n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1;
        if j >= 0:
            nums1[0:j+1] = nums2[0:j+1]
        return

def main():
    s = Solution();
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,3,6]
    n = 3

    s.merge(nums1, m , nums2, n);
    print( nums1 );

if __name__ == '__main__':
    main();
