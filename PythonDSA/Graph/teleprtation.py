"""
You are given an integer array nums of length n.
You start at index 0, and your goal is to reach index n - 1.
From any index i, you may perform one of the following operations:
Adjacent Step: Jump to index i + 1 or i - 1, if the index is within bounds.
Prime Teleportation: If nums[i] is a prime number p, you may instantly jump 
to any index j != i such that nums[j] % p == 0.
Return the minimum number of jumps required to reach index n - 1.

Example 1:
Input: nums = [1,2,4,6]
Output: 2
Explanation:
One optimal sequence of jumps is:
Start at index i = 0. Take an adjacent step to index 1.
At index i = 1, nums[1] = 2 is a prime number. Therefore, we teleport to index i = 3 as nums[3] = 6 is divisible by 2.
Thus, the answer is 2.

Example 2:
Input: nums = [2,3,4,7,9]
Output: 2
Explanation:
One optimal sequence of jumps is:
Start at index i = 0. Take an adjacent step to index i = 1.
At index i = 1, nums[1] = 3 is a prime number. Therefore, we teleport to index i = 4 since nums[4] = 9 is divisible by 3.
Thus, the answer is 2.
"""

from math import sqrt
from collections import deque

arr = [2,3,4,7,9]
q = deque()
q.append((arr[0],0))
count = 0
visited = [0]*len(arr)

def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


while q:
    for _ in range(len(q)):
        node,idx = q.popleft()
        if idx-1 >= 0 and not visited[idx-1]:
            q.append((arr[idx-1],idx-1))
            visited[idx-1] = 1
        if idx + 1 < len(arr) and not visited[idx-1]:
            q.append((arr[idx+1],idx+1))
            visited[idx+1] = 1
        if isPrime(node):
            for j in range(len(arr)):
                if j == idx:
                    continue
                if arr[j] % node == 0 and not visited[j]:
                    q.append((arr[j],j))
                    visited[j] = 1
                    
        count +=1
        
print(count)


        
    

