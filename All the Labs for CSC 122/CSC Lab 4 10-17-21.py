# Question 1

# x = 2
# 9 = y
# print(x;"2"), print (x+y)

# It's supposed to be this
x = [2]
y = [9]

z = x + y

print(x[0])
print(z)

print()
print()
print()

# Question 2

Number1 = int(input("Put your first number here"))
Number2 = int(input("Put your second number here"))

AdditionAnswer = Number1 + Number2
print("Here's the addition answer")
print(AdditionAnswer)

SubtractionAnswer = Number1 - Number2
print("Here's the subtraction answer ")
print(SubtractionAnswer)

AverageAnswer = (Number1 + Number2) / 2
print("Here's the average of both numbers")
print(AverageAnswer)

print()
print()
print()
print()

# Question 3


List = []

print(List)

List.append(input("First input"))
List.append(input("Second input"))
List.append(input("Third input"))
List.append(input("Fourth input"))
List.append(input("Fifth input"))

print(List[0])
print(List[4])
print(List[2])

print()
print()
print()

# Question 4


FirstName = input("Enter your first name")
LastName = input("Enter your last name")

print(LastName, FirstName)

NameList = [FirstName, LastName]

print(NameList)

print()
print()
print()

# Question 5

Q5List = []

A = int(input())
Q5List.append(A)

B = int(input())
Q5List.append(B)

C = int(input())
Q5List.append(C)

D = int(input())
Q5List.append(D)

E = int(input())
Q5List.append(E)

Multi = Q5List[0] * Q5List[4]
print(Multi)

Add = Q5List[0] + Q5List[1]
print(Add)

Sub = Q5List[1] - Q5List[2]
print(Sub)

print(Q5List)