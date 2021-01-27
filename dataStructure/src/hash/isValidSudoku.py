#!/usr/bin/env  python3

import time
class Solution:
    #def isValidSudoku(self, board: List[List[str]]) -> bool:
    def isValidSudoku(self, board):
        # 迭代 逐个遍历  按行、列、子数独块建立hashmap
        hashMapRows = [{} for _ in range(9)]
        hashMapColumns = [{} for _ in range(9)]
        hashMapSubBoxes = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if '.' != num:
                    if hashMapRows[i].__contains__(num):
                        return False
                    else:
                        hashMapRows[i][num] = 1
                    if hashMapColumns[j].__contains__(num):
                        return False
                    else:
                        hashMapColumns[j][num] = 1
                    subBoxesindex = (i//3) * 3 + j//3
                    if hashMapSubBoxes[subBoxesindex].__contains__(num):
                        return False
                    else:
                        hashMapSubBoxes[subBoxesindex][num] = 1
        return True                        

def main():
    s = Solution()
    
    b = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

    timeStamp1 = time.time()
    print(s.isValidSudoku(b))
    timeStamp2 = time.time()
    """
    print(s.containsNearbyDuplicate1(nums,k))
    timeStamp3 = time.time()
    print(s.findRestaurantForce(list1,list2))
    timeStamp4 = time.time()
    """
    print(timeStamp2-timeStamp1)
    """
    print(timeStamp3-timeStamp2)
    print(timeStamp4-timeStamp3)
    """

if __name__ == '__main__':
    main()
