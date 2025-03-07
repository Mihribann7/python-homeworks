d = {"name": "Alice", "age": 25, "city": "New York"}

key = "age"

if key in d:
    del d[key]
else:
    print("key not found")

print(d)
