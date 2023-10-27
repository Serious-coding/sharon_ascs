import csv

# Function to load employee data from a CSV file into a list of dictionaries
def load_employee_data(file_name):
    employee_list = []
    try:
        with open(file_name, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                employee_list.append(row)
    except FileNotFoundError:
        pass  # File doesn't exist yet, start with an empty list
    return employee_list

# Function to save employee data from a list of dictionaries into a CSV file
def save_employee_data(file_name, employee_list):
    with open(file_name, mode='w', newline='') as file:
        fieldnames = employee_list[0].keys() if employee_list else []
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(employee_list)

# Function to add a new employee
def add_employee(employee_list):
    employee = {}
    employee['EmployeeID'] = input("Enter Employee ID: ")
    employee['Name'] = input("Enter Employee Name: ")
    employee['Position'] = input("Enter Employee Position: ")
    employee_list.append(employee)
    print("Employee added successfully!")

# Function to list all employees
def list_employees(employee_list):
    if not employee_list:
        print("No employees found.")
    else:
        for employee in employee_list:
            print(employee)

# Function to search for an employee by ID
def search_employee(employee_list):
    employee_id = input("Enter Employee ID to search: ")
    for employee in employee_list:
        if employee['EmployeeID'] == employee_id:
            print("Employee Found:")
            print(employee)
            return
    print("Employee not found.")

# Main program
employee_data_file = "employee_data.csv"
employees = load_employee_data(employee_data_file)

while True:
    print("\nEmployee Management System Menu:")
    print("1. Add Employee")
    print("2. List Employees")
    print("3. Search Employee")
    print("4. Delete employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_employee(employees)
    elif choice == '2':
        list_employees(employees)
    elif choice == '3':
        search_employee(employees)
    elif choice =='4':
        # Function to delete an employee by Employee ID
        def delete_employee(employee_list):
            employee_id = input("Enter Employee ID to delete: ")
                for employee in employee_list:
                    if employee['EmployeeID'] == employee_id:
                    employee_list.remove(employee)
                    print("Employee deleted successfully!")
                return
    print("Employee not found.")

# Inside the main program loop, add this condition after the "elif" blocks
elif choice == '4':
    delete_employee(employees)


    elif choice == '5':
        save_employee_data(employee_data_file, employees)
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
