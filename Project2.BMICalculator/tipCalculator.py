print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12 or 15?"))
split_bill = int(input("How many people to split the bill?"))
bill_with_tip = tip_percent / 100 * total_bill + total_bill
print("Each person should pay: $", bill_with_tip)