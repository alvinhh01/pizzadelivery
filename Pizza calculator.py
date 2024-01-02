print("Thank you for choosing Python Pizza Deliveries!")
# Based on a user's order, work out their final bill.

#1. User chooses which size of pizza
print("Small Pizza is $15")
print("Medium Pizza is $20")
print("Large Pizza is $25")
size = str(input("What size pizza do you want? S, M, or L "))

#2. User chooses if want pepperoni
print("Add pepperoni for small pizza +$2")
print("Add pepperoni for medium or large pizza +$3")
add_pepperoni = str(input("Do you like pepperoni in your pizza? (Yes or No) "))

#3. User chooses if want cheese
print("Add extra cheese for any size pizza +$1")
add_cheese = str(input("Do you want to add extra cheese to your pizza? (Yes or No) "))
bill = 0

#size.lower is to allow any case
if size.lower() in ["small", "s"]:
    print("A small pizza is $15")
    bill += 15
elif size.lower() in ["medium", "m"]:
    print("A medium pizza is $20")
    bill += 20
elif size.lower() in ["large", "l"]:
    print("A large pizza is $25")
    bill += 25
elif size.lower() not in ["small", "medium", "large", 's', 'm', 'l']:
    print("Invalid input, please select a size of either small, medium, or large")
    exit()

#add pepperoni
if add_pepperoni.lower() in ["yes", "y"]:
    if size.lower() in ["medium", "large"]:
        bill += 3
elif add_pepperoni.lower() in ["yes", "y"]:
    if size.lower() in ["small"]:
        bill += 2
elif add_pepperoni.lower() not in ['y','n','yes','no']:
    print("Invalid input, please indicate if you want pepperoni. Please key in your order again")
    exit()

#add cheese
if add_cheese.lower() in ["yes", "y"]:
    bill += 1
elif add_cheese.lower() not in ['y','n','yes','no']:
    print("Invalid input, please indicate if you want cheese. Please key in your order again")
    exit()

#total bill
print(f"Your total bill is ${bill}")
