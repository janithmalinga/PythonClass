number = int(input("Enter a number: "))
count = 0

while True:

    count += 1

    if (number%2==0):
        number = number/2
    else:
        number = (number * 3) + 1

    print (number)

    if(number==1):
        print("Number of steps are", count)
        break

