employee_file = open("employee.txt", "r")
print(employee_file.readlines())
print(employee_file.read())

employee_file.close()
