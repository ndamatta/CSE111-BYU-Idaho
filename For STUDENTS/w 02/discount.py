# This program calculates the subtotal, applies discounts and sales tax, and displays the total amount for a shopping cart.
# It also considers a discount based on the subtotal amount and the day of the week.

from datetime import datetime

# Initialize variables for subtotal and price.
subtotal = 0
price = 1

# Input loop to gather price and quantity for each item.
print("---MINI SHOPPING CART---")
while price != 0:
    price = float(input("What's the price?: "))
    
    if price != 0:
        quantity = float(input("How many items?: "))
        subtotal = subtotal + (price * quantity)

# Display the calculated subtotal.
print(f"Subtotal is: {subtotal}")

# Get the current date and day of the week.
current_date = datetime.now()
day_of_week = current_date.weekday()

# Apply discounts and calculate total based on day of the week and subtotal.
if day_of_week == 1 or day_of_week == 2:
    if subtotal >= 50:
        discount = subtotal * 0.10
        subtotal -= discount
        sales_tax = subtotal * 0.06
        total = subtotal + sales_tax

        print(f"Discount amount: ${discount:.2f}")
        print(f"Sales tax amount: ${sales_tax:.2f}")
        print(f"Total: ${total:.2f}")
    else:
        sales_tax = subtotal * 0.06
        total = subtotal + sales_tax
        rest = 50 - subtotal

        print(f"You have to buy ${rest:.2f} more to apply for discount!")
        print(f"Sales tax amount: ${sales_tax:.2f}")
        print(f"Total: ${total:.2f}")

