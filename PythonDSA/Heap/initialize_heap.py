class Heap:
    def __init__(self,size):
        self.arr = [0]*size
        self.current = 0
        self.capacity = size
    def parent(self,i):
        return (i-1)//2
    def left (self,i):
        return 2*i+1
    def right(self,i):
        return 2*i+2
    def insert(self,x):
        self.arr[self.current] = x
        k = self.current
        self.current += 1
        
        while k != 0 and self.arr[self.parent(k)] > self.arr[k]:
            self.arr[self.parent(k)], self.arr[k] = self.arr[k], self.arr[self.parent(k)]
            k = self.parent(k)
    def heapify(self,i):
        while True:
            l = self.left(i)
            r = self.right(i)
            smaller = i
            if l < self.current and self.arr[l] < self.arr[smaller]:
                smaller = l
            if r < self.current and self.arr[r] < self.arr[smaller]:
                smaller = r
            if smaller == i:
                break
            self.arr[i],self.arr[smaller] = self.arr[smaller], self.arr[i]
            i = smaller
    def answer(self):
        ans = []
        for i in range(self.current):
            ans.append(self.arr[i])
        return ans
    def top(self):
        if self.current == 0:
            return None
        return self.arr[0]
    def extract(self):
        if self.current == 0:
            return None
        if self.current == 1:
            self.current -= 1
            return self.arr[0]
        mini = self.arr[0]
        self.arr[0] = self.arr[self.current-1]
        self.current -= 1
        self.heapify(0)
        return mini



h = Heap(5)
h.insert(3)
h.insert(4)
h.insert(2)
h.insert(6)


print(h.answer())


            
