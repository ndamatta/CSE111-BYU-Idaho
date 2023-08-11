#https://byui-cse.github.io/cse111-course/lesson01/check.html

#EXERCISE STATEMENT
"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""
#USER INPUT
age = int(input("Please, enter your age: "))

#VARIABLES AND ARITHMETIC
range = 220 - age
maximum_rate = range * 0.85
minimum_rate = range * 0.65

#OUTCOME
print(f"When you exercise to strengthen your heart, you should keep your heart rate between {minimum_rate:.0f} and {maximum_rate:.0f} beats per minute")