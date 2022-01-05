# Q4) Write a Python program that takes 10 names from the user and checks whether each
# name starts with a “Z”, if the name does, add it to a list called znames, if it doesn’t, add it to
# a list called others.
# Print both lists in the end.

znames = []
others = []
counter = 0
while counter != 10:
    name = input("enter a name: ")
    if name[0].lower() == "z":
        znames.append(name)
    else:
        others.append(name)
    counter += 1
print("the znames list: ", znames)
print("the other names list: ", others)

print()
print()
print()
print()

# Q5) Write a Python program that prints from 10 to 1
counter2 = 10
while counter2 >= 1:
  print(counter2)
  counter2 -= 1
