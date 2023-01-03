import csv


def main():
    i_number = input("Please, enter an I-Number: ")

    dictionary = read_dict("students.csv", 0)
    # student_name = check_student(i_number, dictionary)

    if i_number not in dictionary:
        print("No such student")
    else:
        # Retrieve the student name that corresponds
        # to the I-Number that the user entered.
        value = dictionary[i_number]
        name = value[1]

        # Print the student name.
        print(name)

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