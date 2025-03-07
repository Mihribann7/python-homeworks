t = (5, 12, 7, 3, 9, 14, 2)
start_index = 1
end_index = 5

subtuple = t[start_index:end_index]
max_element = min(subtuple) if subtuple else None

print("Minimum of Subtuple:", max_element)