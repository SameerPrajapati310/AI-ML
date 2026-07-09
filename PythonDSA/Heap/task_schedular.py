class Solution:
    def taskSchedular(self,arr,n):
        from collections import deque
        import heapq
        q = deque()
        heap = []
        freq = {}
        for i in range(len(arr)):
            freq[arr[i]] = freq.get(arr[i],0) + 1
        for k in freq:
            heapq.heappush(heap,(-freq[k],k))
        time = 0
        ans = []
        while len(heap) > 0 or len(q) > 0:
            time += 1
            if heap:
                priority,s = heapq.heappop(heap)
                ans.append(s)
                priority += 1
                if priority != 0:
                    cooldown = time + n
                    q.append((cooldown,priority,s))
            if q:
                cd,p,c = q[0]
                if time == cd:
                    heapq.heappush(heap,(p,c))
                    q.popleft()
        return ans

tasks = ["A","A","A","B","B","B"]
n = 2
ans = Solution()
print(ans.taskSchedular(tasks,n))        