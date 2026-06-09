def find(m, target, arr, dp):
    if target == 0:
        return True

    if m == 0:
        return arr[0] == target

    if dp[m][target] != -1:
        return dp[m][target]

    notake = find(m-1, target, arr, dp)

    take = False
    if arr[m] <= target:
        take = find(m-1, target-arr[m], arr, dp)

    dp[m][target] = take or notake
    return dp[m][target]

arr = [4,3,5,2]
k = 6

dp = [[-1]*(k+1) for _ in range(len(arr))]
print(find(len(arr)-1, k, arr, dp))

"""
[1,2,4] k = 3

(2,3)
  |____(1,3)
  |    |____(0,3)
  |       |       |_____False
  |       |____(0,1)
  |       |       |_______True
  |       |______True
  |____(1,-ve)-> never executed
  |          |______False
  |_______True

"""
