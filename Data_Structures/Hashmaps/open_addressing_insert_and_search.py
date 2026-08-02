class Hashmap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.slots = [None]*self.capacity
        self.values = [None]*self.capacity
        self.size = 0

    def hash_function(self, key):
        return abs(hash(key)) % self.capacity
    
    def insert(self, key, value):

        hash_value = self.hash_function(key) 
        initial_index = hash_value

           