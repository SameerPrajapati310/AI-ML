class Heap:
    def __init__(self):
        self.arr = []
        self.current = 0
    def parent(self,i):
        return (i-1)//2
    def right(self,i):
        return i*2 + 2
    def left(self,i):
        return i*2 + 1
    def insert(self,x):
        self.arr.append(x)
        k = self.current
        self.current += 1
        while k != 0 and self.arr[self.parent(k)] > self.arr[k]:
            self.arr[self.parent(k)], self.arr[k] = self.arr[k] ,self.arr[self.parent(k)]
            k = self.parent(k)
    def heapyfy(self,idx):
        while True:
            smaller = idx
            l = self.left(self.current)
            r = self.right(self.current)
            if l > smaller and self.arr[l] < self.arr[smaller]:
                self.arr[l],self.arr[smaller] = self.arr[smaller], self.arr[l]
            if r > smaller and self.arr[r] < self.arr[smaller]:
                self.arr[r], self.arr[smaller] = self.arr[smaller], self.arr[r]
            if smaller == self.current:
                break
            self.current = smaller
    def extract(self):
        mini = self.arr[self.current]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self.current -= 1
        self.heapyfy(0)
        return mini


            
