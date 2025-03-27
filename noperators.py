#operator ---> symbol or keyword that performs an operation on one or more operands
#opeerand ---> Value or Variable acted upon by an operator to produce a result

# + (Addition): Adds two operands.

# num_1 = 20
# num_2 = 10
# result = num_1 + num_2
# print(result)

# - (Subtraction): Subtracts the right operand from the left operand.

# num_1 = 30
# num_2 = 20
# result = num_1 - num_2
# print(result)

# * (Multiplication): Multiplies two operands.

# num_1 = 3
# num_2 = 5
# result = num_1 * num_2
# print(result)

#  ** (Exponentiation): Raises the left operand to the power of the right operand.

# num_1 = 4
# num_2 = 3
# result = num_1 ** num_2
# print(result)

# / (Division): Divides the left operand by the right operand.

# num_1 = 8
# num_2 = 4
# result = num_1 / num_2
# print(result)

# // (Floor Division): Returns the quotient of the division, discarding the remainder.

# num_1 = 9
# num_2 = 4
# result = num_1 // num_2
# print(result)

#  % (Modulus): Returns the remainder of the division of the left operand by the right operand.

# num_1 = 9
# num_2 = 4
# result = num_1 % num_2
# print(result)

# Assignment operator or compound assignment operator (+=, -=, *=, /=)


# num_1 = 20
# num_1 += 10 #eq ---> num_1 = num_1 + 10
# print (num_1)

# num_1 = 2
# num_1 *= 3 #eq ---> num_1 = num_1 * 3
# print (num_1)

# num_1 = 20
# num_1 -= 8 #eq ---> num_1 = num_1 - 3
# print (num_1)

#comparison operators
#performs boolean operator result(True or False)
# == (Equal to), != (Not equal to), < (Less than), > (Greater than), <= (Less than or equal to)

# product_cost_1 = 2000
# product_cost_2 = 8000
# print(product_cost_1 == product_cost_2)

# product_cost_1 = 2000
# product_cost_2 = 2000
# print(product_cost_1 == product_cost_2)

# product_cost_1 = 2000
# product_cost_2 = 3000
# print(product_cost_1 != product_cost_2)

# product_cost_1 = 2000
# product_cost_2 = 1000
# print(product_cost_1 > product_cost_2)

# product_cost_1 = 2000
# product_cost_2 = 3000
# print(product_cost_1 < product_cost_2)

# product_cost_1 = 2000
# product_cost_2 = 2000
# print(product_cost_1 >= product_cost_2)

# product_cost_1 = 2000
# product_cost_2 = 2000
# print(product_cost_1 <= product_cost_2)

#Logical operators
# Logical operators are used to combine multiple conditions. The basic logical operators are:
# and (logical AND), or (logical OR), not (logical NOT)

# user_name = "naveen"
# passwrd = 123
# otp = 1342
# print(user_name == "naveen" and passwrd == 123 and otp == 1342)


# user_name = "naveen"
# passwrd = 123
# otp = 1342
# print(user_name == "naveen" or passwrd == 122 or otp == 1342)

# sample = True
# print(not(sample))

#identity operator
# Identity operators are used to check if two variables refer to the same object.
#  is Returns True if both variables are the same object.
#  is not  Returns True if both variables are not the same object.

# sample = [1,2,3]
# print(id(sample))
# a = sample
# print(id(a))
# sample_2 = [1,2,3]
# print(id(sample_2))
# print(sample is a)
# print(sample is sample_2)
# print(sample is not sample_2)



#Membership operator
# Membership operators are used to test whether a value is a member of a sequence (e.g., a list, tuple, or string).

# fruits = ["apples","oranges","grapes"]
# print("blueberries" in fruits)
# print("blueberries" in fruits)

# Output Formatting (F-strings)


# num_1 = 9
# num_2 = 4
# result = num_1 % num_2
# print(result)
# print(f"num_1 value is {num_1} and num_2 value is {num_2} and result is {result}")


# num_1 = 4
# num_2 = 3
# result = num_1 ** num_2
# print(result)
# print(f"base is {num_1} and expo is {num_2} and final result is {result}")

#discount
# product_cost = 10000
# discount = 5
# result = product_cost * (discount/100)
# product_cost -= result #eq ---> prod = prod - result
# print(product_cost)
# print(f"discount given {discount}% and final discount {result} and total cost after discount {product_cost}")

#Exercise
#Write a Python program to calculate the area of a rectangle using the given formula: area = length * width . Take the values of length and width as inputs from the user.

# length_1 = 2
# width_1 = 3
# area_1 = length_1 * width_1
# print(area_1)
# print(f"length value is {length_1} and width value is {width_1} and area result {area_1}")

#Write a Python program to demonstrate incrementing and decrementing a variable

# num_1 = int(input("enter number"))
# num_2 = int(input("enter number"))
# num_1+= 20
# num_2-= 1
# print(num_1)
# print(num_2)

#Write a Python program to convert temperature from Celsius to Fahrenheit.

# cels = int(input("enter value"))
# Fahrenh = ((cels * 9/5) + 32)
# print(Fahrenh)

#Write a Python program to calculate the simple interest given the principal amount, rate, and time 

# amount_1 = int(input("enter value"))
# rate_1 = float(input("enter value"))
# time_1 = int(input("enter value"))
# interest_1 = (amount_1*rate_1*time_1)/100
# print(interest_1)

# Write a Python program to concatenate two strings and display the result.

# user_name = "naveen"
# user_surname = "sk"
# print(user_name + user_surname)

# Write a Python program to convert a distance from kilometers to miles.

# kilometers = int (input("enter distance"))
# miles = kilometers * 0.62
# print (miles)

#Create a program that takes user input for their name and age. Use formatted strings (f-strings)

# user_name = "naveen"
# age = "25"
# result = user_name + age
# print(f"user name is {user_name} and age is {age} and welcome note is {result}")

#Write a Python script that defines a dictionary with information about a product

# Laptop = {
#     "device_name": "lenovo",
#     "device_price": "25000",
#     "device_quantity": "1"
# }
# print(f"device name is {Laptop['device_name']} and device price is {Laptop['device_price']} and device quantity is {Laptop['device_quantity']}")

#Create a list called numbers that contains integers from 1 to 10.

# num_1 = [1,2,3,4,5,6,7,8,9,10]
# print (5 in num_1)
# print(15 not in num_1)