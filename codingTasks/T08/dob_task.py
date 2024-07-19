
# Task 8 - Practical Task 1

with open('DOB.txt', 'r') as file:
    name_dob = {}
    lines = file.readlines()
    for line in lines:
        split_line = line.split(" ")
        name = split_line[0] + " " + split_line[1]
        dob = split_line[2] + " " + split_line[3] + " " + split_line[4]
        name_dob[name] = dob
    
print("Name")
for k in name_dob:
    print(k)    
        
print("\nBirthdate")
for k, v in name_dob.items():
    print(v, end="")        
    
    