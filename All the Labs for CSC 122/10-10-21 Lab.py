# Q1: Write a program that reads two numbers and multiplies them together and print out their product.
print("Question 1")

print("input the first number")
a = input()
a = int(a)

print("input the second number")
b = input()
b = int(b)

c = a * b

print("The answer is ")
print(c)

# Q2: Evaluate for A = 4, B = 4, and C = 3. Use your Python Editor to check your solution:
print("Question 2")

a = 4
b = 4
c = 3

# A.
f = a ** 2 / 3 * b
print(f)
# B.
f2 = 3 * b / a ** 2
print(f2)
# C.
f3 = a * c / (a + c)
print(f3)
# D.
f4 = (a + 7 - c) % b
print(f4)
# E.
f5 = (c * (b + 3 * a) + 5 * a) / c
print(f5)

# Q3: If Mariam drives her car for 6 hours and travels a total of 250 km, find the speed travelled. Given that speed
# = distance /time.
print("Question 3")

input1 = 6
input2 = 250

print("the speed is...")
ans = input2 / input1
print(ans)

# Q4 Your friend needs to convert the Fahrenheit temperature of 80 degrees into Celsius. Help
# your friend changing a Fahrenheit temperature to Celsius.
print("Question 4")

fdegrees = 80

c = 5 / 9 * (fdegrees - 32)
print("The temperature is...")
print(c)
print("Degrees Celsius")

# Q5 Write a program that calculates the age difference between a father and his child.
print("Question 5")

fatherage = int(input("input the fathers birth year"))
childage = int(input("input the childs birth year"))

agedifference = childage - fatherage

print("the difference is")
print(agedifference)
print("years")
