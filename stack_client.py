from stack import Stack

stack1 = Stack(5)

print(f"After initialization: Length = {len(stack1)}, {stack1}")

stack1.push("Book1")
stack1.push("Book2")
stack1.push("Book3")
stack1.push("Book4")
stack1.push("Book5")
try:
    stack1.push("Book6")
except OverflowError:
    print("***Expected Error: Failed to push another book***")
print(f"After pushing {len(stack1)} books: Length = {len(stack1)}, {stack1}")


stack1.pop()
print(f"After popping: length = {len(stack1)}, {stack1}")

stack1.push("book5")
print(f"After pushing {len(stack1)} books: Length = {len(stack1)}, {stack1}")

try:
    stack1.capacity = 3
except IndexError:
    print(f"Failed to set capacity to 3: Length = {len(stack1)}, {stack1}")

try:
    stack1.capacity = 10
except IndexError:
    print(f"Failed to set capacity to 10: Length = {len(stack1)}, {stack1}")

print(f"After resizing capacity to 10: Length = {len(stack1)}, {stack1}")

stack1.push("Book6")
print(f"After pushing {len(stack1)} books: Length = {len(stack1)}, {stack1}")

"""
After initialization: Length = 0, Capacity = 5
Stack has [] 
***Expected Error: Failed to push another book***
After pushing 5 books: Length = 5, Capacity = 5
Stack has ['Book1', 'Book2', 'Book3', 'Book4', 'Book5'] 
After popping: length = 4, Capacity = 5
Stack has ['Book1', 'Book2', 'Book3', 'Book4'] 
After pushing 5 books: Length = 5, Capacity = 5
Stack has ['Book1', 'Book2', 'Book3', 'Book4', 'book5'] 
Failed to set capacity to 3: Length = 5, Capacity = 5
Stack has ['Book1', 'Book2', 'Book3', 'Book4', 'book5'] 
After resizing capacity to 10: Length = 5, Capacity = 10
Stack has ['Book1', 'Book2', 'Book3', 'Book4', 'book5'] 
After pushing 6 books: Length = 6, Capacity = 10
Stack has ['Book1', 'Book2', 'Book3', 'Book4', 'book5', 'Book6']
"""

