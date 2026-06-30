"""
There is a robot on an m x n grid. 
The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths 
that the robot can take to reach the bottom-right corner.

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Example : 2
Input: m = 3, n = 7
Output: 28

"""

class Solution:
    def find(self,i,j,m,n):
        if j == m-1 and i == n-1:
            return 1
        if j >= m or i >= n:
            return 0
        down = self.find(i+1,j,m,n)
        right = self.find(i,j+1,m,n)
        return down+right
    def TwoDDP(self,m,n):

        return self.find(0,0,m,n)
ans = Solution()
print(ans.TwoDDP(3,7))

