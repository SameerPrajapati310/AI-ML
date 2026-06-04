class PartitionSum:
    def find(self,m,arr,target):
        if m < 0 :
            return 0
        if m == 0:
            if target == 0 and arr[m] == 0:
                return 2
            if target == 0 or arr[m] == target:
                return 1
            return 0
        notake = self.find(m-1,arr,target)
        take = 0
        if target - arr[m] >= 0:
            take = self.find(m-1,arr,target-arr[m])
        return take + notake
    def partition(self,arr,target):
        m = len(arr)
        return self.find(m-1,arr,target)
        



arr = [1, 1, 2, 3]
diff = 1
total = 0
for i in range(len(arr)):
    total += arr[i]

k = (diff+total)//2
ans = PartitionSum()
print(ans.partition(arr,k))


