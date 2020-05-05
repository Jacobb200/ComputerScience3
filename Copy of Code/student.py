"""Assignment 5 - 02 Jacob B."""
from array1 import MyArray


class Student:
    # Class Constants
    ORIGINAL_DEFAULT_YEAR = 0
    DEFAULT_NAME = "No Name"
    MAX_YEAR = 12
    MIN_YEAR = 0
    ORIGINAL_DEFAULT_GPA = 0.00
    MIN_GPA = 0.0
    MAX_GPA = 5.0

    # Class Variables
    default_year = ORIGINAL_DEFAULT_YEAR
    default_gpa = ORIGINAL_DEFAULT_GPA

    # Class Variables
    next_id = 1

    def __init__(self, name=DEFAULT_NAME, year=None, gpa=None):
        """Initializes instance variables and if it needs default values"""

        if year is None:
            year = self.default_year
        if gpa is None:
            gpa = self.default_gpa
        self._classs = []
        self._id = Student.next_id
        self.update_next_id()
        self._name = name
        self._birthday = self.Date()
        self._phone = self.Phone()
        self._address = self.Address()
        self._classes = MyArray()

        # Sanity checks for year + sets to the default value if years is invalid
        try:
            self.grade = year
        except ValueError:
            self._grade = self.default_year
        # Sanity checks for GPA + sets to the default value if GPA is invalid
        try:
            self.gpa = gpa
        except ValueError:
            self._gpa = self.default_gpa

    @property
    def birthday(self):
        """Gets the birthday and then returns it"""
        return self._birthday

    @birthday.setter
    def birthday(self, new_birthday):
        """Sets the birthday by calling date method in Date class"""
        self._birthday.date = new_birthday

    @property
    def classes(self):
        return self._classes

    def add_class(self, period_num, class_name):
        self._classes[period_num] = class_name

    @property
    def address(self):
        """returns whatever is inside of Adress"""
        return self._address

    @address.setter
    def address(self, random_address):
        """USes split values to set the full address"""
        h, s, a = random_address.split(", ")
        self._address.house_num = h
        self._address.street_name = s
        self._address.apartment_num = a

    @property
    def phone(self):
        """Returns what is inside of phone"""
        return self._phone

    @phone.setter
    def phone(self, new_number):
        """Sets the phone to the new phone that is inputted"""
        self._phone.phone_number = new_number

    @property
    def name(self):
        """Checks Student name if it's a str and sets it to the name if true"""
        return self._name

    @name.setter
    def name(self, new_name):
        """Gets the value in name"""
        self._name = new_name

    @property
    def grade(self):
        """Checks grade if it's within range and sets to grade if true"""
        return self._grade

    @grade.setter
    def grade(self, new_grade):
        """Gets the value in new_grade"""
        if not self.valid_year(new_grade):
            raise ValueError
        # else
        self._grade = new_grade

    @property
    def classs(self):
        """Appends the classes into a string"""
        return self._classs

    @classs.setter
    def classs(self, new_class):
        """Gets the value inside of classes"""
        self._classs.append(new_class)

    @classmethod
    def get_default_year(cls):
        """Gets the default value"""
        return cls.default_year

    @classmethod
    def set_default_year(cls, new_default_year):
        """Sets a new value for """
        if not cls.valid_year(new_default_year):
            raise ValueError
        # else
        cls.default_year = new_default_year

    @classmethod
    def valid_year(cls, new_grade):
        """Checks if new_grade is a valid year"""
        if Student.MIN_YEAR <= new_grade <= Student.MAX_YEAR:
            return True
        # else
        return False

    @classmethod
    def update_next_id(cls):
        """Updates the ID"""
        cls.next_id += 1

    @staticmethod
    def which_student_earlier(s1, s2):
        """Checks for student in higher year and returns that student"""
        if s1.grade < s2.grade:
            return s1.name
        elif s1.grade == s2.grade:
            return min(s1.name, s2.name)
        else:
            return s2.name

    @property
    def gpa(self):
        """returns the gpa"""
        return self._gpa

    @classmethod
    def get_default_gpa(cls):
        """returns the default value in default_gpa"""
        return cls.default_gpa

    @classmethod
    def set_default_gpa(cls, new_gpa):
        """Sets the default value to the new_gpa"""
        if not cls.valid_gpa(new_gpa):
            raise ValueError
        # else
        cls.default_gpa = new_gpa

    @gpa.setter
    def gpa(self, new_gpa):
        """Checks for gpa and sets to new_gpa"""
        if not self.valid_gpa(new_gpa):
            raise ValueError
        # else
        self._gpa = new_gpa

    @classmethod
    def valid_gpa(cls, new_gpa):
        """Checks for a valid Gpa"""
        if cls.MIN_GPA <= new_gpa <= cls.MAX_GPA:
            return True
        # else
        return False

    def same_grade(self, other):
        """Checks whether the students are in the same grade"""
        if self.grade > other.grade:
            return True
        return False

    def print_info(self):
        """Prints out all the info that is provided in methods"""
        self.__str__()

    def __str__(self):
        """Returns all the values as a string"""
        return f"Student ID: {self._id}, Name: {self._name}," \
               f" Year: {self._grade}, Address: {self._address}," \
               f" Phone: {self._phone}, Date: {self._birthday} Classes: " \
               f"{self._classes}"

    def __gt__(self, other):
        """Provides the ability to use >/< etc.
        (like a replacement for which student earlier)"""
        if self.birthday < other.birthday:
            return True
        return False

    class Phone:
        # Class Constants
        DEFAULT_NUMBER = "0000000000"

        def __init__(self, phone_num=DEFAULT_NUMBER):
            # Initializes the instance variables
            self._phone_num = phone_num

            # Sanity checks for the phone_number
            try:
                self.phone_number = self._phone_num
            except TypeError:
                self._phone_num = Student.Phone.DEFAULT_NUMBER

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
                   f"{self._phone_num[6:len(self._phone_num)]}"

    class Address:
        # Class Constants
        DEFAULT_HOUSE_NUM = 0
        DEFAULT_ST_NAME = "No"
        DEFAULT_APT = None
        POSITIVE_MIN = 0
        MAX_APT = 1000

        def __init__(self, h_num=DEFAULT_HOUSE_NUM, st=DEFAULT_ST_NAME,
                     apt=DEFAULT_APT):
            # Initializes instance variables
            self._house_num = h_num
            self._street_name = st
            self._apt_num = apt

            # Sanity Checks for House Value, Street Type, and Apartment Value
            try:
                self.house_num = self._house_num
            except ValueError:
                self._house_num = self.DEFAULT_HOUSE_NUM

            try:
                self.street_name = self._street_name
            except TypeError:
                self._street_name = self.DEFAULT_ST_NAME

            try:
                self.apartment_num = self._apt_num
            except ValueError:
                self._apt_num = self.DEFAULT_APT

        @property
        def house_num(self):
            """Gets the house number"""
            return self._house_num

        @house_num.setter
        def house_num(self, new_num):
            """Checks for valid house num then sets house num"""
            if not self.valid_house_num(new_num):
                raise ValueError
            # else
            self._house_num = new_num

        @property
        def street_name(self):
            """Gets the street name"""
            return self._street_name

        @street_name.setter
        def street_name(self, new_street):
            """Checks for valid street name then sets street name"""
            if not self.valid_street_name(new_street):
                raise TypeError
            # else
            self._street_name = new_street

        @property
        def apartment_num(self):
            """Gets Apartment number"""
            return self._apt_num

        @apartment_num.setter
        def apartment_num(self, new_apt):
            """Checks for valid apartment number then sets apartment number"""
            if not self.valid_apt(new_apt):
                raise ValueError
            # else
            self._apt_num = new_apt

        @staticmethod
        def which_address_closer(address1, address2):
            """Checks for whichever address is closer and then returns that one"""
            if address1.street_name < address2.street_name:
                return address1
            else:
                return address2

        @classmethod
        def valid_apt(cls, new_apt):
            """Checks for valid apartment number"""
            if new_apt is not None and \
                    (cls.POSITIVE_MIN < int(new_apt) < cls.MAX_APT):
                return True
            # else
            return False

        @classmethod
        def valid_street_name(cls, new_street):
            """Checks for valid street name"""
            if type(new_street) is str:
                return True
            # else
            return False

        @classmethod
        def valid_house_num(cls, new_num):
            """Checks for valid house num"""
            if int(new_num) > cls.POSITIVE_MIN:
                return True
            # else
            return False

        def __str__(self):
            if self.valid_street_name(self._street_name) \
                    and self.valid_house_num(self._house_num):
                """Returns everything into string and printed in client"""
                return f"{self._house_num} {self._street_name}" \
                       f" Street, #{self._apt_num}\n"
            else:
                return "<None>"

    class Date:
        """Class Constant for Date"""
        DEFAULT_DATE = "1/1/2020"

        def __init__(self, date=DEFAULT_DATE):
            """Initializes all the instance variables """
            self._date = date

            # Sanity checking for the date
            try:
                self.date = self._date
            except ValueError:
                self._date = Student.Date.DEFAULT_DATE

        @property
        def date(self):
            """Gets the date and returns it"""
            return self._date

        @date.setter
        def date(self, new_date):
            """Checks for validness of the date and sets the date"""
            month, day, year = new_date.split("/")
            if not self.valid_month(int(month)):
                raise ValueError
            if not self.valid_day(int(day)):
                raise ValueError
            if not self.valid_date_year(int(year)):
                raise ValueError
            self._date = new_date

        @classmethod
        def valid_month(cls, month):
            """Checks for Valid Month"""
            if 1 <= month <= 12:
                return True
            return False

        @classmethod
        def valid_day(cls, day):
            """Checks for Valid day"""
            if 1 <= day <= 31:
                return True
            # else
            return False

        @classmethod
        def valid_date_year(cls, year):
            """Checks for Valid year"""
            if 1900 <= year <= 2020:
                return True
            return False

        def __str__(self):
            """Returns date as a string"""
            return f"{self._date}"

        def __gt__(self, other):
            """Allows for ability to use >/< when comparing"""
            month, day, year = self.date.split("/")
            month2, day2, year2 = other.date.split("/")

            if year < year2:
                return True
            elif year == year2:
                if month < month2:
                    return True
                elif month == month2:
                    if day < day2:
                        return True
                    else:
                        return False
                return False
            return False


class StudentListUtilities:
    # Class Constants
    NOT_FOUND = -1

    @staticmethod
    def to_string(student_list):
        """Makes the list into a string"""
        students_string = ""
        for i in range(len(student_list)):
            students_string += str((student_list[i])) + "\n"
        return students_string

    @staticmethod
    def sort(student_list):
        # using bubble sort it will sort the students in order
        for j in range(len(student_list)):
            for i in range(len(student_list) - 1):
                num1 = i
                num2 = i + 1
                if student_list[num1] > student_list[num2]:
                    student_list[num1], student_list[num2] = \
                        student_list[num2], student_list[num1]

    @staticmethod
    def get_largest_index(student_list, unsort_index):
        """Helps find largest index"""
        largest_item = 0
        for j in range(unsort_index + 1):
            if student_list[j] > student_list[largest_item]:
                largest_item = j
        return largest_item

    @classmethod
    def selection_sort(cls, student_list):
        """Uses selection sort in order to sort the list of students"""
        for i in range(len(student_list) - 1, 0, -1):
            largest_item = cls.get_largest_index(student_list, i)
            student_list[i], student_list[largest_item] = \
                student_list[largest_item], student_list[i]

    @classmethod
    def merge_sort(cls, student_list):
        """Uses merge sort in order to sort the list of students"""
        if len(student_list) > 1:
            mid = len(student_list) // 2
            left = student_list[0:mid]
            right = student_list[mid:len(student_list)]
            cls.merge_sort(left)
            cls.merge_sort(right)
            # Items within each list(left, right or the student list)
            left_items = 0
            right_items = 0
            student_list_items = 0
            while left_items < len(left) and right_items < len(right):
                if right[right_items] > left[left_items]:
                    student_list[student_list_items] = left[left_items]
                    left_items += 1
                else:
                    student_list[student_list_items] = right[right_items]
                    right_items += 1
                student_list_items += 1
            # Checks for if any list is empty and anything is left over
            while left_items < len(left):
                student_list[student_list_items] = left[left_items]
                left_items += 1
                student_list_items += 1
            while right_items < len(right):
                student_list[student_list_items] = right[right_items]
                right_items += 1
                student_list_items += 1

    @classmethod
    def linear_search(cls, name, student_list):
        """Does a linear search to find name in student_list"""
        for student in student_list:
            if name is student.name:
                return student_list.index(student)
        return cls.NOT_FOUND

    @staticmethod
    def insertion_sort(student_list):
        """Uses Insertion sort in order to find name in list"""
        for i in range(1, len(student_list)):
            current_value = student_list[i]
            last_sorted_index = i - 1
            while last_sorted_index >= 0 and current_value < \
                    student_list[last_sorted_index]:
                student_list[last_sorted_index + 1] = \
                    student_list[last_sorted_index]
                last_sorted_index -= 1
            student_list[last_sorted_index + 1] = current_value

    @classmethod
    def binary_search_h(cls, student_list, start, end, target):
        """Helper function for binary search"""
        middle = int((start + end) / 2)
        if student_list[middle].name == target:
            return middle
        elif student_list[middle].name < target:
            return cls.binary_search_h(student_list, middle, end, target)
        elif student_list[middle].name > target:
            return cls.binary_search_h(student_list, start, middle, target)
        return cls.NOT_FOUND

    @classmethod
    def binary_search(cls, name, student_list):
        """Uses Binary search in order to find name in list"""
        start = 0
        end = len(student_list) - 1
        return cls.binary_search_h(student_list, start, end, name)
