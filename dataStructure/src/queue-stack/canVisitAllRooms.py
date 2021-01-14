#!/usr/bin/env python3

class Solution:
#    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    def canVisitAllRoomsBFS(self, rooms):
        num_rooms = len(rooms) #房间数
        num = 0
        visited = {0} #已访问过的房间 set 无列表
        que = [0] #队列 初始房间
        while que:
            index_room = que.pop(0)
            for key in rooms[index_room]:
                print("index,key:",index_room,key)
                if key not in visited:
                    visited.add(key)
                    que.append(key)
                print("vis:",visited)
            print("que:",que)
            print(num)
            num += 1
        print("num_rooms,num:",num,num_rooms)
        return num_rooms == num
    def canVisitAllRoomsDFS(self, rooms):
        print("DFS")
        num_rooms = len(rooms) #房间数
        visited = {0} #已访问过的房间 set 无列表
        stack = [0] #
        num = 0
        while stack:
            index_room = stack.pop()
            for key in rooms[index_room]:
                print("index,key:",index_room,key)
                if key not in visited:
                    visited.add(key)
                    stack.append(key)
                print("vis:",visited)
            print("stack:",stack)
            print("num:", num)
            num += 1

        print("num_rooms,num:",num,num_rooms)
        return num == num_rooms
    def DFS(self, rooms, index_room,visted):
        print("index,visted:", index_room, visted )
        visted.add(index_room)
        for key in rooms[index_room]:
            if key not in visted:
                print("key:", key)
                self.DFS(rooms, key,visted)
    def canVisitAllRoomsDFSRE(self, rooms):
        print("DFSRE")
        num_rooms = len(rooms) #房间数
        visited = {0}
        self.DFS( rooms, 0, visited )
        return len(visited) == len(rooms)

def main():
    s = Solution()
    rooms = [[1,3],[3,0,1],[2],[0]]
    print(s.canVisitAllRoomsBFS(rooms))
    print(s.canVisitAllRoomsDFS(rooms))
    print(s.canVisitAllRoomsDFSRE(rooms))

if __name__ == '__main__':
    main()
