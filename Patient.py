"""Assignment 4 - 10 Jacob B."""


class Patient:
    # Class Constants
    DEFAULT_NAME = "No Name"
    DEFAULT_TEMP = 0
    MIN_LENGTH = 2
    MAX_LENGTH = 40
    MIN_ID = 0
    MAX_ID = 9999
    MIN_TEMP = 88
    MAX_TEMP = 111
    ALARM_TEMP = 103.5

    # Class Variables
    id = 1

    def __init__(self, name=DEFAULT_NAME, temp=DEFAULT_TEMP):
        """Initializes instance variables"""
        self._name = name
        self._id = self.id
        self.update_id()
        self._temp = temp

        # Sanity checks for both temp and name
        try:
            self.name = self._name
        except ValueError:
            self._name = self.DEFAULT_NAME

        try:
            self.temp = self._temp
        except ValueError:
            self._temp = self.DEFAULT_TEMP

    @property
    def name(self):
        """Accessor for name"""
        return self._name

    @name.setter
    def name(self, new_name):
        """Mutator for name while checking if name is valid"""
        if not self.valid_name(new_name):
            raise ValueError
        # else
        self._name = new_name

    @property
    def temp(self):
        """Accessor for temp"""
        return self._temp

    @temp.setter
    def temp(self, new_temp):
        """Mutator for temp while checking if temp is valid"""
        if not self.valid_temp(new_temp):
            raise ValueError
        # else
        self._temp = new_temp

    @classmethod
    def update_id(cls):
        """Updates id"""
        cls.id += 1

    @classmethod
    def alarm_temp(cls, new_temp):
        if new_temp >= cls.ALARM_TEMP:
            return True
        # else
        return False

    @classmethod
    def valid_temp(cls, new_temp):
        """Checks if temp is valid"""
        if cls.MIN_TEMP <= new_temp <= cls.MAX_TEMP:
            return True
        # else
        return False

    @classmethod
    def valid_name(cls, new_name):
        """Checks if name is a valid length"""
        if cls.MIN_LENGTH <= len(new_name) <= cls.MAX_LENGTH:
            return True
        # else
        return False

    def display(self):
        """Displays information that is inputted"""
        if self.alarm_temp(self._temp):
            print("*** urgent: attend immediately***")
        print(f"Name: {self._name}; ID: {self._id}; Temp: {self._temp}°\n")

    @staticmethod
    def sicker_patient(patient1, patient2):
        """ Checks for whichever ever patient is more sick"""
        if patient1.temp > patient2.temp:
            return f"{patient1}, {patient2}"
        else:
            return f"{patient2}, {patient1}"

    def __str__(self):
        """Allows for strings to be printed in client code"""
        if self.alarm_temp(self._temp):
            print("*** urgent: attend immediately***")
        return f"Patient name: {self._name}, ID: {self._id}, " \
               f"Temperature: {self._temp}°\n"
