adict = ["baa","abcd","abca","cab","cad"]
adj = []
for _ in range(26):
    adj.append([])

print(adj)
present = set()

for word in adict:
    for ch in word:
        present.add(ch)

for i in range(len(adict)-1):
    s1 = adict[i]
    s2 = adict[i+1]

    length = min(len(s1), len(s2))

    for j in range(length):
        if s1[j] != s2[j]:
            u = ord(s1[j]) - ord('a')
            v = ord(s2[j]) - ord('a')
            adj[u].append(v)
            break
print(adj)
from collections import deque

indegree = [0]*26

for i in range(26):
    for it in adj[i]:
        indegree[it] += 1

q = deque()

for ch in present:
    idx = ord(ch) - ord('a')
    if indegree[idx] == 0:
        q.append(idx)

ans = []

while q:
    node = q.popleft()
    ans.append(chr(node + ord('a')))

    for it in adj[node]:
        indegree[it] -= 1
        if indegree[it] == 0:
            q.append(it)

print(ans)