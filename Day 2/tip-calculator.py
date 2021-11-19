print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? "))
percentage = int(input ("How much tip would you like to give? 10, 12, or 15? "))/100
people = int(input("How many people to split the bill? "))
bill = (total_bill/people) + ((total_bill/people) *percentage)
round_bill = round(bill, 2)
final_bill = str(round_bill)
print("Each person should pay: " + final_bill)