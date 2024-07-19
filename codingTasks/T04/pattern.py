
my_arr = []

for i in range(1,10):
    if i > 5:
        my_arr.pop()
    else:
        my_arr.append('*')
    my_string = ''.join(my_arr)
    print(my_string)
    

