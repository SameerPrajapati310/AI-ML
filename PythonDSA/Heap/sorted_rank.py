import heapq
heap = []

arr = [3,21,4,2,1,20]
count = 0
for num in arr:
    heapq.heappush(heap,num)
print(heap)
m = {}
while heap:
    x = heapq.heappop(heap) # To handle duplicate
    if x not in m:
        m[x] = count
        count += 1
print(m)
ans = []
for i in range(len(arr)):
    ans.append(m[arr[i]])

print("=============")
print(arr)
print(ans)
    
