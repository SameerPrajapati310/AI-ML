heights = [10, 5, 20, 0, 15]
k = 2

def find(n, heights):
    if n == 0:
        return 0

    ans = float('inf')

    for i in range(1, k + 1):
        if n - i >= 0:
            jump = abs(heights[n] - heights[n - i]) + find(n - i, heights)
            ans = min(ans, jump)

    return ans

print(find(len(heights) - 1, heights))