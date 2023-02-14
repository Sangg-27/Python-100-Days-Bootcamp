#Day 1 TIP CALCULATOR

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60


print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage would you like to give? 10 , 12, or 15? "))
people = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amt = bill * tip_as_percent
total_bill = bill + total_tip_amt
bill_per_person = total_bill / people
final_amt = round(bill_per_person, 2)
print(f"Each persson should pay: ${final_amt}")

#OUTPUT
Welcome to the tip calculator!
What was the total bill? $150
What percentage would you like to give? 10 , 12, or 15? 10
How many people to split the bill? 5
Each persson should pay: $33.0
