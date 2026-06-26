"""
A frog is standing on the first stone (index 0) and wants to reach the last stone.

The height of each stone is given in an array `height[]`.

The frog can make either:
1. A jump to the next stone (i -> i + 1), or
2. A jump by skipping one stone (i -> i + 2).

The energy consumed for a jump from stone `i` to stone `j` is:

    abs(height[i] - height[j])

Your task is to find the minimum total energy required for the frog to reach
the last stone.

Example:
    Input:
        height = [7, 5, 1, 2, 6]

    Output:
        9

    Explanation:
        The optimal path is:
            0 -> 1 -> 3 -> 4

        Energy cost:
            |7 - 5| + |5 - 2| + |2 - 6|
            = 2 + 3 + 4
            = 9

Constraints:
    1 <= len(height) <= 10^5
    1 <= height[i] <= 10^4
"""




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
