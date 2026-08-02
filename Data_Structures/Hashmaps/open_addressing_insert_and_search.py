class Hashmap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.slots = [None]*self.capacity
        self.values = [None]*self.capacity
        self.size = 0

    def hash_function(self, key):
        return abs(hash(key)) % self.capacity

    def rehash(self, initial_value):
        return initial_value + 1
    
    def insert(self, key, value):
        hash_value = self.hash_function(key) 
        initial_index = hash_value

        if self.slots[initial_index] is None:
            self.slots[initial_index] = key
            self.values[initial_index] = value
        else:
            #updat if key is alreday present
            if self.slots[initial_index] == key:
                self.values[initial_index] = value

            else:
                new_hash_value = self.rehash(initial_index)
                 




           