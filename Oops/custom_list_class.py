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

    def __str__(self):
        output_str = ''
        for i in range(self.size):
            output_str = output_str+str(self.array[i])+","
        return f"[{output_str[:-1]}]"

    def pop(self):
        if self.size==0:
            print("Empty List")
        popped_item = self.array[self.size-1]
        self.size = self.size-1 

    def __getitem__(self, index):
        if index >= 0 and index < self.size:
            return self.array[index]
        else:
            return "Index Error: Index out of range"  

    def clear(self):
        self.size = 0  

    def insert(self, item, position):
        if self.size == self.capacity:
            self.__resize(2*self.capacity)
        for i in range(self.size, position,-1):
            self.array[i] = self.array[i-1]  
        self.array[position] = item
        self.size += 1 

    def remove(self, item):
        for i in range(self.size):
            if int(self.array[i]) == int(item):
                pos = i
                for i in range(pos+1, self.size):
                    self.array[i-1] = self.array[i]
        self.size -= 1   

my_list = CustomList()
my_list.append(1)
my_list.append(2)
print(my_list)
print(len(my_list))
print(my_list[1])
my_list.insert(3,2)
print(my_list)
my_list.remove(2) 
print(my_list)

        