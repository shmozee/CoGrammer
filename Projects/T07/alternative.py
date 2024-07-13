
# Practical Task 1


def alternative(mystring):
    for i in range(0, len(mystring)):
        if i % 2 == 0: 
            number_builder.append(mystring[i].upper())
        else : 
            number_builder.append(mystring[i])
    print("".join(number_builder))
    
def alternative_two(mystring):
    arr = mystring.split(" ")
    for i in range(0, len(arr)):
        if i % 2 != 0: 
            arr[i] = arr[i].upper()
        else : 
            arr[i] = arr[i].lower()
    print(" ".join(arr))



random_string = input("Give me a string: ")
number_builder = []

alternative(random_string)
alternative_two(random_string)
