import ctypes  # provides low level arrays


class Dynamic_Array:
    def __init__(self):
        self._length = 0  # counts current number of elements
        self._capacity = 1   # capacity = total number of blocks reserved for elements
        self._A = self._make_array(self._capacity)  # low-level array

    def __getitem__(self, k):
        """It will return an item at index k """
        if not 0 <= k < self._length:
            raise ValueError("Invalid index")
        return self._A[k]

    def append(self, obj):
        """ It will append the object in the array """
        if self._length == self. _capacity:
            self._resize(2*self._capacity)
        self._A[self._length] = obj
        self._length += 1

    def insert(self, obj, index):
        """ It will assign value at a given index """
        if index == self._capacity:         # not enough room
            self._resize(2*self._capacity)   # so double capacity
        if not 0 <= index < self._length:
            raise ValueError("Invalid index")
        for i in range(self._length, index, -1):
            self._A[i] = self._A[i-1]
        self._A[index] = obj
        self._length += 1

    def delete(self, index):
        """ It wil delete the object at given index from the array """
        if (index >= self._length) or (index < 0):
            raise ValueError("Invalid index")
        else:
            for i in range(index, self._length-1):
                self._A[i] = self._A[i+1]
        self._length -= 1

    def print_array_details(self):
        """ It will print the array details """
        print("\n------------------------------------------")
        print(f"The array length is : {self._length}")
        print(f"The capacity of array is :  {self._capacity}")
        print("Array is : ")
        for i in range(self._length):
            print(self._A[i], end=" ")

    def _resize(self, c):
        """Resize internal array to capacity c."""
        B = self._make_array(c)  # new bigger array of size c
        for i in range(self._length):
            B[i] = self._A[i]
        self._A = B  # Now use the bigger array
        self._capacity = c

    def _make_array(self, c):
        return (ctypes.py_object * c)()


A = Dynamic_Array()
A.print_array_details()
A.append(23)
A.append(34)
A.append(35)
A.append(36)
A.append(37)
A.append(38)
A.append(39)
A.append(40)
A.print_array_details()
A.delete(3)
A.print_array_details()
