# String
# name = "Emmanuel"

# # Integer
# age = 18

# Float
# height = 1.75

# Complex Number
# complex_number = 4 + 7j

# Boolean
# is_student = True

# Print all variables
# print("String:", name)
# print("Integer:", age)
# print("Float:", height)
# print("Complex Number:", complex_number)
# print("Boolean:", is_student)


# creating a bewerries store for selling acholic drinks for guys that up to age 

age = int(input("How old are you"))
gender = input("What is your gender (male)/(female)")
if age >= 18 and (gender == "male" or gender == "female"):
    print("your are up to age you can proceed to buy")
elif age < 18:
    print("you are not up to the age to purchase")
else:
    print("Please enter a correct gender")