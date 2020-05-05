from Address import Address

address1 = Address()
try:
    address1.house_num = -123
except ValueError:
    print("House Number must be Positive")
try:
    address1.street_name = 69
except TypeError:
    print("Street Name must be a String")
try:
    address1.apartment_num = 1001
except ValueError:
    print("Apartment number must be between 0-1000")
print(address1)

address2 = Address(123, "B")
print(address2)

address3 = Address(456, "B", 100)
print(address3)

address4 = Address()
try:
    address4.house_num = 123
except ValueError:
    print("House Number must be Positive")
try:
    address4.street_name = "C"
except TypeError:
    print("Street Name must be a String")
try:
    address4.apartment_num = 976
except ValueError:
    print("Apartment number must be between 0-1000")
print(address4)

address5 = Address()
print(address5)

print(f"Between Address: {address2} and Address: {address4}, "
      f"Address: {Address.which_address_closer(address4, address2)} is closer")

"""
House Number must be Positive
Street Name must be a String
Apartment number must be between 0-1000
0 No Street

123 B Street

456 B Street, #100

123 A Street, #976

0 No Street

Between Address: 123 B Street
and Address: 123 C Street, #976
, Address: 123 B Street
is closer
"""