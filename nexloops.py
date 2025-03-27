###Sum of Squares
## Write a Python program that calculates and prints the sum of the squares of 
#  numbers from 1 to 5 using a for loop.

# sum = 0
# squ = 0
# for i in range(1, 6):
#     print(i*i)
#     squ = i*i
#     sum += squ
# print(f"sum of squares of numbers from 1 to 5 is {sum}")

### Countdown
##  Write a Python program that uses a while loop to print a countdown from 5 to 1.

# count = 5
# while count >= 1:
#     print(count)
#     count -= 1

###Multiplication Table with Nested For Loop
##Write a Python program to print the multiplication table for a user-specified number using a nested for loop.

# num = [int(input("enter the number "))]
# for i in num:
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i*j}")

###Write a Python program that uses a "for" loop to find the sum of all even numbers between 0 and 10

# sum = 0
# for i in range (0, 10):
#     i %2 == 0
#     print(i)
#     sum += i
# print(sum)


#### Calculate the sum of all numbers from 1 to a given number

# num_1 = int(input("Enter a number: "))
# total = 0  

# for i in range(1, num_1 + 1):
#     total += i  

# print("Sum of all numbers from 1 to", num_1, "is:", total)



###Display numbers from a list using loop

# list_1 = [1,2,3,4,5,6,7,8]
# for i in list_1:
#     print(i)

####Display numbers from -10 to -1 using for loop

# for i in range (-10, 0):
#     print(i)

###Write a program to display all prime numbers within a range
# num_1 = int(input("enter number "))
# num_2 = int(input("enter number "))
# for i in range (num_1, num_2):
#     for j in range(2,i):
#         if i%j == 0:
#             print(" not prime number ")
#         else:
#             print(" prime number")

# first_number = int(input("please enter first number in range: "))
# last_number = int(input("please enter last number in range: "))
    
# for num in range(first_number, last_number +1):
#     if num > 1: 
#         for i in range(2, num): 
#             if num % i == 0:
#                 break 
#         else:
#             print(num)
    