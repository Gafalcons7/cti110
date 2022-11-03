# cti 110
# P1HW2_Travel
# Mitchell Howard
# nov 3 2022
#



# input: three expenses, the budget
# processing: total the expenses, compare with budget
# output: did you go over or under

# out variable

gas = 0.0
food = 0.0
hotal = 0.0
totalExpenses = 0.0 # gas + food + hotel
budget = 0.0
destination = ""

print( "This program calculates on the display travel expenses")

print("Enter your budget: ")
budget = float (input())

destination = input("Where are you heading? ")

print("ok, let's total your expenses.")
print("Gas: $")
gas = float(input())

print("Hotel: $")
hotel = float(input())

print("food: $")
food = float(input())

#add everything up
totalExpenses = gas + hotel + food
# output - did they go over budget?

print ("Your total expenses are: $", totalExpenses)
print("Your  budget was: $", budget)

if totalExpenses > budget:
    print("you went over budget!")
else:
    print("You stayed within your budget.")

