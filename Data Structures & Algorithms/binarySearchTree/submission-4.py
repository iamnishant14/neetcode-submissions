class TreeMap:
    
    def __init__(self):
        self.tree = {}
        self.min_val = sys.maxsize
        self.max_val = -1 * sys.maxsize

    def insert(self, key: int, val: int) -> None:
        self.tree[key] = val
        self.min_val = min(self.min_val,key)
        self.max_val = max(self.max_val, key)

    def get(self, key: int) -> int:
        return self.tree.get(key,-1)

    def getMin(self) -> int:
        print(self.min_val)
        return self.tree.get(self.min_val,-1)


    def getMax(self) -> int:
        print(self.max_val)
        return self.tree.get(self.max_val, -1)

    def remove(self, key: int) -> None:
        if key in self.tree:
            del self.tree[key]
        self.update_min_max_key(key)

    def getInorderKeys(self) -> List[int]:
        return sorted(self.tree.keys())
    
    def update_min_max_key(self,key):
        if key == self.min_val:
            self.min_val = sys.maxsize
            for idx,val in self.tree.items():
                self.min_val = min(self.min_val, idx)
        if key == self.max_val:
            self.max_val = -1 * sys.maxsize
            for idx,val in self.tree.items():
                self.max_val = max(self.max_val, idx)
