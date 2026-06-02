height = [7, 5, 1, 2, 6]
ans = float('inf')
dp = [-1]*(len(height)+1)

def find(n,height,dp):
    if n == 0:
        return 0
    if n < 0 :
        return float('inf')
    if dp[n] != -1:
        return dp[n]
    

    one = find(n-1,height,dp) + abs(height[n-1]-height[n])
    two = find(n-2,height,dp) + abs(height[n-2]-height[n])


    dp[n] = min(one,two)
    return dp[n]

print(find(4,height,dp))
