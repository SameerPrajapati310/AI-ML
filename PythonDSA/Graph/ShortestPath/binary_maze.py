"""Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path."""

"""Input: grid = [[0,1],[1,0]]
Output: 2"""

from collections import deque
grid = [[0,1],[1,0]]
n = len(grid)
m = len(grid[0])
distance = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(float('inf'))
    distance.append(row)
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]
if grid[0][0] == 1 or grid[n-1][n-1] == 1:
    print()
q = deque("No shortest distance available")
q.append((0,0))
distance[0][0] = 1
while q:
    for _ in range(len(q)):
        r,c = q.popleft()
        if r==n-1 and c==m-1:
            print("Shortest distance found:",distance[n-1][m-1])
        for i in range(8):
            nr = dr[i] + r
            nc = dc[i] + c
                    
            if nr >= 0 and nr < n and nc >= 0 and nc < m and grid[nr][nc] == 0:
                if distance[r][c] + 1 < distance[nr][nc]:
                    distance[nr][nc] =  distance[r][c] + 1
                    q.append((nr,nc))