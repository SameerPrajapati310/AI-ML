edges = [
    [0, 1, 2],
    [0, 2, 1],
    [1, 2, 1],
    [2, 3, 2],
    [3, 4, 1],
    [4, 2, 2]
]

n = 5

parent = []
rank = []
for i in range(n):
    parent.append(i)

for i in range(n):
    rank.append(0)

def FindUpar(node):
    if node == parent[node]:
        return node
    parent[node] = FindUpar(parent[node])
    return parent[node]

def Union(u,v):
    ulp_u = FindUpar(u)
    ulp_v = FindUpar(v)

    if ulp_u == ulp_v:
        return ulp_u
    if rank[ulp_u] < rank[ulp_v]:
        parent[ulp_u] = ulp_v
    elif rank[ulp_u] > rank[ulp_v]:
        parent[ulp_v] = ulp_u
    else:
        parent[ulp_u] = ulp_v
        rank[ulp_v]+= 1

edges.sort(key=lambda x : x[2])

print(edges)

mst = []
mst_weights = 0

for u,v,wt in edges:
    if FindUpar(u) != FindUpar(v):
        mst_weights += wt
        mst.append((u,v,wt))
        Union(u,v)

print("MST Weight:", mst_weights)
print("MST Edges:")

for edge in mst:
    print(edge)