class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0


    def insert(self, key: int, value: int) -> None:
        index = key % self.capacity
        for i,pair in enumerate(self.table[index]):
            if pair[0]==key:
                self.table[index][i] = (key,value)
                return
        pair = (key,value)
        self.table[index].append(pair)
        self.size+=1

        if self.size /self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = key % self.capacity

        for pair in self.table[index]:
            if pair[0]==key:
                return pair[1]
        return -1

    def remove(self, key: int) -> bool:
        index = key % self.capacity

        for i,pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                self.size-=1
                return True
        return False

    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity*=2
        old_table = self.table
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_table:
            for pair in bucket:
                index = pair[0]%self.capacity
                self.table[index].append(pair)
                self.size+=1
        return
