""""Test 1 Jacob B."""


class Address:
    # Class Constants
    DEFAULT_HOUSE_NUM = 0
    DEFAULT_ST_NAME = "No"
    DEFAULT_APT = None
    POSITIVE_MIN = 0
    MAX_APT = 1000

    def __init__(self, h_num=DEFAULT_HOUSE_NUM,
                 st=DEFAULT_ST_NAME, apt=DEFAULT_APT):
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
        if new_apt is not None and (cls.POSITIVE_MIN < new_apt < cls.MAX_APT):
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
        if new_num > cls.POSITIVE_MIN:
            return True
        # else
        return False

    def __str__(self):
        """Returns everything into string and printed in client"""
        if self._apt_num is None:
            return f"{self._house_num} {self._street_name} Street\n"
        # else
        return f"{self._house_num} {self._street_name}" \
               f" Street, #{self._apt_num}\n"
