#!/usr/bin/env  python3

class Solution:
#    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    def intersection(self, nums1, nums2):
        hashset1 = set(nums1)
        hashset2 = set(nums2)

        return hashset1 &  hashset2

def main():
    s = Solution()
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(s.intersection(nums1,nums2))

if __name__ == '__main__':
    main()
