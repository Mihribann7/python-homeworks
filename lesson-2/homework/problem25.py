string = input("Enter a string: ")
startWord = input("Starts with: ")
endWord = input("Ends with: ")
if string.startswith(startWord) and string.endswith(endWord):
    print("Yes, the string starts and ends with the given words.")
else:
    print("No, the string does not match the given start or end.")
