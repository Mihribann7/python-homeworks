t = (5, 12, 7, 3, 9, 14, 2)
start_index = 1
end_index = 5

subtuple = t[start_index:end_index]
max_element = max(subtuple) if subtuple else None

print("Maximum of Subtuple:", max_element)
