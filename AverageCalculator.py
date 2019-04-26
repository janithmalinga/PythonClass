number = []
temp_number = 0

print("This programme is written to calculate the average of a given set of numbers. Enter -1 to end the numbers.")

while True :
    temp_number = float(input("Enter number : "))
    if temp_number < 0:
        break

    number.append(temp_number)

print("Average is " + str(sum(number)/len(number)))
