print('Initial GRID')

grid = [
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ]

from collections import deque
time = 0
visited = []
q = deque()
n = len(grid)
m = len(grid[0])
total = 0
for i in range(n):
    print(grid[i])

for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            q.append((i,j))
        elif grid[i][j] != 0:
            total +=1

rotten = 0
dr = [-1,0,1,0]
dc = [0,1,0,-1]

while q:

    rotten += len(q)
    if rotten == total:
        print(time)
    time += 1
    for i in range(len(q)):
        left,right = q.popleft()
        for i in range(4):
            nr = dr[i] + left
            nc = dc[i] + right
            if 0 <= nr < n and 0<= nc<m and grid[nr][nc]==1:
                grid[nr][nc] = 2
                print()
                print('GRID After Each iteration')
                for i in range(n):
                    print(grid[i])
                q.append((nr,nc))
                 


