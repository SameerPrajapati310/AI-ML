class Solution:
    def hand_of_straight(self,arr,group_size):
        import heapq
        heap = []
        m = {}
        for i in range(len(arr)):
            m[arr[i]] = m.get(arr[i],0) + 1
        heap = list(m.keys())
        heapq.heapify(heap)

        while heap:
            val = heap[0]
            for val in range(val,val+group_size):
                if val not in m:
                    return False
                m[val] -= 1
                if m[val] == 0:
                    if val != heap[0]:
                        return False
                    heapq.heappop(heap)
        return True

arr = [1,2,3,6,2,3,4,7,8]
group_size = 3
ans = Solution()
print(ans.hand_of_straight(arr,group_size))
