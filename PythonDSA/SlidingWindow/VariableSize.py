"""
Given an array of positive integers and an integer k, 
find the length of the longest contiguous subarray whose sum is less than or equal to k.
"""

class Solution:
    def find(self,arr,k):
        final = -1
        l = 0
        ans = 0
        for r in range(len(arr)):
            ans += arr[r]
            while ans > k:
                ans -= arr[l]
                l+=1
            final = max(final,r-l+1)
        return final





arr = [1,3,5,2,1,2,1]
k = 8
ans = Solution()
print(ans.find(arr,k))