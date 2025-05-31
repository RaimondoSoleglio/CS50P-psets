class Jar:
    def __init__(self, capacity=12):
        # we use _ because these are private attributes
        self._capacity = capacity
        if self._capacity < 0:
            raise ValueError()
        self._size = 0

    def __str__(self):
        # this is what is returned with str(jar) - where jar is an object jar = Jar()
        return self.size * "🍪"

    def deposit(self, n):
        self.size += n

        # raise an error if more than capacity
        if self.size > self.capacity:
            raise ValueError()

    def withdraw(self, n):
        self.size -= n

        # raise an error if less than size
        if self.size < 0:
            raise ValueError()

    # the property instead won't have the underscore
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size
