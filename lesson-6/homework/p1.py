def check(func):
    def wrapper(a, b):
        if b==0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper

@check
def div(a, b):
    return a / b

print(div(1, 2))
print(div(1, 0))