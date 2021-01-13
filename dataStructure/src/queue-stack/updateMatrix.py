#!/usr/bin/env python3

import time

class Solution:
#    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
    def updateMatrixBFS(self, matrix):
        # 多个1，要找出每个1到0的最近曼哈顿距离。由于1到0的距离和0到1的距离一样的，
        # 所以其实我们可以换个思维：找出每个0到1的距离
        m, n = len(matrix), len(matrix[0])
        directions = {(1,0),(-1,0),(0,1),(0,-1)}
        res = [[0] * n for _ in range(m)]
        visted = [[0] * n for _ in range(m)]
        zero_points = []
        update_points = []
        for i in range(m):
            for j in range(n):
                if 0 == matrix[i][j]:
                    zero_points.append((i,j))
                    visted[i][j] = 1
                else:
                    update_points.append((i,j))
        print(zero_points)
        print(update_points)
        step = 0
        while zero_points:
            size = len(zero_points)      
            while size:
                point = zero_points.pop(0)
                i = point[0]
                j = point[1]
                if 1 == matrix[i][j]:
                    res[i][j] = step;
                for direction in directions:
                    new_i = i + direction[0]
                    new_j = j + direction[1]
                    if 0<=new_i<m and 0<=new_j<n and visted[new_i][new_j] != 1:
                        zero_points.append((new_i,new_j))
                        visted[new_i][new_j] = 1
                    else:
                        continue;
                size -= 1;
            step += 1;
        print("res:",res)
        return res;
    def updateMatrixBFS2(self, matrix):
        m, n = len(matrix), len(matrix[0])
        directions = {(1,0),(-1,0),(0,1),(0,-1)}
        res = [[-1] * n for _ in range(m)]
        zero_points = []
        update_points = []
        for i in range(m):
            for j in range(n):
                if 0 == matrix[i][j]:
                    zero_points.append((i,j))
                    res[i][j] = 0
                else:
                    update_points.append((i,j))
        print(zero_points)
        print(update_points)
        while zero_points:
            point = zero_points.pop(0)
            print("point:",point[0], point[1])
            for direction in directions:
                new_i = point[0] + direction[0]
                new_j = point[1] + direction[1]
                if 0<=new_i<m and 0<=new_j<n and -1==res[new_i][new_j]:
                    res[new_i][new_j] = res[point[0]][point[1]] + 1
                    zero_points.append((new_i,new_j))
            print("--res:",res)
        print("res:",res)
        return res
    def updateMatrixBFS3(self, matrix):
        # 对每一个非零元素BFS，找到最近的零元素
        m, n = len(matrix), len(matrix[0])
        directions = {(1,0),(-1,0),(0,1),(0,-1)}
        res = [[0] * n for _ in range(m)]
        zero_points = []
        update_points = []
        for i in range(m):
            for j in range(n):
                if 0 == matrix[i][j]:
                    zero_points.append((i,j))
                else:
                    update_points.append((i,j))
        print(zero_points)
        print(update_points)
        while update_points:
            update_point = update_points.pop(0)
            """
            visted = [[0] * n for _ in range(m)]
            dist = 0
            que = []
            que.append(update_point)
            step = 1
            print("update_point:",update_point[0],update_point[1])
            while que:
                size = len(que)
                point = que.pop(0)
                visted[point[0]][point[1]] = 1
                for direction in directions:
                    new_i = point[0] + direction[0]
                    new_j = point[1] + direction[1]
                    if 0<=new_i<m and 0<=new_j<n and 0==visted[new_i][new_j] and (new_i,new_j) in zero_points:
                        que.append((new_i,new_j))
                        step += 1
            print("step,visted:",step,visted)
            """
    def updateMatrixDP(self, matrix):
        #f(i,j)={1+min(f(i-1,j),f(i,j-1),f(i+1,j),f(i,j+1)) if matrix[i][j]==1
        #       {0                                          if matrix[i][j]==0
        m, n = len(matrix), len(matrix[0])
        dp = [[10000] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if 0 == matrix[i][j]:
                    dp[i][j] = 0
        #左上角
        for i in range(0,m,1):
            for j in range(0,n,1):
                if i-1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
                if j-1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
        print("dp1:",dp)
        #右下角
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i+1 < m:
                    dp[i][j] = min(dp[i][j], dp[i+1][j] + 1)
                if j+1 < n:
                    dp[i][j] = min(dp[i][j], dp[i][j+1] + 1)
        print("dp2:",dp)
        return dp

def main():
    s = Solution()
    matrix = [[0,0,0], [0,1,0], [1,1,1]]
    matrix2 = [[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]
    print(matrix)
#    s.updateMatrixBFS(matrix)
#    s.updateMatrixBFS2(matrix)
    s.updateMatrixDP(matrix)
    s.updateMatrixDP(matrix2)

if __name__ == '__main__':
    main()
