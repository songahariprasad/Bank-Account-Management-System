class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
        self.work_hours = 0  # New attribute for work hours

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Department: {self.department}, Salary: ${self.salary:.2f}, Work Hours: {self.work_hours}"


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee.name} added to {self.name} department.")

    def remove_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                print(f"Employee {employee.name} removed from {self.name} department.")
                return
        print("Employee not found.")

    def list_employees(self):
        print(f"Employees in {self.name} department:")
        if not self.employees:
            print("No employees in this department.")
        else:
            for employee in self.employees:
                print(employee)


class EmployeeManagementSystem:
    def __init__(self):
        self.departments = {}
        self.employees = {}

    def add_department(self, department_name):
        if department_name not in self.departments:
            self.departments[department_name] = Department(department_name)
            print(f"Department {department_name} created.")
        else:
            print(f"Department {department_name} already exists.")

    def view_departments(self):
        if not self.departments:
            print("No departments available.")
        else:
            print("Available departments:")
            for dept in self.departments.keys():
                print(f"- {dept}")

    def add_employee(self, emp_id, name, department_name, salary):
        if emp_id in self.employees:
            print("Employee ID already exists.")
            return

        if department_name not in self.departments:
            print(f"Department {department_name} does not exist. Please create it first.")
            return

        employee = Employee(emp_id, name, department_name, salary)
        self.employees[emp_id] = employee
        self.departments[department_name].add_employee(employee)

    def view_employee(self, emp_id):
        employee = self.employees.get(emp_id)
        if employee:
            print(employee)
        else:
            print("Employee not found.")

    def update_employee(self, emp_id, name=None, department_name=None, salary=None):
        employee = self.employees.get(emp_id)
        if employee:
            if name:
                employee.name = name
            if department_name and department_name in self.departments:
                # Remove from old department
                self.departments[employee.department].remove_employee(emp_id)
                employee.department = department_name
                self.departments[department_name].add_employee(employee)
            if salary is not None:
                employee.salary = salary
            print(f"Employee {emp_id} updated.")
        else:
            print("Employee not found.")

    def delete_employee(self, emp_id):
        employee = self.employees.pop(emp_id, None)
        if employee:
            self.departments[employee.department].remove_employee(emp_id)
            print(f"Employee {employee.name} deleted.")
        else:
            print("Employee not found.")

    def list_employees_in_department(self, department_name):
        if department_name in self.departments:
            self.departments[department_name].list_employees()
        else:
            print("Department not found.")

    def list_all_employees(self):
        if not self.employees:
            print("No employees available.")
        else:
            print("All Employees:")
            for employee in self.employees.values():
                print(employee)

    def add_bonus(self, emp_id, bonus_amount):
        employee = self.employees.get(emp_id)
        if employee:
            employee.salary += bonus_amount
            print(f"Bonus of ${bonus_amount:.2f} added to {employee.name}. New Salary: ${employee.salary:.2f}")
        else:
            print("Employee not found.")


def display_menu():
    print("\nEmployee Management System")
    print("1. Add Department")
    print("2. View Departments")
    print("3. Add Employee")
    print("4. View Employee")
    print("5. Update Employee")
    print("6. Delete Employee")
    print("7. List Employees in Department")
    print("8. List All Employees")  # New option
    print("9. Add Bonus to Employee")  # New option
    print("10. Exit")


def main():
    ems = EmployeeManagementSystem()

    while True:
        display_menu()
        choice = input("Select an option (1-10): ")

        if choice == '1':
            dept_name = input("Enter department name: ")
            ems.add_department(dept_name)
        elif choice == '2':
            ems.view_departments()
        elif choice == '3':
            emp_id = input("Enter employee ID: ")
            name = input("Enter employee name: ")
            dept_name = input("Enter department name: ")
            salary = float(input("Enter employee salary: "))
            ems.add_employee(emp_id, name, dept_name, salary)
        elif choice == '4':
            emp_id = input("Enter employee ID to view: ")
            ems.view_employee(emp_id)
        elif choice == '5':
            emp_id = input("Enter employee ID to update: ")
            name = input("Enter new name (leave blank to keep current): ")
            dept_name = input("Enter new department name (leave blank to keep current): ")
            salary_input = input("Enter new salary (leave blank to keep current): ")
            salary = float(salary_input) if salary_input else None
            ems.update_employee(emp_id, name if name else None, dept_name if dept_name else None, salary)
        elif choice == '6':
            emp_id = input("Enter employee ID to delete: ")
            ems.delete_employee(emp_id)
        elif choice == '7':
            dept_name = input("Enter department name to list employees: ")
            ems.list_employees_in_department(dept_name)
        elif choice == '8':
            ems.list_all_employees()  # List all employees
        elif choice == '9':
            emp_id = input("Enter employee ID to add bonus: ")
            bonus_amount = float(input("Enter bonus amount: "))
            ems.add_bonus(emp_id, bonus_amount)  # Add bonus to employee
        elif choice == '10':
            print("Exiting the Employee Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
