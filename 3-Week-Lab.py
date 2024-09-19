# Exercise 1 - Day of the Week
# number = int(input("Enter a number between 1 - 7: "))
#
# if number < 1 or number > 7:
#     print(f"{number} is not between 1 - 7")
# elif number == 1:
#     print(f"The number {number} is Monday.")
# elif number == 2:
#     print(f"The number {number} is Tuesday.")
# elif number == 3:
#     print(f"The number {number} is Wednesday.")
# elif number == 4:
#     print(f"The number {number} is Thursday.")
# elif number == 5:
#     print(f"The number {number} is Friday.")
# elif number == 6:
#     print(f"The number {number} is Saturday.")
# elif number == 7:
#     print(f"The number {number} is Sunday.")

# ----------------------------------------------------------------------------------

# Exercise 2 - Areas of Rectangles

# length_one = int(input("What is the length of the first rectangle: "))
# width_one = int(input("What is the width of the first rectangle: "))
# area_one = length_one * width_one
# print(f"The area of the first rectangle is: {area_one}")
#
#
# length_two = int(input("What is the length of the second rectangle: "))
# width_two = int(input("What is the width of the second rectangle: "))
# area_two = length_two * width_two
# print(f"The area of the second rectangle is: {area_two}")
#
# if area_one == area_two:
#     print(f"The two rectangles have the same area.")
# elif area_one > area_two:
#     print(f"The first rectangle has a greater area")
# else:
#     print(f"The second rectangle has a greater area")

# ----------------------------------------------------------------------------------

# Exercise 3 - Age Classifier
# age = int(input("How old are you? "))
# if age <= 1:
#     print("You are an infant.")
# elif age > 1 and age < 13:
#     print("You are a child.")
# elif age >= 13 and age <= 20:
#     print("You are a teenager.")
# else:
#     print("You are an adult.")

# ----------------------------------------------------------------------------------

# Exercise 4 - Roman Numerals
# number = int(input("Enter a number between 1 - 10: "))
# if number < 1 or number > 10:
#     print(f"{number} is not between 1 - 10")
# elif number == 1:
#     print(f"The Roman Numeral for {number} is I")
# elif number == 2:
#     print(f"The Roman Numeral for {number} is II")
# elif number == 3:
#     print(f"The Roman Numeral for {number} is III")
# elif number == 4:
#     print(f"The Roman Numeral for {number} is IV")
# elif number == 5:
#     print(f"The Roman Numeral for {number} is V")
# elif number == 6:
#     print(f"The Roman Numeral for {number} is VI")
# elif number == 7:
#     print(f"The Roman Numeral for {number} is VII")
# elif number == 8:
#     print(f"The Roman Numeral for {number} is VIII")
# elif number == 9:
#     print(f"The Roman Numeral for {number} is IX")
# elif number == 10:
#     print(f"The Roman Numeral for {number} is X")

# ----------------------------------------------------------------------------------

# Exercise 5 - Mass and Weight
# mass = int(input("What is the object's  mass? "))
# weight = mass * 9.8
#
# if weight > 500:
#     print(f"{weight:.2f} it is too heavy.")
# elif weight < 100:
#     print(f"{weight:.2f} it is too light.")
# else:
#     print(f"{weight:.2f} it is alright.")

# ----------------------------------------------------------------------------------

# Exercise 6 - Magic Dates
# month = int(input("Enter a month (in numeric form): "))
# day = int(input("Enter a day: "))
# year = int(input("Enter a two-digit year: "))
# magic = month * day
#
# if magic == year:
#     print(f"{month} x {day} = the year {year}. The date is magic")
# else:
#     print(f"The date is not magic.")

# ----------------------------------------------------------------------------------

# Exercise 7 - Color Mixer

# primary_one = input("Enter a primary color (Red, Blue, Yellow): ").lower()
# primary_two = input("Enter a another primary color (Red, Blue, Yellow): ").lower()
#
# if primary_one == "red" and primary_two == "blue":
#     print(f"{primary_one} and {primary_two} combined turns to purple.")
# elif primary_one == "red" and primary_two == "yellow":
#     print(f"{primary_one} and {primary_two} combined turns to orange.")
# elif primary_one == "blue" and primary_two == "yellow":
#     print(f"{primary_one} and {primary_two} combined turns to green.")
# else:
#     print("One is not a primary color.")

# ----------------------------------------------------------------------------------

# Exercise 8 - Hot Dog Cookout Counter

# hotdog_package = 10
# hotdog_buns = 8
#
# people = int(input("How many people are invited to the cookout? "))
# dog_per_person = int(input("How many hotdogs is everyone going to eat? "))
#
# total_hotdogs_needed = people * dog_per_person
#
# amount_hotdogs_packages = (total_hotdogs_needed + hotdog_package - 1) // hotdog_package
# total_hotdogs = amount_hotdogs_packages * hotdog_package
#
# amount_buns_packages = (total_hotdogs_needed + hotdog_buns - 1) // hotdog_buns
# total_buns = amount_buns_packages * hotdog_buns
#
# dogs_left_over = total_hotdogs - total_hotdogs_needed
# buns_left_over = total_buns - total_hotdogs_needed
#
# print(f"Minimum packages of hotdogs required: {amount_hotdogs_packages}")
# print(f"Minimum packages of hotdog buns required: {amount_buns_packages}")
# print(f"Number of hotdogs left over: {dogs_left_over}")
# print(f"Number of hotdog buns left over: {buns_left_over}")

# ----------------------------------------------------------------------------------

# Exercise 9 - Roulette Wheel Colors

# num = int(input("Enter a pocket number: "))
#
# if num == 0:
#     print("The pocket is green!")
# elif num > 1 and num < 10:
#     if num % 2 == 0:
#         print(f"The number is {num} and the pocket is black.")
#     else:
#         print(f"The number is {num} and the pocket is red.")
# elif num >= 11 and num < 18:
#     if num % 2 == 0:
#         print(f"The number is {num} and the pocket is red.")
#     else:
#         print(f"The number is {num} and the pocket is black.")
# elif num >= 19 and num < 28:
#     if num % 2 == 0:
#         print(f"The number is {num} and the pocket is black.")
#     else:
#         print(f"The number is {num} and the pocket is red.")
# elif num >= 29 and num < 36:
#     if num % 2 == 0:
#         print(f"The number is {num} and the pocket is red.")
#     else:
#         print(f"The number is {num} and the pocket is black.")
# else:
#     print(f"{num} is not between 1 - 36")

# ----------------------------------------------------------------------------------

# Exercise 10 - Money Counting Game

# print("You need to make $1.00 in exact change.")
# amount_pennies = float(input("Enter the amount of pennies: "))
# amount_nickels = float(input("Enter the amount of nickels: "))
# amount_dimes = float(input("Enter the amount of dimes: "))
# amount_quarters = float(input("Enter the amount of quarters: "))
#
# penny = 0.01
# nickel = 0.05
# dime = 0.1
# quarter = 0.25
# dollar = 1
#
# total_pennies = amount_pennies * penny
# total_nickels = amount_nickels * nickel 
# total_dimes = amount_dimes * dime 
# total_quarters = amount_quarters * quarter 
#
# overall_total = total_pennies + total_nickels + total_dimes + total_quarters
#
# if overall_total == dollar:
#     print("Congratulations you won!")
# else:
#     if overall_total > dollar:
#         print(f"Thats a little too much change. Total change was ${overall_total:.2f}")
#     else:
#         print(f"That is not enough for a dollar. Total change was ${overall_total:.2f}")

# ----------------------------------------------------------------------------------

# Exercise 11 - Book Club Points

# num_books = int(input("How many books did you purchase the month? "))
#
# if num_books >= 8:
#     print("With a purchase of 8 or more books you earn 60 points.")
# elif num_books >= 6:
#     print("With a purchase of 6 books you earn 30 points.")
# elif num_books >= 4:
#     print("With a purchase of 4 books you earn 15 points.")
# elif num_books >= 2:
#     print("With a purchase of 2 books you earn 5 points.")
# else:
#     print("Since no didn't purchase any books you earned 0 points")

# ----------------------------------------------------------------------------------

# Exercise 12 - Software Salse

# packages_purchased = float(input("Enter the amount of packages you would like to purchase: "))
#
# package_cost = 99
#
# if packages_purchased >= 10 and packages_purchased < 19:
#     cost = packages_purchased * package_cost
#     discount = cost * .1
#     total = cost - discount 
#     print(f"Your discount would be 10% and total discount is ${discount:.2f} off.")
#     print(f"Your total would be ${total:.2f}.")
# elif packages_purchased >= 20 and packages_purchased < 49:
#     cost = packages_purchased * package_cost
#     discount = cost * .2
#     total = cost - discount 
#     print(f"Your discount would be 20% and total discount is ${discount:.2f} off.")
#     print(f"Your total would be ${total:.2f}.")
# elif packages_purchased >= 50 and packages_purchased < 99:
#     cost = packages_purchased * package_cost
#     discount = cost * .3
#     total = cost - discount 
#     print(f"Your discount would be 30% and total discount is ${discount:.2f} off.")
#     print(f"Your total would be ${total:.2f}.")
# elif packages_purchased >= 100:
#     cost = packages_purchased * package_cost
#     discount = cost * .4
#     total = cost - discount 
#     print(f"Your discount would be 40% and total discount is ${discount:.2f} off.")
#     print(f"Your total would be ${total:.2f}.")
# else:
#     cost = packages_purchased * package_cost
#     print("Your total would be ${cost:.2f}.")

# ----------------------------------------------------------------------------------

# Exercise 13 - Shipping charges

# weight = int(input("Enter the amount of pounds the package weighs: "))
#
# if weight <= 2:
#     rate_per_pound = weight * 1.50
#     print(f"The cost of shipping is ${rate_per_pound:.2f}")
# elif weight > 2 and weight <= 6:
#     rate_per_pound = weight * 3.00
#     print(f"The cost of shipping is ${rate_per_pound:.2f}")
# elif weight > 6 and weight <= 10:
#     rate_per_pound = weight * 4.00
#     print(f"The cost of shipping is ${rate_per_pound:.2f}")
# elif weight > 10:
#     rate_per_pound = weight * 4.75
#     print(f"The cost of shipping is ${rate_per_pound:.2f}")

# ----------------------------------------------------------------------------------

# Exercise 14 - Time Calculator

# seconds = int(input("Enter the number of seconds: "))
#
# if seconds >= 86400:
#     days = seconds // 86400
#     seconds = seconds % 86400
#     hours = seconds // 3600
#     seconds = seconds % 3600
#     minutes = seconds // 60
#     seconds = seconds % 60
#     print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
# elif seconds >= 3600:
#     hours = seconds // 3600
#     seconds = seconds % 3600
#     minutes = seconds // 60
#     seconds = seconds % 60
#     print(f"{hours} hours, {minutes} minutes, {seconds} seconds")
# elif seconds >= 60:
#     minutes = seconds // 60
#     seconds = seconds % 60
#     print(f"{minutes} minutes, {seconds} seconds")
# else:
#     print(f"{seconds} seconds")

# ----------------------------------------------------------------------------------

# Exercise 15 - February days

# Get the year from the user
# year = int(input("Enter a year: "))
#
# if year % 100 == 0:
#     if year % 400 == 0:
#         print(f"In {year} February has 29 days.")
#     else:
#         print(f"In {year} February has 28 days.")
# elif year % 4 == 0:
#     print(f"In {year} February has 29 days.")
# else:
#     print(f"In {year} February has 28 days.")

# ----------------------------------------------------------------------------------

# Exercise 16 - Wi-Fi Diagnostic Tree

# print("Reboot the computer and try to connect.")
# response = input("Did that fix the problem? (yes/no) ").lower()
#
# if response == "yes":
#     print("Problem solved!")
# else:
#     print("Reboot the router and try to connect.")
#     response = input("Did that fix the problem? (yes/no) ").lower()
#
#     if response == "yes":
#         print("Problem solved!")
#     else:
#         print("Make sure the cables between the router and modem are plugged in firmly.")
#         response = input("Did that fix the problem? (yes/no) ").lower()
#
#         if response == "yes":
#             print("Problem solved!")
#         else:
#             print("Move the router to a new location.")
#             response = input("Did that fix the problem? (yes/no) ").lower()
#
#             if response == "yes":
#                 print("Problem solved!")
#             else:
#                 print("Get a new router.")

# ----------------------------------------------------------------------------------

# Exercise 17 - Restaurant Selector

vegetarian = input("Is anyone in your party a vegetarian? (yes/no) ").lower()
vegan = input("Is anyone in your party a vegan? (yes/no) ").lower()
gluten_free = input("Is anyone in your party gluten-free? (yes/no) ").lower()

print("Here are your restaurant choices:")

if vegetarian == "no" and vegan == "no" and gluten_free == "no":
    print("Joe's Gourmet Burgers")

if vegetarian == "yes" and vegan == "no" and gluten_free == "yes":
    print("Main Street Pizza Company")
if vegetarian == "yes" and vegan == "no" and gluten_free == "no":
    print("Main Street Pizza Company")
if vegetarian == "no" and vegan == "no" and gluten_free == "yes":
    print("Main Street Pizza Company")

if vegetarian == "yes" and vegan == "yes" and gluten_free == "yes":
    print("Corner Café")
if vegetarian == "yes" and vegan == "yes" and gluten_free == "no":
    print("Corner Café")
if vegetarian == "yes" and vegan == "no" and gluten_free == "yes":
    print("Corner Café")
if vegetarian == "yes" and vegan == "no" and gluten_free == "no":
    print("Corner Café")

if vegetarian == "yes" and vegan == "no":
    print("Mama's Fine Italian")

if vegetarian == "yes" and vegan == "yes" and gluten_free == "yes":
    print("The Chef's Kitchen")
if vegetarian == "yes" and vegan == "yes" and gluten_free == "no":
    print("The Chef's Kitchen")
if vegetarian == "yes" and vegan == "no" and gluten_free == "yes":
    print("The Chef's Kitchen")

































