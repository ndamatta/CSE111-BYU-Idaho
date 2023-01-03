import csv
from datetime import datetime

#Indexes
PRODUCT_ID_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2

PRODUCT_QUANTITY_INDEX = 1

def main():
    try:
        current_date_and_time = datetime.now()

        products_dict = read_dict("products.csv", 0)
        print(products_dict)
        
        with open("request.csv", "r") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)

            #Variables for prices and total
            number_of_items = 0
            sub_total = 0
            print("Iknom Emporium")
            for row in reader:
                product_name = products_dict[row[PRODUCT_ID_INDEX]][1]
                product_price = products_dict[row[PRODUCT_ID_INDEX]][2]

                number_of_items += int(row[PRODUCT_QUANTITY_INDEX])
                sub_total += float(product_price) * int(row[PRODUCT_QUANTITY_INDEX])

                print(f"{product_name}: {row[PRODUCT_QUANTITY_INDEX]} @ {product_price}")
                
            sales_tax = sub_total * 0.06
            total = sub_total + sales_tax
            print()
            print(f"Number of items: {number_of_items}")
            print(f"Subtotal: {sub_total:.2f}")
            print(f"Sales tax: {sub_total * 0.06:.2f}")
            print(f"Total: {total:.2f}")
            print()
            print("Thank you for shopping at the Inkom Emporium")
            print(f"{current_date_and_time:%a %b %d %I:%M:%S %Y}")
            print("If you are satisfied with our services, feel free to complete this online survey: www.online-survey.com")
            

    
    except FileNotFoundError as file_not_found:
        print()
        print(type(file_not_found).__name__, file_not_found, sep=": ")
        print("The file doesn't exist.")
        print("Run the program again and enter the name of an existing file.")
    
    except PermissionError as permision_err:
        print()
        print(type(permision_err).__name__, permision_err, sep=": ")
        print("You don't have permission to read the file.")
        print("Run the program again and enter the name of a file that you are allowed to read.")

    except KeyError as key_error:
        print()
        print(type(key_error).__name__, permision_err, sep=": ")
        print("Error: unknown product ID in the request.csv file")


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list

    return dictionary

if __name__ == "__main__":
    main()