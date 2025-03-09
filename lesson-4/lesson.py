authenticated = True
if authenticated:
    pass
print("HI")

r = list(range(15, 51, 3))
print(r)

languages = ['Python', 'JavaScript', 'Java']
versions = [3, 7, 13]

for i in zip(languages, versions):
    print(i)

for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                print(i, j, k, l)