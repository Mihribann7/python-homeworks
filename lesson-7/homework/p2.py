class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:
    file = "employees.txt"

    def __init__(self):
        self.employees = self.load_employees()

    def load_employees(self):
        try:
            with open(self.file, "r") as file:
                return [self.parse_employee(line.strip()) for line in file]
        except FileNotFoundError:
            return []

    def save_employees(self):
        with open(self.file, "w") as file:
            for employee in self.employees:
                file.write(str(employee) + "\n")

    @staticmethod
    def parse_employee(line):
        employee_id, name, position, salary = line.split(",")
        return Employee(employee_id, name, position, float(salary))

    def add_employee(self):
        employee_id = input("Enter employee ID: ")
        name = input("Enter name: ")
        position = input("Enter position: ")
        salary = float(input("Enter salary: "))

        new_employee = Employee(employee_id, name, position, salary)
        self.employees.append(new_employee)
        self.save_employees()
        print("Employee added")

    def view_all_employees(self):
        if not self.employees:
            print("No employees added")
        else:
            for employee in self.employees:
                print(employee)

    def search_employee(self):
        search_id = input("Enter employee ID: ")
        for employee in self.employees:
            if employee.employee_id == search_id:
                print("Found: ", employee)
                return
        print("No employee found")

    def update_employee(self):
        update_id = input("Enter employee ID: ")
        for employee in self.employees:
            if employee.employee_id == update_id:
                employee.name = input("Update name: ")
                employee.position = input("Update position: ")
                employee.salary = input("Update salary: ")
                self.save_employees()
                print("Employee updated")
                return
        print("No employee found")

    def delete_employee(self):
        delete_id = input("Enter Employee ID to delete: ")
        for employee in self.employees:
            if employee.employee_id == delete_id:
                self.employees.remove(employee)
                self.save_employees()
                print("Employee deleted successfully!")
                return
        print("Employee not found.")

    def run(self):
        while True:
            print("""
    Welcome to the Employee Records Manager!
    1. Add new employee record
    2. View all employee records
    3. Search for an employee by Employee ID
    4. Update an employee's information
    5. Delete an employee record
    6. Exit
    """)
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_all_employees()
            elif choice == "3":
                self.search_employee()
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = EmployeeManager()
    manager.run()

