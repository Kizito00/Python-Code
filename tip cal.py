# Tip Calculator

print ("welcome to the top calculator")
bill = float(input("What was the total bill? £"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = bill + total_tip
bill_pp = total_bill / people
final_amount = round(bill_pp, 2)

print(f"Each person should pay: £{final_amount}")