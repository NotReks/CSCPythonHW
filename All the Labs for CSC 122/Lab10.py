# Q4) Write a Python program that prints from 10 to 1 in reverse, using a for loop.
counter = 10
for x in range(counter):
    print(counter)
    counter -= 1

print()
print()
print()
print()

# Q5) Write a Python program to find those numbers which are divisible by 7 and multiple of
# 5, between 1500 and 2700 (both included) using for loop.


for c in range(1500,2701):
    if (c % 5 == 0) and (c % 7 == 0):
        print(c)

print()
print()
print()

# Q6) Write a for loop to loop through a list of numbers and use an if statement, that appends
# each number to a new list if the number is positive. Use the following list


nums = [1,-2,3,4,-9,-100,23,45,-1]
numsnew = []
for index in (nums):
    if index > 0:
        numsnew.append(index)
print(numsnew)
