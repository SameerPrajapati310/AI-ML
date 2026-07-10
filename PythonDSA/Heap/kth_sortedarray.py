import heapq
class Solution:
    def KthSorted(self,arr,k):
        heap = []
        for i in range(k+1):
            heapq.heappush(heap,arr[i])
        index = 0
        for i in range(k+1,len(arr)):
            arr[index] = heapq.heappop(heap)
            index+=1
            heapq.heappush(heap,arr[i])
        while heap:
            arr[index] = heapq.heappop(heap)
            index+=1
        return arr
        

arr = [1,2,6,3,10,4]

k = 3
ans = Solution()
print(ans.KthSorted(arr,k))
