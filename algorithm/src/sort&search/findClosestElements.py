#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:
    #def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    def findClosestElements2Pointer(self, arr, k, x):
        """
        一个一个删，因为是有序数组，且返回的是连续升序子数组，所以
        每一次删除的元素一定位于边界 ；
        一共 77 个元素，要保留 33 个元素，因此要删除 44 个元素；
        因为要删除的元素都位于边界，于是可以使用 双指针
        对撞的方式确定保留区间，即「最优区间」。
        """
        length = len(arr)
        indexLeft = 0
        indexRight = length - 1
        removeCount = length - k

        while removeCount > 0:
            print("l,r,rmove:",indexLeft,indexRight, removeCount)
            if  x - arr[indexLeft] <= arr[indexRight] - x:
                indexRight -= 1
            else:
                indexLeft += 1

            removeCount -= 1
        return arr[indexLeft:indexLeft+k]
    def findClosestElementsWindow(self, arr, k, x):
        pass

    def findClosestElementsBinarySearch(self, arr, k, x):
        """
        如果目标 x 小于等于有序数组的第一个元素，那么前 k 个元素就是答案。
        如果目标 x 大于等于有序数组的最后一个元素，那么最后 k 个元素就是答案。
        其他情况 参考滑动窗口在  [index-k-1, index+k-1] 区间内， 双指针相逆
            如果 low 小于 0 或者 low 对应的元素比 high 对应的元素更接近 x，那么减小 high 索引
            如果 high 大于最后一个元素的索引 arr.size()-1 或者它比起 low 对应的元素更接近 x ，那么增加 low 索引
            当且仅当 [low, high] 之间恰好有 k 个元素，循环终止]
        """
        length = len(arr)
        indexLeft = 0
        indexRight = length - k

        while indexLeft < indexRight:
            mid = indexLeft + (indexRight - indexLeft) // 2
            if mid + k >= length:
                tmp = arr[length-1]
            else:
                tmp = arr[mid + k]
            print("l,r,m:",indexLeft,indexRight,mid,arr[mid],tmp)
                

            #if abs(x - arr[mid]) > abs(tmp - x):
            if x - arr[mid] > tmp - x:
                indexLeft = mid + 1
            else:
                indexRight = mid

        return arr[indexLeft:indexLeft+k]

def main():
    s = Solution()

    """
    arr = [1,2,3]
    k = 2
    x = 0 
    arr = [1,2,3]
    k = 2
    x = 4 
    arr = [1,2,3,4,5,6]
    k = 2
    x = 4 
    arr = [-2,-1,1,2,3,4,5]
    k = 7
    x = 3
    """
    arr = [-2,-1,1,2,3,4,5]
    k = 7
    x = 3
    print(s.findClosestElements2Pointer(arr, k, x))
    print(s.findClosestElementsBinarySearch(arr, k, x))

if __name__ == '__main__':
    main()
