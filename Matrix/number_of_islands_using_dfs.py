#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
from collections import deque
class Solution:
    def numIslands(self,grid):
        #code here
        r, c = len(grid), len(grid[0])
        on = [[i, j] for i in range(r) for j in range(c) if grid[i][j]]
        dir1 = [[-1, -1], [-1, 0], [-1, 1], [1,0], [1, -1], [1, 1], [0, 1], [0, -1], [0, 0]]
        co = 0
        for x, y in on:
            if grid[x][y] in {0, -1}:
                continue
            
            q = deque()
            q.append([x,y])
            co += 1
            while q:
                x, y = q.popleft()
                grid[x][y] = -1
                for x1, y1 in dir1:
                    x2, y2 = x+ x1 , y+ y1
                    if -1<x2<r and -1<y2<c and grid[x2][y2] == 1:
                        q.append([x2, y2])
                        grid[x2][y2] = -1
        return co

