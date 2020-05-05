"""Assignment 02 - 09 Jacob B,"""


class phoneNumber:
    # Class Constants
    DEFAULT_NUMBER = "0000000000"

    def __init__(self, phone_num=DEFAULT_NUMBER):
        # Initializes the instance variables
        self._phone_num = phone_num

        # Sanity checks for the phone_number
        try:
            self.phone_number = self._phone_num
        except TypeError:
            self._phone_num = self.DEFAULT_NUMBER

    @property
    def phone_number(self):
        """Getter for the phone number"""
        return self._phone_num

    @phone_number.setter
    def phone_number(self, new_phone_number):
        """Setter for phone number that is inputted"""
        if self.get_valid_num(new_phone_number) is None:
            raise TypeError
        # else
        self._phone_num = self.get_valid_num(new_phone_number)

    @staticmethod
    def extract_digits(new_phone_num):
        """Extracts the numbers in inputted string and adds into new string"""
        extracted_num = ""
        for i in new_phone_num:
            if i.isdigit():
                extracted_num += i
        return extracted_num

    @classmethod
    def get_valid_num(cls, new_phone_num):
        """Checks for the length of the num inputted, returns extracted num"""
        if 10 <= len(new_phone_num) <= 20:
            return cls.extract_digits(new_phone_num)
        return None

    def __str__(self):
        """Returns the digits to be printed in the client code"""
        return f"({self._phone_num[0:3]}) " \
               f"{self._phone_num[3:6]}-" \
               f"{self.extract_digits(self._phone_num)[6:len(self._phone_num)]}"
