#Employees Details
# This code is an Employee Management System that allows users to add, search, and view employee details.
employees = {
    101 : {"name" : "Satya", "age" : 27, "Department" : "HR", "Salary" : 50000},
    102 : {"name" : "Sundar", "age" : 30, "Department" : "Finance", "Salary" : 60000},
    103 : {"name" : "Tim", "age" : 35, "Department" : "IT", "Salary" : 70000},
    104 : {"name" : "Elon", "age" : 40, "Department" : "Engineering", "Salary" : 80000},
    105 : {"name" : "Jeff", "age" : 45, "Department" : "Marketing", "Salary" : 90000},
    106 : {"name" : "Mark", "age" : 50, "Department" : "Sales", "Salary" : 100000},
    107 : {"name" : "Larry", "age" : 55, "Department" : "Support", "Salary" : 110000},
    108 : {"name" : "Sergey", "age" : 60, "Department" : "Operations", "Salary" : 120000},
    109 : {"name" : "Bill", "age" : 65, "Department" : "Legal", "Salary" : 130000}, 
    110 : {"name" : "Warren", "age" : 70, "Department" : "Research", "Salary" : 140000}
}

# Employee Management System
def main_menu():
    while True:
        print("\n Employee Management System ")
        print("1. Add Employees")
        print("2. Search for Employee")
        print("3. View all Employees")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            add_employee()
        elif choice == 2:
            search_employee()
        elif choice == 3: 
            print("\nEmployee List ")
            for emp_id, details in employees.items():
                print(f"ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, Department: {details['Department']}, Salary: {details['Salary']}")
        elif choice == 4:
            print("\nThank you for using the Employee Management System!")
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

#Add an employee to the system
def add_employee():
    print("\n Add Employee ")
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    department = input("Enter Employee Department: ")
    salary = float(input("Enter Employee Salary: "))
    if salary<=0:
        print("Salary must be a positive number.")
        return
    
    employees[emp_id] = {
        "name": name,
        "age": age,
        "Department": department,
        "Salary": salary
    }
    print(f"Employee {name} added successfully.")  
    return

#Search for an employee by ID
def search_employee():
    emp_id = int(input("Enter Employee ID to search: "))
    if emp_id in employees:
        emp_details = employees[emp_id]
        print(f"Employee ID: {emp_id}, Name: {emp_details['name']}, Age: {emp_details['age']}, Department: {emp_details['Department']}, Salary: {emp_details['Salary']}")
    else:
        print("Employee not found.")

#View all employees by ID
def view_all_employees(emp_id):
    if emp_id in employees:
        emp_details = employees[emp_id]
        return f"Employee ID: {emp_id}, Name: {emp_details['name']}, Age: {emp_details['age']}, Department: {emp_details['Department']}, Salary: {emp_details['Salary']}"
    else:
        return "Employee not found."

#Call the main menu function to start the program
if __name__ == "__main__":
    main_menu()