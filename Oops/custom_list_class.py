import ctypes

class CustomList:
    def __init__(self):
        initial_capacity = 1
        self.capacity = initial_capacity
        self.size = 0
        self.array = self.__create_array(self.capacity)

    def __create_array(self, capacity):
        #create a new referential array with given capacity
        return (capacity * ctypes.py_object)()

    def __resize(self, new_capacity):
        new_array=self.__create_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
            self.array = new_array
            self.capacity = new_capacity


    def append(self, item):
        if (self.size == self.capacity):
            self.__resize(2*self.capacity)

        self.array[self.size] = item
        self.size += 1  

    def __len__(self):
        return self.size
my_list = CustomList()
my_list.append(1)
my_list.append(2)
print(my_list)
print(len(my_list))          