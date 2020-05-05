from dog import dog

dog1 = dog()
dog2 = dog("Phil", -2, "Huskey")
dog3 = dog()
dog4 = dog("Carl")

dog1.name = "Bob"
try:
    dog1.age = 1
except ValueError:
    print("Age must be at least greater than or equal to 0")
dog1.breed = "German Shepard"
dog1.print_info()

dog2.print_info()

dog3.print_info()

try:
    dog4.age = -5
except ValueError:
    print("Age must be at least greater than or equal to 0")
dog4.print_info()

print(f"Number of Dogs: {dog.POPULATION}")

"""
Dog Name: Bob
Dog Age: 1
Dog Breed: German Shepard

Dog Name: Phil
Dog Age: -1
Dog Breed: Huskey

Dog Name: No Name
Dog Age: -1
Dog Breed: No breed

Age must be at least greater than or equal to 0
Dog Name: Carl
Dog Age: -1
Dog Breed: No breed

Number of Dogs: 4
"""