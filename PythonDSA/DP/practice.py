class Lcsubstring:
    def find(self,m,n,s,t,dp):
        if m < 0 or n < 0:
            return 0
        if dp[m][n] != -1:
            return dp[m][n]  

        if s[m] == t[n]:
            dp[m][n] = 1 + self.find(m-1,n-1,s,t,dp)
            return dp[m][n]
        dp[m][n] = max(self.find(m-1,n,s,t,dp),self.find(m,n-1,s,t,dp))
        return dp[m][n]

        
    def lcs(self,s,t):
        m = len(s)
        n = len(t)
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1) ]
        for it in dp:
            print(it)
        print("+++++++++")
        for i in range(m+1):
            dp[i][0] = 0
        for j in range(n+1):
            dp[0][j] = 0

        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        for it in dp:
            print(it)
        return dp[m][n]



s1 = "awbct"
s2 = "abewc"

ans = Lcsubstring()


print(ans.lcs(s1,s2))

