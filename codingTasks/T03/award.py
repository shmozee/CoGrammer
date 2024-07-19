# Store my times for each event
swimming = int(input("Enter swimming time (minutes): "))
cycling = int(input("Enter cycling time (minutes): "))
running = int(input("Enter running time (minutes): "))

# Work on the logic
total_time = swimming + cycling + running

if 0 <= total_time <= 100:
    award = "Provincial colours"
elif 101 <= total_time <= 105:
    award = "Provincial half colours"
elif 106 <= total_time <= 110:
    award = "Provincial scroll"
else:
    award = "No award"

# print the results
print()
print("Total time (minutes): ", total_time)
print("Award: ", award)