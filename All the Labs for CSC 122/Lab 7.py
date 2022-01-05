# Q5) Assume that you are working in the finance department, and you are responsible for the
# salaries of 5 employees. Given that salary = 12.5h + 11, where h is the hours worked by the
# employees and salary is the salary of the employee.
# a. Take the hours worked (h) as inputs from user
# b. For each input, calculate the salary of the employee
# c. Append the salary into a list called salaries
# d. Print the salaries
salaries = []
i = 0
while(i!=5):
    x = int(input("input the hours"))
    salaries.append(12.5 * x + 11)
    i += 1
print(salaries)
