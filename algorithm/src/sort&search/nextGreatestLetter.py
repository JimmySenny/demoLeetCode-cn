#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:
    #def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    def nextGreatestLetterForce(self, letters, target):
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]
    def nextGreatestLetterBinarySearch(self, letters, target):
        left, right = 0, len(letters) - 1
        while(left < right):
            mid = left + (right - left)//2
            print("l,r,m",left, right, mid)
            if(letters[mid] == target):
                left = mid + 1
            elif(letters[mid] < target):
                left = mid + 1
            elif(letters[mid] > target):
                right = mid
        if right < 0:
            return letters[0]
        elif right == len(letters) - 1 and letters[right] <= target:
            return letters[0]
        return letters[right]
        

def main():
    s = Solution()

    letters = ["c", "f", "j"]
    target = "j"
    #target = "z"

    print(s.nextGreatestLetterForce(letters, target))
    print(s.nextGreatestLetterBinarySearch(letters, target))

if __name__ == '__main__':
    main()
