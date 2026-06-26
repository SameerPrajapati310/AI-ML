"""
Finds the Longest Common Subsequence (LCS) of two strings using
Dynamic Programming (Tabulation) and reconstructs the LCS string.

A subsequence is formed by deleting zero or more characters from a string
without changing the order of the remaining characters. Unlike a substring,
the characters do not need to be contiguous.

Algorithm:
1. Create a DP table of size (m + 1) x (n + 1), initialized with 0.
2. Fill the table:
   - If characters match:
         dp[i][j] = 1 + dp[i-1][j-1]
   - Otherwise:
         dp[i][j] = max(dp[i-1][j], dp[i][j-1])
3. The value at dp[m][n] gives the length of the LCS.
4. Reconstruct the LCS by backtracking from dp[m][n]:
   - If characters match, include the character and move diagonally.
   - Otherwise, move in the direction of the larger neighboring value.
5. Reverse the collected characters to obtain the final LCS.

Example:
    Input:
        s1 = "abc"
        s2 = "ebc"

    DP Table:
          e  b  c
       0  0  0  0
    a  0  0  0  0
    b  0  0  1  1
    c  0  0  1  2

    LCS = "bc"
    Length = 2

Time Complexity:
    O(m × n)

Space Complexity:
    O(m × n)

where:
    m = length of s1
    n = length of s2
"""

# class LCS:
#     def find(self,m,n,s1,s2,dp):
#         if m == 0 or n == 0:
#             return 0
        
#         if dp[m][n] != -1:
#             return dp[m][n]
#         if s1[m] == s2[n]:
#             dp[m][n] = 1 + self.find(m-1,n-1,s1,s2,dp)
#             return dp[m][n]
#         dp[m][n] = max(self.find(m-1,n,s1,s2,dp),self.find(m,n-1,s1,s2,dp))
#         return dp[m][n]

            
        
#     def lcs_find(self,s1,s2,dp):
#         m = len(s1)
#         n = len(s2)
#         return self.find(m-1,n-1,s1,s2,dp)

# s1 = "abc"
# s2 = "ebc"
# dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
# print(dp)
# ans = LCS()
# print(ans.lcs_find(s1,s2,dp))
# for i in dp:
#     print(i)

"""
Tabulation
"""
class DP_tab:
    def lsc_tab(self,s1,s2):
        m = len(s1)
        n = len(s2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        print("Printing LCS")
        ans = "" 
        for i in range(dp[m][n]):
            ans += "#"
        ans = []
        i = m
        j = n
        while i > 0 and j > 0:
            if s1[i-1] == s2[j-1]:
                ans.append(s1[i-1])
                i -= 1
                j -= 1

            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1

        print("".join(reversed(ans)))
        return dp[m][n]
                

s1 = "abc"
s2 = "ebc"
ans = DP_tab()
print(ans.lsc_tab(s1,s2))