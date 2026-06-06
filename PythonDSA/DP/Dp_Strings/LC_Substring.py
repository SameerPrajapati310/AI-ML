# class LC_String:
#     def find(self, m, n, count, s1, s2):
#         if m < 0 or n < 0:
#             return count

#         if s1[m] == s2[n]:
#             count = self.find(m-1, n-1, count+1, s1, s2)

#         count1 = self.find(m-1, n, 0, s1, s2)
#         count2 = self.find(m, n-1, 0, s1, s2)

#         return max(count, count1, count2)

#     def lcs(self, s1, s2):
#         return self.find(len(s1)-1, len(s2)-1, 0, s1, s2)


# s1 = "abcjklp"
# s2 = "acjkp"

# obj = LC_String()
# print(obj.lcs(s1, s2))

class tab_lc:
    def find(self,s1,s2):
        m = len(s1)
        n = len(s2)
        count = 0
        print(m," ",n)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for it in dp:
            print(it)
        for i in range(1,m+1):
            for j in range(1,n+1):
                print(s1[i-1]," ",s2[j-1])
                if s1[i-1] == s2[j-1]:
                    print(i,j)
                    dp[i][j] = 1 + dp[i-1][j-1]
                    count = max(count,dp[i][j])
                    
                else:
                    dp[i][j] = 0
        print("+++++++++++")
        for it in dp:
            print(it)
        return count

s1 = "abcfree"
s2 = "abfreeec" 
ans = tab_lc()
print(ans.find(s1,s2))                  
                
