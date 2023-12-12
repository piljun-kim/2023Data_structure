class ArraySet:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def __str__(self):
        return str(self.array[0:self.size])

    def contains(self, e):
        return self.binary_search(0, self.size - 1, e)

    def binary_search(self, left, right, e):
        if (left > right):
            return False

        Ant = (left + right) // 2
        if self.array[Ant] == e:
            return True
        elif self.array[Ant] < e:
            return self.binary_search(Ant + 1, right, e)
        else:
            return self.binary_search(left, Ant - 1, e)

    def insert(self, e):
        if not self.contains(e) and not self.isFull():
            self.array[self.size] = e
            self.size += 1
            self.array[:self.size] = sorted(self.array[:self.size])
        else:
            pass

    def delete(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                self.array[i] = self.array[self.size - 1]
                self.size -= 1
		self.array[:self.size] = sorted(self.array[:self.size])
                break

    def union(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            setC.insert(self.array[i])
        for i in range(setB.size):
            setC.insert(setB.array[i])
        return setC

    def intersect(self, setB):
        setC = ArraySet()
        for i in range(setB.size):
            if self.contains(setB.array[i]):
                setC.insert(setB.array[i])
        return setC

    def difference(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            if not setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC