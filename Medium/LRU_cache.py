class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        
        

    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        elif len(self.cache)<self.size:
            self.cache[key] = value

        else:
            self.cache.pop(list(self.cache)[0])
            self.cache[key] = value



from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1
        
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)