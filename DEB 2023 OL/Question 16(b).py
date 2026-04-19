# Question 16(b)
# Name and School: Arthur

flight_number = input("Enter your flight number: ")
destination = input("Enter your destination: ")
num_ppl = int(input("Enter the number of people in the travel group: "))

print("Your flight number is", flight_number)
print("You are travelling to", destination)
print("There are", num_ppl, "people in the travel group")


if flight_number.upper() == "EI121":
    cost_per_person = 520
else:
    cost_per_person = 400


num_children = int(input("Enter the number of children in the travel group: "))

total_cost = (num_ppl * cost_per_person) - (num_children * 50)

print("The total cost of your flights is", total_cost)
