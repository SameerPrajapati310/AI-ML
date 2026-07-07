class Heap:
    def __init__(self,x):
        self.arr = [0]*x
        self.size = x
        self.current = 0
    def parent(self,i):
        return (i-1)//2
    def left(self,i):
        return 2*i + 1
    def right(self,i):
        return 2*i+2
    def insert(self,x):
        self.arr[0] = x
        self.current += 1
        k = self.current
        while k != 0 and self.arr[self.parent(k)] > self.arr[k]:
            self.arr[self.parent(k)], self.arr[k] = self.arr[k],self.arr[self.parent(k)]
            k = self.parent(k)
    def heapify(self,i):
        while True:
            l = self.left(i)
            r = self.right(i)
            smaller = i
            if l < self.current and self.arr[l] > self.arr[smaller]:
                smaller = l
            if r < self.current and self.arr[r] > self.arr[smaller]:
                smaller = r
            if smaller == i:
                break
            self.current[smaller],self.arr[i] = self.arr[i],self.arr[smaller]
            i = smaller
    def extract(self):
        mini = self.arr[0]
        self.arr[0] = self.arr[self.current-1]
        self.heapify(0)
        self.current -= 1
        return mini



