print("Welcome to the tip calculator.")
total_bill = float(input("What was the total of your bill? £"))
num_of_people = int(input("How many of you were eating? "))
tip = int(input("How much would you like to tip? 10, 12, or 15 percent? "))
bill_with_tip = total_bill + (total_bill * tip/100)
bill_per_person = bill_with_tip / num_of_people
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay £{final_amount}")