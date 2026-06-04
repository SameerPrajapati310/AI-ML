class CountSubsetSum:
    def find(self,m,arr,target):
        if m == 0:
            if target == 0 and arr[0] == 0:
                return 2   # include or exclude zero
            if target == 0 or arr[0] == target:
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