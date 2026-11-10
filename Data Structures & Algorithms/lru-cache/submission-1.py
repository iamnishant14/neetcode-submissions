class LRUCache:

    def __init__(self, capacity: int):
        self._cache = dict()
        self._limit = capacity
        

    def get(self, key: int) -> int:
        if key in self._cache:
            val = self._cache.pop(key)
            self._cache[key] = val
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            self._cache.pop(key)
        self._cache[key] = value
        if len(self._cache) > self._limit:
            del self._cache[next(iter(self._cache))]
