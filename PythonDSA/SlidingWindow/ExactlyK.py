class Solution:
    def find(self, arr, k):
        m = {}
        l = 0
        ans = 0
        for r in range(len(arr)):
            m[arr[r]] = m.get(arr[r], 0) + 1

            while len(m) > k:
                m[arr[l]] -= 1
                if m[arr[l]] == 0:
                    del m[arr[l]]
                l += 1
            ans += r - l + 1
        return ans


arr = [1,2,4,5,2,2,1,1,2,4]
k = 3

obj = Solution()
print(obj.find(arr, k) - obj.find(arr, k-1))
