my_list = [1, 5, 3, 9, 2, 8]
shift = 2
rotated_list = my_list[-shift:] + my_list[:-shift]
print(rotated_list)
