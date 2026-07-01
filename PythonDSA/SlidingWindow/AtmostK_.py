"""
Given an array and an integer k, 
find the length of the longest contiguous subarray containing at most k distinct elements.

arr = [1, 4, 5, 2, 1, 1, 5, 2]
k = 3

One valid longest subarray is:
[2, 1, 1, 5, 2]

"""


class Solution:
    def find(self, arr, k):
        m = {}
        l = 0
        ans = -1

        for r in range(len(arr)):
            m[arr[r]] = m.get(arr[r], 0) + 1

            while len(m) > k:
                m[arr[l]] -= 1

                if m[arr[l]] == 0:
                    del m[arr[l]]

                l += 1

            ans = max(ans, r - l + 1)

        return ans


arr = [1, 4, 5, 2, 1, 1, 5, 2]
k = 3

obj = Solution()
print(obj.find(arr, k))