class Heap:
    def __init__(self):
        self.arr = []
        self.current = 0
    def __len__(self):
        return self.current
    def parent(self,i):
        return (i-1)//2
    def left(self,i):
        return 2*i + 1
    def right(self,i):
        return 2*i + 2
    def insert(self,x):
        self.arr.append(x)
        k = self.current 
        self.current += 1
        while k != 0 and self.arr[self.parent(k)] > self.arr[k]:
            self.arr[self.parent(k)],self.arr[k] = self.arr[k],self.arr[self.parent(k)]
            k = self.parent(k)
    def hepify(self,i):
        while True:
            smaller = i
            l = self.left(i)
            r = self.right(i)
            if l < self.current and self.arr[l] < self.arr[smaller]:
                smaller = l
            if r < self.current and self.arr[r] < self.arr[smaller]:
                smaller = r
            if smaller == i:
                break
            self.arr[smaller],self.arr[i] = self.arr[i],self.arr[smaller]
            i = smaller
    def extract(self):
        if self.current == 0:
            return None

        if self.current == 1:
            self.current -= 1
            return self.arr.pop()

        mini = self.arr[0]
        self.arr[0] = self.arr.pop()
        self.current -= 1
        self.hepify(0)

        return mini


k = 2
arr = [10,1,2,20,4]

heap = Heap(arr)
ans = -1

for num in arr:
    heap.insert(num)


print(arr)
