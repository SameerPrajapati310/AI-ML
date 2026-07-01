class Solution:
    def find(self,arr,k):
        window_sum = 0
        ans = -1
        for i in range(len(arr)):
            window_sum += arr[i]
            if i >= k:
                window_sum -= arr[i-k]
            if i >= k-1:
                ans = max(ans,window_sum)
        return ans

arr = [1,4,3,2,6,7]
ans = Solution()
print(ans.find(arr,3))