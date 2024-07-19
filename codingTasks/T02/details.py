"""
Using the Input command 4 times, i will store the following information in seperate variables
Name
Age
Nouse number
Street name

Using f'string, i will concat all the values to form a sentence and store this in 'sentence'
Using print(), i will print the f string
"""

name = input("Enter name: ")
age = input("Enter age: ")
house_number = input("Enter house number: ")
street_name = input("Enter street name: ")

my_sentence = f"This is {name}. He is {age} years old and lives at house number {house_number} on {street_name}."

print(my_sentence)