def simle_generator():
    yield 1
    yield 2
    yield 3
num = simle_generator()
print(next(num))

#infinite counter
def all_nums(start = 0):
    while True:
        yield start
        start = start + 1
allNums = all_nums()
for nums in allNums:
    print(nums)
    if nums == 5:
        break

for i in range(1, 11):
    print(i)


def fibonacci(n):
    a, b = 0, 1
    while b<n:
        yield b
        a, b = b, a+b

fibon = fibonacci(100)
for i in fibon:
    print(i)

r = range(1, 16)
for i in r:
    print(i)

#CALLING FUNCTION INSIDE ANOTHER FUNCTION
"""def printHello():
    print("Hello")


def decorator(func):
    print("Before decorating")
    func()
    print("After decorating")

decorator(printHello)
"""

# @DECORATOR
def decorator2(func):
    def wrapper():
        print("Before decorating")
        func()
        print("After decorating")
    return wrapper

@decorator2
def say_hello():
    print("Hello")
say_hello()

"""
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat
def func_repeat(name):
    print("hello", name)

print(func_repeat("Alice"))
"""

print("")
try:
    print(1/0)
    a=[1]
    print(a[2])
except Exception: #order matters
    print("Error occured")
except ZeroDivisionError:
    print("Division by zero")
except IndexError:
    print("Index out of range")


# try -> except -> else -> finally

file = open("file.txt", mode = "a")
file.write(" banana")
#file.close()


#WITH KEYWORD CLOSES THE FILE ITSELF
#with open("file.txt") as f:
 #   txt = f.read()
#print(f.read())


with open('sample.txt') as f:
    txt = f.readlines() #readlines()
    print(txt[1])

with open('sample.txt') as f:
    for i in f:
        print(i)

with open('sample.txt') as f:
    file_contents = f.read(10)
    print(file_contents)


f = open('demo.txt', 'wt')
f.write('hello world')
f.close()


