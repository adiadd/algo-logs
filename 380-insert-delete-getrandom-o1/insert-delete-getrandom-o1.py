class RandomizedSet:

    def __init__(self):
        self.store = {}
        self.values = []
    
    def insert(self, val):
        if val in self.store:
            return False
        
        self.store[val] = len(self.values)
        self.values.append(val)
        return True
    
    def remove(self, val):
        if val not in self.store:
            return False

        indx = self.store[val]
        last = self.values[-1]
        self.values[indx] = last
        self.store[last] = indx
        self.values.pop()
        del self.store[val]
        return True

    def getRandom(self):
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()