# Q5) Write a program that prints the square of numbers upto a certain value inputted by the
# user.
def question5():
    counter = 0
    n = int(input("Enter a number: "))
    for i in range(1,n + 1):
        counter += 1
        x = counter ** 2
        print(x)

question5()


# Q6) Define a function that accepts 2 values and return its sum, subtraction and
# multiplication
def question6(a, b):
    return a - b, (a + b) / 2, a * b
sub, sum, mult = question6(int(input("enter the first number: ")),int(input("Enter the second number: ")))
print(sub)
print(sum)
print(mult)