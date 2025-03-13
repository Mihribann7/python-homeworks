def add_employee():
    with open("employees.txt", "a") as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        position = input("Enter Employee Position: ")
        salary = input("Enter Employee Salary: ")
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
    print("Employee record added successfully!\n")

def view_employees():
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
            if records:
                print("\nEmployee Records:")
                for record in records:
                    print(record.strip())
            else:
                print("No records found.")
    except FileNotFoundError:
        print("No records found.")


def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    with open("employees.txt", "r") as file:
        records = file.readlines()
        for record in records:
            if record.startswith(emp_id + ","):
                print("Employee Found:", record.strip())
                return
    print("Employee not found.")


def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    updated_records = []
    found = False
    with open("employees.txt", "r") as file:
        records = file.readlines()
        for record in records:
            if record.startswith(emp_id + ","):
                found = True
                name = input("Enter new name (leave blank to keep current): ") or record.split(", ")[1]
                position = input("Enter new position (leave blank to keep current): ") or record.split(", ")[2]
                salary = input("Enter new salary (leave blank to keep current): ") or record.split(", ")[3]
                updated_records.append(f"{emp_id}, {name}, {position}, {salary}\n")
            else:
                updated_records.append(record)

    if found:
        with open("employees.txt", "w") as file:
            file.writelines(updated_records)
        print("Employee record updated successfully!")
    else:
        print("Employee not found.")


def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    updated_records = []
    found = False
    with open("employees.txt", "r") as file:
        records = file.readlines()
        for record in records:
            if record.startswith(emp_id + ","):
                found = True
            else:
                updated_records.append(record)

    if found:
        with open("employees.txt", "w") as file:
            file.writelines(updated_records)
        print("Employee record deleted successfully!")
    else:
        print("Employee not found.")


while True:
    print("\nEmployee Records Manager")
    print("1. Add new employee record")
    print("2. View all employee records")
    print("3. Search for an employee by Employee ID")
    print("4. Update an employee's information")
    print("5. Delete an employee record")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        delete_employee()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")