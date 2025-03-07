d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"c": 10, "d": 20, "e": 30}

common_keys = set(d1.keys()) & set(d2.keys())

print(common_keys)
