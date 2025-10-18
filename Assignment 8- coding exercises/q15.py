#Author:Arthur drummond
#Date:17/10/2025
#A program that checks largest number of list of inputted numbers

numbers_input = input("Enter numbers separated by spaces: ")
number_strings = numbers_input.split()
numbers = [int(num) for num in number_strings]
largest = max(numbers)
print("The largest number is:", largest)
