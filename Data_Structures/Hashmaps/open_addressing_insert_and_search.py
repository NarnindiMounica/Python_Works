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
            #continue probing until an empty slot is found or key is found    
                while self.slots[new_hash_value] is not None and self.slots[new_hash_value] is not key:
                    new_hash_value = self.rehash(initial_index)

                if self.slots[new_hash_value]==None:  
                    self.slots[new_hash_value] = key
                    self.values[new_hash_value] = value
                else:
                    self.values[new_hash_value] = value 





           