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

for i in range(n):
    parent.append(i)

rank = []

for i in range(n):
    rank.append(0)


def FindUpar(node):

    if node == parent[node]:
        return node

    parent[node] = FindUpar(parent[node])

    return parent[node]


def UnionByRank(u, v):

    ulp_u = FindUpar(u)
    ulp_v = FindUpar(v)

    if ulp_u == ulp_v:
        return

    if rank[ulp_u] < rank[ulp_v]:

        parent[ulp_u] = ulp_v

    elif rank[ulp_v] < rank[ulp_u]:

        parent[ulp_v] = ulp_u

    else:

        parent[ulp_v] = ulp_u

        rank[ulp_u] += 1


# Sort edges based on weight
edges.sort(key=lambda x: x[2])

mst_weight = 0
mst_edges = []

for u, v, wt in edges:

    if FindUpar(u) != FindUpar(v):

        mst_weight += wt
        mst_edges.append([u, v, wt])

        UnionByRank(u, v)

print("MST Weight:", mst_weight)
print("MST Edges:")

for edge in mst_edges:
    print(edge)