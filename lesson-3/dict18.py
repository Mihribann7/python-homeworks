from collections import defaultdict

d = defaultdict(lambda: "Not Found")

d["name"] = "Alice"
d["age"] = 25

existing = d["name"]
missing = d["city"]

print(missing)
