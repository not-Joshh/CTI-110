#Joshua Murray
#P4LAB2
#3/27/2024
#Use a while loop


var1 = int(input("Enter the smallest enteger: "))
var2 = int(input("Enter the largest enteger: "))

while var1 >= var2:
    print("First number must be smaller. Try again")
    var1 = int(input("Enter the smallest enteger: "))
    var2 = int(input("Enter the largest enteger: "))


#While loop broken, values entered correctly

for num in range(var1, var2+1, 5):
    print(num, end = " ")

