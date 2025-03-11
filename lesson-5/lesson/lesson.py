# Comprehension
#List Comprehension
#Dictionary comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []
for i in numbers:
    squares.append(i ** 2)
print(squares)

squares2 = [num**2 for num in numbers]
print(squares2)

squareEven = [num**2 for num in numbers if num%2==0 ]
print(squareEven)

a_even = [(val, val**2) for val in numbers if val%2==0]
print(a_even)
b_even = [print(val) for val in numbers if val%2==0]
print(b_even)

a = [num**2 for num in range(1, 11)]
print(a)


def greet():
    print("Hello")
print(greet())

def introduce(name):
    print("Hello,", name)
print(introduce("Lali"))

def add(a, b):
    return a + b
print(add(1, 2))

def greeting(name, message):
    print(f"Hello, {name}, {message}")

print(greeting("Lali", "Good day!"))
print(greeting(message="Good day!", name="Lalula♥"))


#POSITIONAL ONLY
def position_only(x, /, y):
    return x + y

print(position_only(1, y=2))


#KEYWORD ONLY
def key_only(*, x, y):
    return x*y

print(key_only(x=3, y=6))

def demo(x, y, /, a, b, *, z):
    print("Executed")
print(demo(1, 2, 3, 4, z=5))


#ARBITRARY ARGUMENTS
def demoo(*args):
    return sum(args)
print(demoo(1, 2, 3, 4))

def dictin(**kwargs):
    return kwargs
print(dictin(name = "Lali", address = "USA", age = 27))

#LAMBDA FUNCTIONS
squaree = lambda x: x**2;
print(squaree(5))

sumof = lambda x, y: x + y;
print(sumof(2, 3))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def squareofnums(num):
    return num**2

print(list(map(squareofnums, numbers)))
#OR
print(list(map(lambda x: x**2, numbers)))