t = (1, 2, 3, 2, 4, 2, 5)

element = 2

indices = [i for i, val in enumerate(t) if val == element]

print(f"Indices of {element}:", indices)
