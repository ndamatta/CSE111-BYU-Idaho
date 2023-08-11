#https://byui-cse.github.io/cse111-course/lesson01/prove.html
#W01 - Prove
import math
from datetime import datetime

#USER INPUTS
width = float(input("Enter the width of the tire in mm (ex 205): "))
ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

#VOLUME FORMULA
volume = (math.pi * (width ** 2) * ratio * (width * ratio + 2540 * diameter)) / 10000000000

#PRINT
print(f"The approximate volume is {volume:.2f} liters")

#CUSTOMER INPUT AND VARIABLES
customer_answer = ""
customer_name = ""
customer_phone = ""

while customer_answer != "yes" or customer_answer != "no":
    customer_answer = input("Do you want to buy a tire with inserted dimensions? (Yes/No): ")

    if customer_answer.lower() == "yes":
        customer_name = input("Great choice!\nPlease, insert your name: ")
        customer_phone = input("Please, insert your phone number: ")
        print("Thanks!")
        break;

    elif customer_answer.lower() == "no":
        print("Ok!")
        break;


#WORK WITH .TXT FILE
current_date = datetime.now()
with open("volumes.txt", mode="at") as volume_file:

    print(f"{current_date:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume:.2f}",file=volume_file)

    if customer_name != "" or customer_phone != "": #Only print customer if variable has data
        print(f"Customer name: {customer_name}\nCustomer phone number: {customer_phone}", file=volume_file)

    