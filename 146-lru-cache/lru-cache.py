from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.max_capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache.get(key, -1)

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
              
        self.cache[key] = value      

        if len(self.cache) > self.max_capacity:
            #  evict least recently used key
            self.cache.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)