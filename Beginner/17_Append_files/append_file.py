employees_file = open("employees.txt", "a")

print(employees_file.writable())

employees_file.write("\nMimo Saha - Sr. Android Dev") # will add new line Mimo Saha - Sr. Android Dev

employees_file.close()