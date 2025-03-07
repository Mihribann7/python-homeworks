t = (2, 5, 7)

repeat_count = 3

repeated_tuple = tuple(e for e in t for _ in range(repeat_count))

print(repeated_tuple)
