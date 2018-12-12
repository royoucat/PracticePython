list = []

for i in range(10):
    add = int(input("Pleas enter a number to add to the list: "))
    list.append(add)

check = int(input("Please choose a number to check against: "))
checkList = []
for num in list:
    if int(num) < check:
        checkList.append(num)

print(checkList)
