#This is a simple tip calculator ;)


print("Welcome to the tip calculator")
bill = input("What is the total bill amount?\n")
percentage = input("What percentage tip would you like to give? \n")
percentage = float(percentage) / 100
people = input("How many people will contribute to the tip?\n")

tip = (float(bill) * float(percentage)) / int(people)

print(f"The tip amount is ${"%.2f" % tip} per person.\n\n")


