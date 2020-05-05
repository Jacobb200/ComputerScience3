"""Assignment4 04 Jacob B."""


class dog:
    # Class Constants
    POPULATION = 0
    DEFAULT_AGE = -1

    def __init__(self, names="No Name", age=-1, breed="No breed"):
        """Initializes instance variables"""
        self._name = names
        self._age = age
        self._breed = breed
        dog.POPULATION += 1

        # Sanity check for age
        try:
            self.age = self._age
        except ValueError:
            self._age = dog.DEFAULT_AGE

    @property
    def name(self):
        """Returns the value in self._name"""
        return self._name

    @name.setter
    def name(self, dog_name):
        """Sets value in sel._name"""
        self._name = dog_name

    @property
    def age(self):
        """Returns value in self._age"""
        return self._age

    @age.setter
    def age(self, new_age):
        """Checks for age to be greater than 0, if not raise ValueError"""
        if new_age <= 0:
            raise ValueError
        self._age = new_age

    @property
    def breed(self):
        """Returns Value in self._breed"""
        return self._breed

    @breed.setter
    def breed(self, new_breed):
        """Sets value in self._breed"""
        self._breed = new_breed

    def print_info(self):
        """Prints all the info about the dog"""
        print(f"Dog Name: {self._name}")
        print(f"Dog Age: {self._age}")
        print(f"Dog Breed: {self._breed}\n")
