import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    #Call the read_compund_list to read the file pupils.csv and store the list in the variable
    students_list = read_compound_list("pupils.csv")

    #Create a lambda function to use as an argument in the sorted function, and store results in variables
    birthday_func = lambda birthday: birthday[BIRTHDATE_INDEX]
    given_name_func = lambda given_name: given_name[GIVEN_NAME_INDEX]

    students_old_to_young = sorted(students_list, key=birthday_func)
    students_young_to_old = sorted(students_list, key=birthday_func, reverse=True)
    students_given_name = sorted(students_list, key=given_name_func)

    #Print list os students sorted on birthday oldest to youngest
    print_list(students_old_to_young)
    print()
    print_list(students_young_to_old)
    print()
    print_list(students_given_name)

def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(list):
    """"
    Read a list and return each element of the list on a separate line
    Parameter: a list
    Return: each element of the list
    """
    for element in list:
        print(element)

if __name__ == "__main__":
    main()