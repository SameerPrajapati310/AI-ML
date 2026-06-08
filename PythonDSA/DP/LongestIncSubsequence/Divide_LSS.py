class Div_LSS:
    def find(self,idx,pre,m,arr):
        if idx >= len(arr):
            return []
        notake = self.find(idx+1,pre,m,arr)
        take = []
        if pre == -1 or arr[idx]%arr[pre] == 0:
            take = [arr[idx]] + self.find(idx+1,idx,m,arr)
        return take if len(take) > len(notake) else notake

    def table(self,arr):
        m = len(arr)
        return self.find(0,-1,m,arr)
arr = [2,4,10,20,30,8]
ans = Div_LSS()
print(ans.table(arr))
