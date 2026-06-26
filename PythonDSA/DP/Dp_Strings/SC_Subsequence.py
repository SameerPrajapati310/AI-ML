"""
Finds the Shortest Common Supersequence (SCS) of two strings using
Dynamic Programming.

A Shortest Common Supersequence is the shortest string that contains
both input strings as subsequences. It is constructed by first finding
the Longest Common Subsequence (LCS) and then merging the remaining
characters from both strings.

Algorithm:
1. Compute the LCS DP table.
2. Backtrack through the table:
   - If characters match, include the character once and move diagonally.
   - Otherwise, move in the direction of the larger DP value and include
     the corresponding character.
3. Append any remaining characters from either string.
4. Reverse the collected characters to obtain the final SCS.

Example:
    Input:
        s1 = "abac"
        s2 = "cab"

    LCS = "ab"

    Shortest Common Supersequence = "cabac"
    Length = 5

Time Complexity:
    O(m × n)

Space Complexity:
    O(m × n)

where:
    m = length of s1
    n = length of s2
"""

class SCS:
    def shortestCommonSupersequence(self, s1, s2):
        m = len(s1)
        n = len(s2)

        # Step 1: Build LCS DP table
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Step 2: Backtrack to construct SCS
        ans = []
        i = m
        j = n

        while i > 0 and j > 0:
            if s1[i - 1] == s2[j - 1]:
                ans.append(s1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                ans.append(s1[i - 1])
                i -= 1
            else:
                ans.append(s2[j - 1])
                j -= 1

        # Append remaining characters
        while i > 0:
            ans.append(s1[i - 1])
            i -= 1

        while j > 0:
            ans.append(s2[j - 1])
            j -= 1

        return "".join(reversed(ans))


# Example
s1 = "abac"
s2 = "cab"

obj = SCS()
ans = obj.shortestCommonSupersequence(s1, s2)

print("Shortest Common Supersequence:", ans)
print("Length:", len(ans))