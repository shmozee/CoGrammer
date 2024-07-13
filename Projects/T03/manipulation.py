str_manip = input("Enter a sentence: ")

print("Lenth of the sentence: ", len(str_manip))
last_letter = str_manip[-1]
new_str = str_manip.replace(last_letter, '@')

print("Replacing every occurence of the last letter with '@': ", new_str)
print("Getting the last 3 letters: ", str_manip[-3:])

five_letter_word = str_manip[0:3] + str_manip[-2:]
print("Making the 5 letter word: ", five_letter_word)

print()
