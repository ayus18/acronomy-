Phrase = input("Enter a Phrase to convert in Acronym: ")
list_words = Phrase.split()
final_acro = ""

# Adding the first letter and iterating of each string to output
for i in list_words:
    final_acro = final_acro + i[0].upper()  # Changing the output to uppercase (required Acronym).

print("Final Acronym : ", final_acro)

# Generating acronyms for all given strings.
for i in range(len(final_acro)):
    print(final_acro[i], " ==> ",list_words[i])