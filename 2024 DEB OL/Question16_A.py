# Question 16(a)
# Name and School: Arthur

print("Household budget calculator.  Enter the following information:")


num_adults = int(input("Number of adults in household: "))
num_child = int(input("Number of children in household: "))

food_budget = 300
cost_food_adults = 50
cost_food_child = 35
child_allowance = 140


inflation_rate = float(input("Inflation rate (e.g. 0.05 for 5% inflation): "))


if num_child > 3:
    allowance_total = child_allowance * num_child + 20 * (num_child - 3)
else:
    allowance_total = child_allowance * num_child

food_cost = cost_food_adults * num_adults + cost_food_child * num_child


food_inflate = food_cost * (1 + inflation_rate)


food_inflate = round(food_inflate, 2)


percentage = round(food_inflate / allowance_total * 100, 2)


budget_remaining = allowance_total + food_budget - food_inflate

print("Children's allowance total: €" + str(allowance_total))
print("Total household food cost: €" + str(food_cost))
print("Total household food cost with inflation: €" + str(food_inflate))
print("Percentage spend on food: " + str(percentage) + "%")
print("Budget remaining after food spend: €" + str(budget_remaining))
