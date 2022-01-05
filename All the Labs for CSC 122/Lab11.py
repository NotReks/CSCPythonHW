# Q5) Write a Python program, that takes input from a user, and calculate the square of all
# numbers from 1 to a given number.

userinput = int(input("Enter a number: "))
while userinput > 0:
    numberexp = userinput ** 2
    print(numberexp)
    userinput -= 1


print()
print()
print()
print()


# Q6) Use a loop to display elements from a given list present at odd index positions.

my_list=[10 ,20 ,30 ,40 ,50 ,60 ,70 ,80 ,90 ,100]

for index in range(len(my_list)):
    if index % 2 != 0:
        print(index, my_list[index])





# Failed Attempt with while loops
#counter = 0
#while counter != len(my_list):
    #if my_list[counter] % 2 != 0:
      #  print(my_list[counter])
    #counter += 1