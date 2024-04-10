#Joshua Murray
#P4HW2
#4/09/2024
num_employees = 0
regular_pay_total = 0
overtime_pay_total = 0
gross_pay_total = 0

while True:
  
  employee_name = input("Enter employee name: ")
  if employee_name.lower() == "done":
    break
 
  pay_rate = float(input("Enter pay rate: "))
  hours_worked = float(input("Enter hours worked: "))
 
  
  if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_pay = (hours_worked - 40) * 1.5 * pay_rate
  else:
    regular_pay = hours_worked * pay_rate
    overtime_pay = 0
   
  
  print(f"{employee_name} earned {regular_pay:.2f} in regular pay and {overtime_pay:.2f} in overtime pay.")
 
  
  num_employees += 1
  regular_pay_total += regular_pay
  overtime_pay_total += overtime_pay
  gross_pay_total += regular_pay + overtime_pay
# display totals
print(f"\nNumber of employees entered: {num_employees}")
print(f"Regular pay total: {regular_pay_total:.2f}")
print(f"Overtime pay total: {overtime_pay_total:.2f}")
print(f"Gross pay total: {gross_pay_total:.2f}")
