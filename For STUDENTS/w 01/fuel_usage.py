# https://byui-cse.github.io/cse111-course/lesson03/check.html

# Import the necessary module for tracking memory allocation.
from tracemalloc import start

# Define the main function that drives the program's execution.
def main():
    print("---FUEL USAGE---")
    # Prompt the user for the first and second odometer readings in U.S. miles.
    first_odometer = float(input("Enter the first odometer reading (miles): "))
    second_odometer = float(input("Enter the second odometer reading (miles): "))
    
    # Prompt the user for the amount of fuel used in U.S. gallons.
    fuel_used = float(input("Enter the amount of fuel used (gallons): "))
    
    # Calculate miles per gallon (mpg) using the provided function and user inputs.
    mpg = miles_per_gallon(first_odometer, second_odometer, fuel_used)
    
    # Convert mpg to liters per 100 kilometers (lp100k) using the provided function.
    lp100k = lp100k_from_mpg(mpg)
    
    # Display the calculated fuel efficiency values.
    print("---RESULTS---")
    print("In your trip you used...")
    print(f"{mpg:.2f} miles per gallon")
    print(f"{lp100k:.2f} liters per 100 km")

# Calculate miles per gallon (mpg) based on odometer readings and fuel consumption.
def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters:
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """ 
    mpg = (end_miles - start_miles) / amount_gallons
    return mpg

# Convert miles per gallon (mpg) to liters per 100 kilometers (lp100k).
def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter:
        mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    lp100k = 235.215 / mpg
    return lp100k

# Call the main function to start the program's execution.
main()
