#Joshua Murray
#2/21/2024
#P1HW2

#Getting integers from user

budget = int(input("Enter your budget: "))

destination = input("Enter your destination: ")

gas = float(input("How much do you think will be spent on gas?"))

hotel = float(input("How much will you need for a hotel?"))

food = float(input("Last, how much will you need for food?"))

expenses = gas+hotel+food
balance = budget-expenses

print ("------Travel Expenses------")

print ("Location: ", destination)
print ("Initial Budget:", "$",budget)
print ("Fuel:", "$",gas)
print ("Accomodation:", "$",hotel)
print ("Food:", "$",food)
print ("---------------------------")
print ("Remaining Balance:", "$",balance)    
