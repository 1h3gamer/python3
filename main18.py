string = input("Please enter your string: ")

string1 = ('')

for i in string:
    string1 = i + string1

print("The original string: ", string)
print("The reversed string: ", string1)