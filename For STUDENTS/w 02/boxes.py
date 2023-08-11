# https://byui-cse.github.io/cse111-course/lesson02/check.html
# W02 - CHECK POINT
import math

items_number = int(input("Enter the number of items: "))
items_perbox = int(input("Enter the number of items per box: "))

output =  math.ceil(items_number / items_perbox)

print(f"\nFor {items_number} items, packing {items_perbox} items in each box, you will need {output} boxes.")