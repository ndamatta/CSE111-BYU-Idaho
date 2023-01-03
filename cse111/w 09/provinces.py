
from typing import List


def main():
    list = read_list("provinces.txt")
    print(list)

def read_list(filename):

    text_list = []

    with open(filename, "rt") as text_file:

        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)

        #Removes first and last item
        text_list.pop()
        text_list.pop(0)

        #Changes AB to Alberta
        for province in range(len(text_list)):
            if text_list[province] == "AB":
                text_list[province] = "Alberta"

        #Count Alberta in list
        print("Alberta appears: ", text_list.count("Alberta"))
        

    return text_list 


if __name__ == "__main__":
    main()