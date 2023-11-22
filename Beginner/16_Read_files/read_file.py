employees_file = open("employees.txt", "r")

# print(employees_file.readable()) # True
# print(employees_file.readline()) # will show first line
# print(employees_file.readline()) # will show second line
# print(employees_file.readlines()) # will show all lines as a list

for employee in employees_file.readlines():
    print(employee)

employees_file.close()