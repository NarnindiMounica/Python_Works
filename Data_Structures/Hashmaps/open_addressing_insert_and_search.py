class Hashmap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.slots = [None] * self.capacity
        self.values = [None] * self.capacity
        self.size = 0

    def hash_function(self, key):
        return abs(hash(key)) % self.capacity

    def rehash(self, initial_value):
        return (initial_value + 1) % self.capacity
    
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
                    new_hash_value = self.rehash(new_hash_value)

                if self.slots[new_hash_value]==None:  
                    self.slots[new_hash_value] = key
                    self.values[new_hash_value] = value
                else:
                    self.values[new_hash_value] = value 


    def get(self, key):
        initial_index = self.hash_function(key)
        current_position = initial_index

        while self.slots[current_position] is not None:
            if self.slots[current_position]==key:
                return self.values[current_position]

            current_position = self.rehash(current_position)

            if current_position == initial_index:
                return "Not Found, Traversal Completed"

        return "Not Found"

    def delete(self, key):
        initial_index = self.hash_function(key)
        current_position = initial_index

        while(self.slots[current_position] is not None):
            if self.slots[current_position] == key:
                self.slots[current_position] = None
                self.values[current_position] = None
                print(f"{key} has been deleted")
                return
            current_position = self.rehash(current_position)

            if current_position == initial_index:
                break

        return "Key not found to delete, traversal completed"

    def __setitem__(self, key, value):
        return self.insert(key, value)

h1 = Hashmap(3)
h1.insert("apple", 10)
h1.insert("banana", 20)
h1.insert("litchi", 30)
h1.delete("litchi")
print(h1.get('banana'))  
print(h1.get('pineapple'))



           