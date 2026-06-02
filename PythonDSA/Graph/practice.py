import heapq

adj = [[[1,1], [2,6]],[[2,3], [0,1]],[[1,3], [0,6]]]

pq = []
heapq.heappush(pq,(0,0))
distance = [float('inf')]*len(adj)
distance[0] = 0
while pq:
    wt,node = heapq.heappop(pq)
    for it,newwt in adj[node]:
        if wt + newwt < distance[it]:
            distance[it] = wt + newwt
            heapq.heappush(pq,(distance[it],it))
print(distance)


    