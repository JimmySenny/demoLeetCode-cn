#!/usr/bin/env python3

class Solution:
#    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    def floodFillBFS(self, image, sr, sc, newColor):
        # 起始颜色和目标颜色相同，则直接返回原图
        if newColor == image[sr][sc]:
            return image;
        # 设置四个方向偏移量，一种常见的省事儿技巧
        directions = {(1,0),(-1,0),(0,1),(0,-1)}
        # 构造一个队列，先把起始点放进去
        que = []
        que.append((sr,sc))
        # 记录初始颜色
        oriColor = image[sr][sc]
        while que:
            point = que.pop(0)
            image[point[0]][point[1]] = newColor
            # 遍历四个方向
            #for new_i, new_j in zip((point[0], point[0], point[0] + 1, point[0] - 1), (point[1] + 1, point[1] - 1, point[1], point[1])): 
            for direction in directions:
                # 新点是(new_i,new_j)
                new_i = point[0] + direction[0]
                new_j = point[1] + direction[1]
                # 如果这个点在定义域内并且它和原来的颜色相同 则入队
                if 0 <= new_i < len(image) and 0 <= new_j < len(image[0]) and image[new_i][new_j] == oriColor:
                    que.append((new_i,new_j))
        return image
    def DFS(self, image, si, sj, oriColor,newColor):
        if 0 <= si < len(image) and 0 <= sj < len(image[0]) and image[si][sj] == oriColor:
            image[si][sj] = newColor;
            self.DFS(image,si,sj+1,oriColor,newColor)
            self.DFS(image,si,sj-1,oriColor,newColor)
            self.DFS(image,si-1,sj,oriColor,newColor)
            self.DFS(image,si+1,sj,oriColor,newColor)
        return

    def floodFillDFS(self, image, sr, sc, newColor):
        if newColor == image[sr][sc]:
            return image;
        oriColor = image[sr][sc]
        self.DFS(image,sr,sc,oriColor,newColor)
        return image
    def floodFillRes(self, image, sr, sc, newColor):
        if image[sr][sc] != newColor:
            oriColor = image[sr][sc]
            image[sr][sc] = newColor
            for i,j in zip((sr+1,sr-1,sr,sr),(sc,sc,sc+1,sc-1)):
                if 0 <= i < len(image) and 0 <= j < len(image[0]) and image[i][j] == oriColor:
                    self.floodFillRes(image,i,j,newColor)
        return image

def main():
    s = Solution()
    image = [[3,1,1],[1,1,0],[1,0,1]]
    print(image,image[0])
#    s.floodFillBFS(image,1,1,2)
    s.floodFillDFS(image,1,1,2)
#    s.floodFillRes(image,1,1,2)
    print(image[0])
    print(image[1])
    print(image[2])

if __name__ == '__main__':
    main()
