#print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? £"))
tip = int(input("What percentage would you like to tip? 10, 12, 15? "))
people = int(input("How many people will split the bill? "))
tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = bill + total_tip
bill_pp = total_bill / people
final_amount = round(bill_pp, 2)

print(f"Each person should pay £ {final_amount} and the total bill is £{total_bill}" )