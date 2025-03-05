string = str(input("Enter a string: "))
string2 = string.lower()
numvowels = 0
numcons = 0
for char in string2:
    if(char == "e" or char == "u" or char=="o" or char=="a" ):
        numvowels = numvowels + 1
    else:
        numcons = numcons + 1
print("Number of vowels: ", numvowels)
print("Number of consonants: ", numcons)
