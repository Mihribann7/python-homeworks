for i in range(1, 100):
    if i > 1 and all(i % j != 0 for j in range(2, int(i**0.5) + 1)):
        print(i)
