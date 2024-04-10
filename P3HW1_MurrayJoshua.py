#Joshua Murray
#3/14/2024
#P3HW1
#Get grades from user
num_modules = 6
grades = []

for i in range(num_modules):
    grade = float(input(f"Enter grade for Module {i+1}: "))
    grades.append(grade)

lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / num_modules

print("\n-Results--")
print("Lowest Grade:", lowest_grade)
print("Highest Grade:", highest_grade)
print("\nSum of Grades:", sum_of_grades)
for grade in grades:
    print(grade)
print("\nAverage:")
print(f"{average_grade:.2f}")

if average_grade >= 90:
    letter_grade = "A"
elif average_grade >= 80:
    letter_grade = "B"
elif average_grade >= 70:
    letter_grade = "C"
elif average_grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print("\nYour grade is:", letter_grade)
