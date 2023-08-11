import numbers
import random

def main():
    numbers = []
    append_random_numbers(numbers)
    append_random_numbers(numbers, 20)
    print(numbers)
def append_random_numbers(numbers_list, quantity=1):
    
   for _ in range(quantity):
    random_number = random.uniform(0, 100)
    rounded = round(random_number, 1)
    numbers_list.append(rounded)
    
if __name__ == "__main__":
    main()