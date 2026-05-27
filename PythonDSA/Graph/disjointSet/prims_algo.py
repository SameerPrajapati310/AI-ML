edges = [
    [0, 1, 2],
    [0, 2, 1],
    [1, 2, 1],
    [2, 3, 2],
    [3, 4, 1],
    [4, 2, 2]
]
s = set()
for i in range(len(edges)):
    s.add(edges[i][0])

adj = []
for _ in range(len(s)):
    adj.append([])

for i in range(len(adj)):
    u = edges[i][0]
    v = edges[i][1]
    wt = edges[i][2]
    adj[u].append((v,wt))


import heapq
pq = []
visited = [0]*len(adj)
heapq.heappush(pq,(0,0))
min_sum = 0

while pq:
    wt,node = heapq.heappop(pq)
    if visited[node] == 1:
        continue
    visited[node] = 1
    min_sum += wt
    for it,edwt in adj[node]:
        if not visited[it]:
            heapq.heappush(pq,(edwt,it))

print(min_sum)


