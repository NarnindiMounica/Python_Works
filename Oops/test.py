import ctypes
class CustomList:
    def __init__(self):
        initial_capacity = 1
        self.capacity = initial_capacity
        self.size = 0
        self.array = self.__create_array(self.capacity)

    def __create_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def __resize_array(self, new_capacity):
        new_array = self.__create_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]

        self.capacity = new_capacity
        self.array = new_array   


    def append(self, item):
        if self.size == self.capacity:
            self.array = self.__resize_array(2*self.capacity)

        self.array[self.size] = item
        self.size += 1

    def __len__(self):
        return self.size

    def __str__(self):
        output_str = ''
        for i in range(self.size+1):
            output_str = output_str + str(i)+","
        return f"[{output_str[:-1]}]"    

