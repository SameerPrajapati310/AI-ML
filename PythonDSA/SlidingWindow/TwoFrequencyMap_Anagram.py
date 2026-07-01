class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False

        need = {}
        for ch in s1:
            need[ch] = need.get(ch, 0) + 1

        window = {}
        i = 0

        for j in range(len(s2)):
            # expand window
            window[s2[j]] = window.get(s2[j], 0) + 1

            # maintain fixed size
            if j - i + 1 > k:
                window[s2[i]] -= 1
                if window[s2[i]] == 0:
                    del window[s2[i]]
                i += 1

            # check permutation
            if j - i + 1 == k:
                if window == need:
                    return True

        return False
s1 = "ab"
s2 = "eidbaooo"
ans = Solution()
print(ans.checkInclusion(s1,s2))