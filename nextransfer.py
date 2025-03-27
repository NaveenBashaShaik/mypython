########Using break in a While Loop
'''Write a Python program that takes a list of numbers as input numbers = [25, 30, 20, 40, 15, 25]
and prints the sum of the numbers. However, if the sum exceeds 100, stop adding numbers and 
 print "Sum exceeded 100".'''

# nums = [25, 30, 20, 40, 15, 25]
# sum = 0
# for i in nums:
#     i += 1
#     sum += i
#     if sum > 100:
#         break
#     print ("Sum exceeded 100")

######### Using continue in a For Loop

'''
Write a Python script that uses a for loop to iterate through numbers from 1 to 
600. Print only the odd numbers, skipping the even ones using the 
statement.

'''
# for i in range (1, 601):
#     if i%2 == 0:
#         continue
#     print(i)

#####Using pass in Conditional Statements
'''
Write a Python script that checks if a number is even or odd. If the number is 
even, print "Even"; if odd, do nothing (use the 
pass statement).

'''
# num_1 = 2
# for i in range (1, num_1):
#     if i%2==0:
#         print("Even")
#         pass

##########Combining Transfer Statements
'''
 Write a Python script that iterates through a list of words. If the word is "break," 
exit the loop using the 
break statement. If the word is "skip," skip the rest of the 
code for the current iteration using the 
continue statement. For any other word, 
print the word.

'''

# list_1 = ["skip","start", "break","standby","proceed","check","skip","skip","skip","success"]
# for i in list_1:
#     if i == "break":
#         break
#     if i == "skip":
#         continue
#     print(i)
