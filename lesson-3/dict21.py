d = {"b": 2, "a": 1, "c": 3}

sorted_dict = dict(sorted(d.items(), key=lambda x: x[1]))

print( sorted_dict)
