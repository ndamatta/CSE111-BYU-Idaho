# This program calculates the approximate volume of a tire based on user-provided dimensions (width, aspect ratio, and diameter).
# It also interacts with the user to gather information and stores the tire dimensions and customer data in a .txt file.

# Import necessary modules.
import math
from datetime import datetime

# Gather user inputs for tire dimensions.
width = float(input("Enter the width of the tire in mm (ex 205): "))
ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate the approximate volume of the tire using the provided formula.
volume = (math.pi * (width ** 2) * ratio * (width * ratio + 2540 * diameter)) / 10000000000

# Print the calculated volume.
print(f"The approximate volume is {volume:.2f} liters")

# Gather customer information and store it if desired.
customer_answer = ""
customer_name = ""
customer_phone = ""

while customer_answer.lower() != "yes" and customer_answer.lower() != "no":
    customer_answer = input("Do you want to buy a tire with inserted dimensions? (Yes/No): ")

    if customer_answer.lower() == "yes":
        customer_name = input("Great choice!\nPlease, insert your name: ")
        customer_phone = input("Please, insert your phone number: ")
        print("Thanks!")
        break
    elif customer_answer.lower() == "no":
        print("Ok!")
        break

# Work with a .txt file to store tire dimensions and customer data.
current_date = datetime.now()
with open("volumes.txt", mode="at") as volume_file:
    print(f"{current_date:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume:.2f}", file=volume_file)
    if customer_name != "" or customer_phone != "":
        print(f"Customer name: {customer_name}\nCustomer phone number: {customer_phone}", file=volume_file)
