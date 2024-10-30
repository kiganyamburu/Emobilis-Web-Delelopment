# def fibonacci(n):
#     if n < 0:
#         return "Please enter a non-negative number"
#     elif n <= 1:
#         return n
#
#     a, b = 0, 1
#     for _ in range(2, n + 1):
#         a, b = b, a + b
#     return b
#
# print(fibonacci(0))
# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(20))

# classes in python

class animals:
    def __init__(self, name, number_legs):
        self.name = name
        self.number_legs = number_legs

    def move(self):
        print("i can walk")

class Dog(animals):
    def sound(self):
        print("I bark")

my_animal = Dog("osama", 4)
my_animal.sound()







































