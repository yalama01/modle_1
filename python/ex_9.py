
word_list = []
for _ in range(5):
    word = input("Enter a word: ")
    word_list.append(word)

resultant_string = ' '.join(word_list)

print("List of words:", word_list)
print("Resultant string:", resultant_string)
