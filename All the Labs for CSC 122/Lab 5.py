# Q1: Given a Python list, and replace the number 20 with 200, and number 10 with 100.

list1 = [5, 10, 15, 20, 25, 50, 20]
print("this is the original list, ", list1)
list1[3] = 200
list1[6] = 200
list1[1] = 100
print("this is the edited list, ", list1)

print()
print()
print()
print()

# Q2: Assume that you are a teacher for 5 students in a CSC122 Course. Take the students
# grades as inputs from the user and:
GradeList = []

Grade1 = float(input("the first students grade"))
Grade2 = float(input("the second students grade"))
Grade3 = float(input("the third students grade"))
Grade4 = float(input("the fourth students grade"))
Grade5 = float(input("the fifth students grade"))

GradeList.append(Grade1)
GradeList.append(Grade2)
GradeList.append(Grade3)
GradeList.append(Grade4)
GradeList.append(Grade5)

print("the average is, ", sum(GradeList) / len(GradeList))
print("The highest number is, ", max(GradeList))
print("The lowest number is, ", min(GradeList))
print("Here's the sorted list, ", sorted(GradeList))

print()
print()
print()
print()

# Q3: Given a list of name that consists of firstname and lastname of a person, swap the
# position of the firstname and lastname in the list to make the firstname as the first element in
# the list.

Name = ["Al Adsani", "Fahad"]
print(Name)
Name.insert(0, Name[1])
Name.pop(2)
print(Name)

print()
print()
print()
print()

# Q4: Assume that you are working in the finance department, and you are responsible for the
# salaries of 5 employees. Given that salary = 12.5h + 11, where h is the hours worked by the
# employees and salary is the salary of the employee.

SalaryList = []

Hours1 = float(input("The 1st Hour count"))
salary1 = 12.5 * Hours1 + 11
Hours2 = float(input("The 2nd Hour count"))
salary2 = 12.5 * Hours2 + 11
Hours3 = float(input("The 3rd Hour count"))
salary3 = 12.5 * Hours3 + 11
Hours4 = float(input("The 4th Hour count"))
salary4 = 12.5 * Hours4 + 11
Hours5 = float(input("The 5th Hour count"))
salary5 = 12.5 * Hours5 + 11

SalaryList.append(salary1)
SalaryList.append(salary2)
SalaryList.append(salary3)
SalaryList.append(salary4)
SalaryList.append(salary5)

print(SalaryList)

print()
print()
print()
print()

# Q5: Take the students attendances as inputs from user; assuming that your class consists of 5
# students.

Student1 = bool(input("1st Student attendance"))
Student2 = bool(input("2nd Student attendance"))
Student3 = bool(input("3rd Student attendance"))
Student4 = bool(input("4th Student attendance"))
Student5 = bool(input("5th Student attendance"))

StudentList = [Student1, Student2, Student3, Student4, Student5]

print(StudentList)

StudentList.pop(3)

print(StudentList)
