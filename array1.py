class MyArray:
    DEFAULT_VALUE = "Tutorial"
    NUMBER_OF_ITEMS = 10

    def __init__(self, items=NUMBER_OF_ITEMS, value=DEFAULT_VALUE, ):
        self._value = value
        self._num_items = items
        self._classes = [self._value for _ in range(self._num_items)]

    def __getitem__(self, index):
        if self.valid_index(index, self._num_items):
            return self._classes[index]
        raise IndexError

    @classmethod
    def valid_index(cls, index, end_length):
        if 0 <= index <= end_length:
            return True
        return False

    def __setitem__(self, index, value):
        if self.valid_index(index, self._num_items):
            if isinstance(value, str) is True:
                self._classes[index] = value
            return TypeError
        return IndexError

    def __str__(self):
        return (str(self._classes).strip('[]')).replace("'", "")
