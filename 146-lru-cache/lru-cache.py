class LRUCache:
    def __init__(self, capacity):
        self.max_capacity = capacity
        self.queue = []
        self.cache = {} # {key: value, key: value}

    def get(self, key):
        
        res = self.cache.get(key, -1)
        if res != -1:
            self.queue.remove(key)
            self.queue.append(key)
        return res

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            # update self.queue
            self.queue.remove(key)
            self.queue.append(key)
        else:
           self.cache[key] = value
           # update self.queue
           self.queue.append(key)

        if len(self.cache) > self.max_capacity:
            #  evict least recently used key
            key = self.queue.pop(0)
            self.cache.pop(key, None)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)