from student import Student
from student import StudentListUtilities
import random
import string


def random_address():
    """Creates a random as address"""
    random_st = "".join([random.choice(string.ascii_lowercase)
                         for _ in range(5)])
    random_st = random_st[0].upper() + random_st[1:]
    random_house_num = "".join([str(random.randint(0, 10)) for _ in range(4)])
    random_apt_num = "".join([str(random.randint(0, 10)) for _ in range(2)])
    random_ad = f"{random_house_num}, {random_st}, {random_apt_num}"
    return random_ad


student1 = Student("Jacob", 12)
student2 = Student("JP", 10)
student3 = Student("Jonathan", 11)
student4 = Student("Francisco", 11)
student5 = Student("Bresy", 11)
student6 = Student("Jasmine", 10)

students = [student1, student2, student3, student4, student5, student6]

print(StudentListUtilities.to_string(students))

print("======= Adding Birthday =======")
try:
    student1.birthday = "11/12/2002"
except ValueError:
    print(f"***Failed to set Birthday {student1.birthday} for {student1.name}***")
try:
    student2.birthday = "13/12/2002"
except ValueError:
    print(f"***Failed to set Birthday {student2.birthday} for {student2.name}***")
try:
    student3.birthday = "11/132/2002"
except ValueError:
    print(f"***Failed to set Birthday {student3.birthday} for {student3.name}***")
try:
    student4.birthday = "11/12/2021"
except ValueError:
    print(f"***Failed to set Birthday {student4.birthday} for {student4.name}***")
try:
    student5.birthday = "5/4/1999"
except ValueError:
    print(f"***Failed to set Birthday {student5.birthday} for {student5.name}***")
try:
    student6.birthday = "4/20/2020"
except ValueError:
    print(f"***Failed to set Birthday {student6.birthday} for {student6.name}***")

print(StudentListUtilities.to_string(students))

StudentListUtilities.sort(students)

print(StudentListUtilities.to_string(students))


"""
Student ID: 1, Name: Jacob, Year: 12, Address: <None>, Phone: (000) 000-0000, Date: 1/1/2020 Classes: Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial
Student ID: 2, Name: JP, Year: 10, Address: <None>, Phone: (000) 000-0000, Date: 1/1/2020 Classes: Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial
Student ID: 3, Name: Jonathan, Year: 11, Address: <None>, Phone: (000) 000-0000, Date: 1/1/2020 Classes: Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial
Student ID: 4, Name: Francisco, Year: 11, Address: <None>, Phone: (000) 000-0000, Date: 1/1/2020 Classes: Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial
Student ID: 5, Name: Bresy, Year: 11, Address: <None>, Phone: (000) 000-0000, Date: 1/1/2020 Classes: Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial
Student ID: 6, Name: Jasmine, Year: 10, Address: <None>, Phone: (000) 000-0000, Date: 1/1/2020 Classes: Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial

======= Adding Birthday =======
***Failed to set Birthday 1/1/2020 for JP***
***Failed to set Birthday 1/1/2020 for Jonathan***
***Failed to set Birthday 1/1/2020 for Francisco***
Student ID: 1, Name: Jacob, Year: 12, Address: <None>, Phone: (000) 000-0000, Date: 11/12/2002 Classes: Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial
Student ID: 2, Name: JP, Year: 10, Address: <None>, Phone: (000) 000-0000, Date: 1/1/2020 Classes: Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial
Student ID: 3, Name: Jonathan, Year: 11, Address: <None>, Phone: (000) 000-0000, Date: 1/1/2020 Classes: Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial
Student ID: 4, Name: Francisco, Year: 11, Address: <None>, Phone: (000) 000-0000, Date: 1/1/2020 Classes: Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial
Student ID: 5, Name: Bresy, Year: 11, Address: <None>, Phone: (000) 000-0000, Date: 5/4/1999 Classes: Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial
Student ID: 6, Name: Jasmine, Year: 10, Address: <None>, Phone: (000) 000-0000, Date: 4/20/2020 Classes: Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial

Student ID: 5, Name: Bresy, Year: 11, Address: <None>, Phone: (000) 000-0000, Date: 5/4/1999 Classes: Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial
Student ID: 1, Name: Jacob, Year: 12, Address: <None>, Phone: (000) 000-0000, Date: 11/12/2002 Classes: Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial
Student ID: 2, Name: JP, Year: 10, Address: <None>, Phone: (000) 000-0000, Date: 1/1/2020 Classes: Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial
Student ID: 3, Name: Jonathan, Year: 11, Address: <None>, Phone: (000) 000-0000, Date: 1/1/2020 Classes: Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial
Student ID: 4, Name: Francisco, Year: 11, Address: <None>, Phone: (000) 000-0000, Date: 1/1/2020 Classes: Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial
Student ID: 6, Name: Jasmine, Year: 10, Address: <None>, Phone: (000) 000-0000, Date: 4/20/2020 Classes: Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial, Tutorial

"""
