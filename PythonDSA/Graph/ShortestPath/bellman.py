"""
Use Dijkstra when:
    weights are non-negative
    you want fast shortest path
Use Bellman-Ford when:
------NOTE: will only work for directed graph
------in case of unidirected graph convert them into directed.
    graph may contain negative edges
    you need negative cycle detection 
"""

# Dijkstra:TC
# (E+V)logV

# Bellman-Ford: TC
# V×E

edges = [
    [0, 1, 5],
    [1, 2, -2],
    [2, 3, 3],
    [3, 1, -10]
]

n = 4
src = 0

distance = [float('inf')] * n
distance[src] = 0

# Step 1: Relax edges V-1 times
for i in range(n - 1):

    for u, v, wt in edges:

        if distance[u] != float('inf') and distance[u] + wt < distance[v]:

            distance[v] = distance[u] + wt

# Step 2: Detect negative cycle
negative_cycle = False

for u, v, wt in edges:

    if distance[u] != float('inf') and distance[u] + wt < distance[v]:

        negative_cycle = True
        
        break

if negative_cycle:
    print("Negative Cycle Exists")
    print(distance)
else:
    print(distance)


"""
Why Bellman-Ford relaxes edges V-1 times?

Consider a linear graph:

0 ---> 1 ---> 2 ---> 3
      5      2      1

Number of vertices (V) = 4

Shortest path from 0 to 3 is:

0 -> 1 -> 2 -> 3

This path contains 3 edges.

Notice:

V - 1 = 4 - 1 = 3

So the maximum edges required
to reach any node in shortest path
can be at most V-1.

--------------------------------------

How relaxation works:

Initial distance:

[0, inf, inf, inf]

--------------------------------------

Iteration 1:
Using at most 1 edge

0 -> 1 gets updated

distance:

[0, 5, inf, inf]

--------------------------------------

Iteration 2:
Using at most 2 edges

1 -> 2 gets updated

distance:

[0, 5, 7, inf]

--------------------------------------

Iteration 3:
Using at most 3 edges

2 -> 3 gets updated

distance:

[0, 5, 7, 8]

Now shortest paths to all nodes
have been found.

--------------------------------------

Why not V times?

If a path contains V edges,
then some node must repeat.

Repeated node means cycle exists.

Shortest paths never need cycles
(unless there is a negative cycle).

Therefore Bellman-Ford relaxes
all edges exactly V-1 times.
"""