import pandas as pd

def main():
    try:
        print("----------TABLE FROM CSV----------")
        filename = str(input("Please, enter the name of your .csv file to start (car_financing.csv): "))
        df = creates_dataframe(filename)

        #If dataframe was created ok
        if df is not None:
            display_menu = "\n1 - Print whole dataframe\n2 - Validate your dataframe  (Show N first and N last rows)\n3 - Select a column (Search for column)\n4 - Rename a column\n5 - Delete column\n0 - Close"
            user_input = ""

            while user_input != 0:
                print(display_menu)
                user_input = int(input("\nPlease, select a number for an operation: "))

                match user_input:
                    case 1:
                        #PRINT WHOLE DATAFRAME
                        print(df)

                    case 2:
                        #VALIDATE DATAFRAME
                        user_rows = int(input("How many rows from the first?: "))
                        first_rows = select_5_first_rows(df, user_rows)

                        user_rows = int(input("How many rows from the last?: "))
                        last_rows = select_last_5_rows(df, user_rows)

                        print(f"------FIRST ROWS------")
                        print(first_rows)
                        print()
                        print(f"------LAST ROWS------")
                        print(last_rows)

                    case 3:
                        #SELECT COLUMN
                        user_column = input("What is the name of the column?: ")
                        first_index = int(input("What is the first index? (0 if none): "))
                        last_index = int(input("What is the last index? (0 if none): "))

                        column = select_column(df, user_column, first_index, last_index)
                        print(f"------COLUMN------")
                        print(column)
                
                    case 4:
                        #RENAME COLUMN
                        original_column = input("What is the name of the column you want to rename?: ")
                        new_column = input("What name do you want to rename this column to?: ")
                        df = rename_column(df, original_column, new_column)

                    case 5:
                        #DELETE COLUMN
                        user_column = input("What is the name of the column you want to delete?: ")
                        delete_column(df, user_column)

                    case 0:
                        print("Thanks for using this program! :)")
                    

    except IndexError as error:
        print(f"Index error: {error}")
        print("Please, run the program again and enter a valid index")

    except ValueError as error:
        print(f"Value Error: {error}")
        print("Please, run the program again and enter a valid value")

    except TypeError as error:
        print(f"Type Error: {error}")
        print("Please, run the program again and enter a valid type")

    except KeyError as error:
        print(f"Key Error: {error}")
        print("Please, run the program again and enter a valid key")

def creates_dataframe(filename):
    """
    Creates a dataframe from a given csv file. If function can't find given file, it will print an error.
        Parameters: 
            filename: filename of csv file with .csv extension, could be a path too
        Return:
            returns dataframe
    """
    try:
        return pd.read_csv(filename)

    except FileNotFoundError as file_not_found:
        print()
        print(type(file_not_found).__name__, file_not_found, sep=": ")
        print("The file doesn't exist.")
        print("Run the program again and enter the name of an existing file.")

def select_5_first_rows(df, rows):
    """
    Uses the .head attribute to return to the user the first N and last N rows of the dataframe, so the user can validate the information
        Parameters:
            df: a pandas dataframe
            rows: [INT] how many rows from first. Used in .head()
        Return:
            None. It will print the results.
    """
    try:
        if rows < 0:
            print("ERROR: Can't search a negative index row. Try again with positive index")
        else:  
            return df.head(rows)

    except TypeError as type_error:
        print()
        print(type(type_error).__name__, type_error, sep=": ")
        print("You must enter a valid argument[INT].")
        print("Run the program again and enter the correct argument.")

    except AttributeError as attribute_error:
        print()
        print(type(attribute_error).__name__, attribute_error, sep=": ")
        print("Can't find dataframe in arguments.")
        print("Run the program again and make sure to create dataframe and pass it to the function.")

def select_last_5_rows(df, rows):
    """
    Uses the .head attribute to return to the user the first N and last N rows of the dataframe, so the user can validate the information
        Parameters:
            df: a pandas dataframe
            rows: [INT] how many rows from first. Used in .head()
        Return:
            5 last rows
    """
    try:
        if rows < 0:
            print("ERROR: Can't search a negative index row. Try again with positive index")
        else: 
            return df.tail(rows)

    except TypeError as type_error:
        print()
        print(type(type_error).__name__, type_error, sep=": ")
        print("You must enter a valid argument[INT].")
        print("Run the program again and enter the correct argument.")

    except AttributeError as attribute_error:
        print()
        print(type(attribute_error).__name__, attribute_error, sep=": ")
        print("Can't find dataframe in arguments.")
        print("Run the program again and make sure to create dataframe and pass it to the function.")

def select_column(df, column, first_index=0, last_index=0):
    """
    Uses the .loc attribute to select column and return it to the user.
        Parameters:
            df: a pandas dataframe
            column: [STR] column to select from dataframe
            first_index: [INT] first index of row. Used in .loc
            last_index: [INT] last index of row. Used in .loc
        Return:
            df.loc with selected column
    """
    try:
        if first_index == 0 and last_index == 0:
            return df.loc[:, [column]]

        elif first_index == 0:
            return df.loc[:last_index, [column]]
        
        elif last_index == 0:
            return df.loc[first_index:, [column]]
        
        else:
            return df.loc[first_index:last_index, [column]]

    except TypeError as type_error:
        print()
        print(type(type_error).__name__, type_error, sep=": ")
        print("You must enter a valid index[INT].")
        print("Run the program again and enter the correct argument.")

def rename_column(df, original_column, new_column):
    """
    Uses the .rename attribute to select a column from dataframe, rename it, and return the new value. If users enters a non-existing column, the program won't change anything but still print the dataframe
        Parameters:
            df: a pandas dataframe
            original_column: [STR] the column  users wants to rename
            new_column: [STR] new column name to update
        Return:
            returns a df to update main dataframe with updated column
    """
    try:
        return df.rename(columns = {original_column : new_column})

    except TypeError as type_error:
        print()
        print(type(type_error).__name__, type_error, sep=": ")
        print("You must enter a valid type[STR].")
        print("Run the program again and enter the correct argument.")
    
    except KeyError as error:
        print(f"Key Error: {error}")
        print("Please, run the program again and enter a valid key")

def delete_column(df, column):
    """
    Uses the del command to delete a column from the dataframe.
        Parameters:
            df: a pandas dataframe
            coumn: [STR] desired column to be deleted
        Return:
            returns a df to update main dataframe with removed column
    """
    try:
        del df[column]

    except TypeError as type_error:
        print()
        print(type(type_error).__name__, type_error, sep=": ")
        print("You must enter a valid type[STR].")
        print("Run the program again and enter the correct argument.")
    
    except KeyError as error:
        print(f"Key Error: {error}")
        print("Please, run the program again and enter a valid key")
    
if __name__ == "__main__":
    main()
