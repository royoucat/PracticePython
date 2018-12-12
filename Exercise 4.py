num = int(input("Please enter your number: "))
list = []

for i in range(1, num):
    if num % i == 0:
        list.append(i)
print(list)
