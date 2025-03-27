##Vowel Checker:
#Write a Python program that takes a character as input and checks whether it is a vowel or not. Use the 
#if-else statement.

# vowel_let = ('a', 'e', 'i', 'o', 'u')
# alphabet_1 = input("enter a letter: ")
# if alphabet_1 in vowel_let:
#     print (f"you entered {alphabet_1} and it is vowel letter")
# else:
#     print (f"you enterd {alphabet_1} and it is consonent")

##Age Group Classification
# Child: 0-12 years
#  Teenager: 13-17 years
#  Adult: 18-64 years
#  Senior: 65 years and older

# age_group = int(input("enter age"))
# if age_group <= 12:
#     print(f"your age is {age_group}, your under child age group")
# elif age_group <= 17:
#     print(f"your age is {age_group}, your under Teenager age group")
# elif age_group <= 64:
#     print(f"your age is {age_group}, your under Adult age group")
# else:
#     print(f"your age is {age_group}, your under senior age group")

#Number Classifier:
#Write a program that takes an integer as input and classifies it as positive, negative, or zero.
#if-elif-else statement

# num_1 = int(input("enter value"))
# if num_1 > 0:
#     print(f"you entered a number {num_1}, and it is positive")
# elif num_1 < 0:
#     print(f"you entered a number {num_1}, and it is negative")
# else:
#     print(f"you entered a number {num_1}, and it is zero")


## Leap Year Checker:

# year = int(input("enter a year"))
# if (year %4 == 0 and year %100 != 0) or (year% 400 ==0):
#     print(f"you enter {year}, it is leap year")
# else:
#     print(f"you enter {year}, it is not leap year")

##Calculator:

# num_1 = int(input("enter a value "))
# num_2 = int(input("enter a value "))
# cal_operator = input("enter operator")
# if cal_operator == '+':
#     print(num_1+num_2)
# elif cal_operator == '-':
#     print(num_1 - num_2)
# elif cal_operator == '*':
#     print(num_1 * num_2)
# elif cal_operator == '/':
#     print(num_1 / num_2)
# else:
#     print("enter correct operator")


## Short Hand If:

# x = int(input("enter a value "))
# print(f"{x} is even") if x %2 == 0 else print (f"{x} is odd")

##Discount Calculator:

# og_price = 20000
# dis_percent = 10
# dis_cal = og_price*(dis_percent/100)
# og_price -= dis_cal
# print(og_price)

## BMI Calculator:

# weight_kg = int(input("enter your weight "))
# height_m = int(input("enter your height "))
# BMI = weight_kg / (height_m ^ 2)
# print(f"your weight is {weight_kg} and your height is {height_m} and BMI is {BMI} ")

# weight_kg = float(input("enter your weight "))
# height_m = int(input("enter your height "))
# BMI = weight_kg / (height_m ^ 2)
# print(f"your weight is {weight_kg} and your height is {height_m} and BMI is {BMI:.2f} ")

