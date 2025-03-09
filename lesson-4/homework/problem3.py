txt = input("Enter a string: ")
vowels = "aeiou"
result = []
count = 0
i = 0

while i < len(txt):
    result.append(txt[i])
    count += 1
    if count % 3 == 0 and i + 1 < len(txt):
        if txt[i] in vowels:
            result.append(txt[i + 1])
            i += 1
        if i + 1 < len(txt):
            result.append('_')

    i += 1

print("".join(result))
