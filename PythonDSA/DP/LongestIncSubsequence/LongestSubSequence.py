# class LIS:
#     def find(self,m,pre,nums,dp):
#         if m >= len(nums):
#             return 0
#         if dp[m][pre+1] != -1:
#             dp[m][pre+1]
#         notake = self.find(m+1,pre,nums,dp)
#         take = float('-inf')
#         if pre == -1 or nums[m] > nums[pre]:
#             take = 1 + self.find(m+1,m,nums,dp)
#         dp[m][pre+1] = max(take,notake)
#         return dp[m][pre+1]
#     def longest(self,m,nums):
#         return self.find(0,-1,nums)


# arr = [1,2,10,20,30]
# m = len(arr)
# dp = [[-1 for _ in range(m+1)] for _ in range(m+1)]
# ans = LIS()
# print(ans.find(0,-1,arr,dp))


" TABULATION APPROACH "

class Tab:
    def tabulation(self, arr):
        n = len(arr)

        dp = [[0]*(n+1) for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for prev in range(i-1, -2, -1):
                notake = dp[i+1][prev+1]
                take = 0
                if prev == -1 or arr[i] > arr[prev]:
                    take = 1 + dp[i+1][i+1]

                dp[i][prev+1] = max(take, notake)

        return dp[0][0]
ans = Tab()
arr = [1,2,10,20,30]
print(ans.tabulation(arr))