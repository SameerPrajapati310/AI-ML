class CountSubSetSum:
    def find(self,m,arr,k):
        if m == 0:
            if k == 0 and arr[0] == 0:
                return 2   
            if k == 0 or arr[0] == k:
                return 1
            return 0
        notake = self.find(m-1,arr,k)
        take = 0
        if k - arr[m] >= 0:
           take =  self.find(m-1,arr,k-arr[m])
        return take + notake
    def count(self,arr,k):
        m = len(arr)
        return self.find(m-1,arr,k)

arr = [1, 2, 3, 4, 5]
k = 5

ans = CountSubSetSum()
print(ans.count(arr,k))