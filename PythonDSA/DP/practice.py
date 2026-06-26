class Solution:
    def find(self,n,arr,k):
        if k == 0:
            return True
        if n == 0:
            return arr[n] == k

        notake = self.find(n-1,arr,k)
        take = False
        if arr[n] <= k:
            take = self.find(n-1,arr,k-arr[n])
        ans = take or notake
        return ans

arr = [4,3,5,2]
k = 100

ans = Solution()
print(ans.find(len(arr)-1,arr,k))

