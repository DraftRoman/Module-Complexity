class LruCache:
    def __init__(self, limit: int):
        if limit <= 0:
            raise ValueError("Limit must be greater than 0")
        self.limit = limit
        self.cache = {}
        self.order = []

    def get(self, key):
        if key not in self.cache:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache) >= self.limit:
                lru_key = self.order.pop(0)
                del self.cache[lru_key]

            self.cache[key] = value
            self.order.append(key)

    def set(self, key, value):
        self.put(key, value)