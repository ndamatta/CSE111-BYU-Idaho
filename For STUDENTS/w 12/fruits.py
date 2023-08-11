
def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    #reverse and print
    fruit_list.reverse()
    print(fruit_list)

    #append orange
    fruit_list.append("orange")
    print(fruit_list)

    #insert cherry before apple
    fruit_list.insert(1, "cherry")
    print(fruit_list)

    #sort and print
    fruit_list.sort()
    print(fruit_list)

    #clear
    fruit_list.clear()
    print(fruit_list)
 

if __name__ == "__main__":
    main()