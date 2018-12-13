string = input("Please enter a word to check if it is a palindrome!: ")
stringBack = ""

for c in reversed(string):
    stringBack = stringBack + c


if stringBack == string:
    print("This word is a palindrome!")
else:
    print("This word is not a palindrome!")