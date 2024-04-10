#Joshua Murray
#P4HW1
#4/09/2024
# prompt user to enter number of scores they want to enter
num_scores = int(input("How many scores do you want to enter? "))

# initialize an empty list to store scores
scores = []

for i in range(num_scores):
    score = -1

    while score < 0 or score > 100:
        score = int(input("Enter score #{}: ".format(i+1)))
        if score < 0 or score > 100:
            print("INVALID Score entered!!!!\nScore should be between 0 and 100")
            print("Enter score #{} again: ".format(i+1))
    scores.append(score)


lowest_score = min(scores)
print("The lowest score entered is:", lowest_score)


scores.remove(lowest_score)


average_score = sum(scores) / len(scores)
print("The modified score list is:", scores)
print("The average score is:", average_score)


if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# display the letter grade
print("The letter grade for the average score is:", letter_grade)
