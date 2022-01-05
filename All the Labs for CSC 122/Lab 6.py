# Q1) Write a Python code that:
# a. Take 2 inputs from the user as integer.
# b. Checks which one of these numbers is higher than the other.
# c. Print the result as: “.. is higher than ..”.

N1 = int(input("Input your number"))
N2 = int(input("Input your second number"))


if N1 > N2:
    print(N1, " is higher than ", N2)
elif N2 > N1:
    print(N2, " Is higher than ", N1)
else:
    print("they're equal")

print()
print()
print()
print()

# Q2) Write a python program:
# a. Create a list called names
# b. Take 1 name as inputs from the user, change the name into upper case letters.
# c. Check if a persons’ name starts with an ‘A’, do not append to the list otherwise
# append it to the list.
# d. If the name starts with “F”, split the letter “F” from it.
# e. Print the list in the end.

Names = []
Name1 = input("input your name")
NCaps = Name1.upper()
if (NCaps.startswith("A")):
    print("No")
elif (NCaps.startswith("F")):
    nsplit = NCaps.split("F")
    Names.append(nsplit)
else:
    Names.append(NCaps)
print("The list is ", Names)

# Q3) Draw the flowchart and write a Python program to print the even and odd numbers from
# the input given by the user.

FirstNumber = int(input("Enter your number"))

if FirstNumber % 2 == 0:
    print("This number is even")
else:
    print("the number is odd")

# Q4) Draw a flowchart that tells a user that checks if the number that the user entered is a 5 or
# a 6. Then implement it in code.

fiveorsix = int(input("input either 5 or 6"))

if fiveorsix == 5:
    print("The number is 5")
elif fiveorsix == 6:
    print("The number is 6")
else:
    print("input a number that's either 5 or 6")

# Q5) Maria wants to know her profit and loss, your program should take her income and cost
# as an input. When income>=loss then we calculate the profit using Profit=income-cost
# and when cost>=income then the loss is calculated using loss=cost-income.

income = int(input("please input your income"))
cost = int(input("please input your cost"))

if income >= cost:
    profit = income - cost
    print(profit)
elif cost >= income:
    loss = cost - income
    print(loss)
else:
    print()
