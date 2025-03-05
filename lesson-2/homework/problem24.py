string = str(input("Enter a string: "))
character = str(input("Enter a character: "))
vowels = "aeiouAEIOU"
for char in vowels:
    string = string.replace(char, character)
print(string)