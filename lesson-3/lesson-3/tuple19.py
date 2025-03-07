t = (3, 8, 4, 8, 5, 8, 6)
element = 8

lst = list(t)
if element in lst:
    lst.remove(element)
new_tuple = tuple(lst)

print("New Tuple after Removing", element, ":", new_tuple)
