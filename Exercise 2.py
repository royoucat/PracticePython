number = int(input("Please enter a number : "))
check = int(input("Please enter a number to check against: "))

if number%4 == 0:
    print("This number is divisible by 4!")
elif number%2 == 0:
    print("This number is even!")
else:
    print("This number is odd!")

if number % check == 0:
    print(str(number) + " is divisible by " + str(check))
else:
    print(str(number) + " is not divisible by " + str(check))