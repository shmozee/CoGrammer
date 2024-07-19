import statistics
my_arr = []

while True: 
    num = int(input("Enter a number: "))
    if num == -1:
        print(statistics.mean(my_arr))
        break
    else:
        my_arr.append(num)
        print("Current array: ", my_arr)
