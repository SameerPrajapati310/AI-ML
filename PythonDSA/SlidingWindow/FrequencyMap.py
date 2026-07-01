class Solution:
    def lengthOfLongestSubstring(self,s):
        i = 0
        j = 0
        maxi = 0
        freq = {}
        while j < len(s):
            freq[s[j]] = freq.get(s[j],0) + 1
            while freq[s[j]] > 1:
                freq[s[i]] -= 1
                if freq[s[i]] == 0:
                    del freq[s[i]]
                i+=1
            maxi = max(maxi,j-i+1)
            j+=1
        return maxi
s = "abcabcbb"
ans = Solution()
print(ans.lengthOfLongestSubstring(s))