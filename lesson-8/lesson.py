

class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary  # private-like attribute
        self._email = "<EMAIL>" # protected
    def print_salary(self):
        return self.__salary

person = Person("John", 30, 2500)
print(person.name)
print(person._Person__salary) # access private-like attribute
print(person._email)
print(person.print_salary())

#INHERITANCE
# class ChildClass(ParentClass)

class EmptyClass:
    pass
print(dir(EmptyClass))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print("Eating meal")
    def walk(self):
        print("walking")
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

p1 = Person("John", 30)
print(p1)
p1.eat()
p1.walk()


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def eat(self):
        print("teacher eating meal")
    def teach(self):
        print("teaching")

t = Teacher("Leslie", 25, "Math")
t.eat()
t.teach()


class NUmberList(list):
    def append(self, *args):
        for i in args:
            if not isinstance(i, (int, float)):
                raise ValueError(i)
        super().__init__(args)

a = NUmberList([2,3, 4,5])
a.append(8)
print(a)


#Property

class Person:
    def __init__(self, name, age):
        if not isinstance(name, str) or name =="":
            raise ValueError("name cannot be an empty string")
        self.name = name
        if not isinstance(age, int) or age < 0:
            raise ValueError("age must be a positive integer")
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

p1 = Person("Lalula", 25)
print(p1)
p1.name = -3
print(p1)

class People:
    def __init__(self, name, age):
        if not isinstance(name, str) or name =="":
            raise ValueError("name cannot be an empty string")
        self.__name = name
        if not isinstance(age, int) or age < 0:
            raise ValueError("age must be a positive integer")
        self.__age = age
    def set_name(self, name):
        if not isinstance(name, str) or name =="":
            raise ValueError("name cannot be an empty string")
        self.__name = name
    def set_age(self, age):
        if not isinstance(age, int) or age < 0:
            raise ValueError("age must be a positive integer")
        self.__age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def __str__(self):
        return f"People(name={self.__name}, age={self.__age})"

pp1 = People("John", 25)
pp1.set_name("Josh")
pp1.set_age(25)
print(pp1)
print(pp1.get_name())



from urllib.request import urlopen
"""
class WebPage:
    def __init__(self, url):
        self.url = url
        self.content = None

    def content(self):
        return urlopen(self.url).read()

webpage = WebPage("https://example.com")
content = webpage.content()
print(content.decode("utf-8"))
"""
# class method takes cls (the class itself) as the first argument.

class Demo:
    def regular(self):
        print("regular")

    @staticmethod
    def static():
        print("static")

    @classmethod
    def classm(cls): #takes class as a first argument
        print("classm")

demo = Demo()
demo.regular()
demo.static()


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    @classmethod
    def from_tuple(cls, coords: tuple[float, float]):
        x, y = coords
        return cls(x, y)

v1 = Vector(1, 2)
print(v1)




