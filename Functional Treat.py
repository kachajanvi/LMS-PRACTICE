#functional treat
Employee = []

def add_employee():
    global employee

    print("\n===Add Employee Salary===")
    row = input("Enter salaries separated by spaces:")

    employee=[]
    for salary in row.split():
        employee.append(int(salary))

    print("Employee data saved successfully!")

def salary_summary():
    if len(employees) == 0:
        print("no employee data found!")
        return

    print("\n===salary summary===")
    print("total employees :", len(employees))
    print("highest salary :", max(employees))
    print("lowest salary :", min(employees))
    print("total summary :", sum(employees))
    print("average salary:", round(sum(employees)/len(employees),2))

def bonus_filter():
    if len(employee) == 0:
        print("np employee data found!")
        return

    amount=int(input("enter minimum  salary:"))
    result=(filter(lambda x:x >=amount,employee))

    print("filter salaris :",result)

def sort_salary():
    if len(employee) == 0:
        print("no employee data found!")
        return

    employee.sort()
    print("sorted salaries:",employee)

def factorial(n):
    if n <=1:
        return 1
    return n*factorial(n-1)

def calculate_factorial():
    num=int(input("enter a number:"))
    print("factorial:",factorial(num))

while True:
    print("\n===Employee Management System===")
    print("1. Add employee salaries")
    print("2. Salary summary")
    print("3. filter salaries")
    print("4. sort salaries")
    print("5. calculate factorial")
    print("6. Exit")

    choice=input("Enter your choice:")

    if choice == "1":
        add_employee()
    elif choice == "2":
        add_employee()
    elif choice == "3":
        bonus_filter()
    elif choice == "4":
        sort_salary()
    elif choice == "5":
        calculate_factorial()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
