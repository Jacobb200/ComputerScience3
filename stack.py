"""Assignment 5 - 09 Jacob B."""


class Stack:
    # Class Constants
    DEFAULT_CAPACITY = 1000
    DEFAULT_VALUE = ""
    MIN_CAPACITY = 0
    MAX_CAPACITY = 1000

    def __init__(self, capacity=DEFAULT_CAPACITY, value=DEFAULT_VALUE):
        """Initializes instance variables"""
        self._value = value
        self._capacity = capacity
        self._books = []
        self._tos = ""
        self.top_of_stack()

    def pop(self):
        """Pops the word from stack"""
        if len(self._books) >= 1:
            self._books.pop()
            self.top_of_stack()
        else:
            raise IndexError

    def top_of_stack(self):
        """Check for the top of stack"""
        if len(self._books) >= 1:
            self._tos = self._books[self.__len__() - 1]
        else:
            self._tos = ""

    def push(self, value):
        """Pushes items into the stack"""
        if self.__len__() < self._capacity:
            self._books.append(value)
            self.top_of_stack()
        else:
            raise OverflowError

    @classmethod
    def valid_capacity(cls, new_capacity):
        """Checks for valid capacity"""
        if cls.MIN_CAPACITY < new_capacity < cls.MAX_CAPACITY:
            return True
        return False

    @property
    def capacity(self):
        """Gets and returns the capacity"""
        return self._capacity

    @capacity.setter
    def capacity(self, new_capacity):
        """Sets capacity to new capacity if its valid
        and not less than the previous one"""
        if self.valid_capacity(new_capacity):
            if new_capacity > self._capacity:
                self._capacity = new_capacity
            else:
                raise IndexError
        else:
            raise IndexError

    def __str__(self):
        """Able to return values as strings"""
        return f"Capacity = {self._capacity}\nStack has {self._books} "

    def __len__(self):
        """Able to get the len of the object"""
        return len(self._books)
