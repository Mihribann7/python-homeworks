sentences = str(input("Enter sentences: "))
sentences = sentences.split()
seperate = str(input("Enter seperator: "))
final = seperate.join(sentences)
print(final)