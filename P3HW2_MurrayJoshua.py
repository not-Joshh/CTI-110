#P3HW2 - Salary
#Joshua Murray
#3/25/2024

   
#Ask user to enter employee details
employee_name = input("Enter the name of the employee: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter the employee's pay rate: "))


overtime_hours = max(hours_worked - 40, 0)
overtime_pay_rate = pay_rate * 1.5
overtime_pay = overtime_hours * overtime_pay_rate


regular_hours = hours_worked - overtime_hours
regular_pay = regular_hours * pay_rate


gross_pay = regular_pay + overtime_pay


print("Employee Name:", employee_name)
print("Pay Rate:", pay_rate)
print("Hours Worked:", hours_worked)
print("Overtime Hours:", overtime_hours)
print("Overtime Pay:", overtime_pay)
print("Pay for Regular Hours:", regular_pay)
print("Gross Pay:", gross_pay)

