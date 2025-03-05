sentence = str(input("Enter a sentence: "))
acronym = sentence.split()
for i in acronym:
    print(i[0].upper(), end="")