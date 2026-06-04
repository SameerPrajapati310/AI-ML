class CountSubsetSum:
    def find(self,m,arr,target):
        if target == 0:
            return 1
        if m == 0:
            if arr[m] == target:
                return 1
            return 0
        notake = self.find(m-1,arr,target)
        take = 0
        if target - arr[m] >= 0:
            take = self.find(m-1,arr,target-arr[m])
        return take + notake

    def count(self,arr,k):
        m = len(arr)
        return self.find(m-1,arr,k)

arr = [1, 2, 3, 4, 5]
k = 5

ans = CountSubsetSum()
print(ans.count(arr,k))