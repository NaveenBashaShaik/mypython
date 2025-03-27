#data structures

#list data type
#mutable, ordered sequence of elements, elements can be different data types, []
# list_1  = [20,3.5,"Naveen"]
# print (list_1)
# print(type(list_1))
# list_1.append("Basha")
# print(list_1)
# print(id(list_1))

# list_1  = [20,3.5,"Naveen",(1,2,3,4),[3,4,5,6]] #in side list we can use tuple and list.
# print(list_1)

#tuple data type
#immutable, ordered sequence of elements, elements can be different data types, cannot be modify,()
# tuple_1 = (1,2,3,5,5,5,5,5,"Ajay","Tarun", [1,2,3,4,5])
# print(tuple_1)
# print(type(tuple_1))
# print(id(tuple_1))

# tuple_1 = (1,2,3,5,5,5,5,5,"Ajay","Tarun", [1,2,3,4,5],(3,4,5,6,7,8))
# print(tuple_1)    #in side tuple we can use list and tuple

#sets data types
#mutable data type, unordered collection of unique elements,in elements contains immutable,{}

# set_1 = {1,2,8,9,0,3,"Naveen", 1234,3456, "Basha"}
# print(set_1)
# print(type(set_1))
# print(id(set_1))

# set_3 = {1,2,8,9,0,3,"Naveen", 1234,3456, "Basha",1,2,8,9,6,1234,3456,3}
# print(set_3)
# print(type(set_3))
# print(id(set_3))


#complex data types
#consists of real part and imaginary part, it's written in the form a + bj

#a --> real part (int or float)
#b --> imaginary part (int or float)

# a = 2 + 3j
# b = 1 - 4j
# print ("addition", a + b)

#dictionaries
#ordered collection of key-value pairs
#keys must be unique within a dictionary
#dictionaries are defined used curly braces {} and colons :

# accounts = {
#     "user1" : "password1",
#     "user2" : "password2",
#     "user3" : "password3",
# }
# print (accounts)
# print (type(accounts))
# print (id(accounts))


#boolean data types
# sample = True
# sample_1 = False
# print(sample)
# print(sample_1)
# print(type(sample))
# print(type(sample_1))

# print(bool(0))
# print(bool(1))

#f- strings    (format strings), result readable, python3.6 version is using f strings
# num1 = int(input("enter a value"))
# num2 = int(input("enter a value"))
# # result = num1 + num2
# # print(f"num1 value is {num1},num2 value is {num2} and result is {result}")
# print(f"num1 value is {num1},num2 value is {num2} and result is {num1 + num2}")

#type conversion
#int ---> float
# num = 10
# print(type(num))
# float_conversion = float(num)
# print (float_conversion)
# print (type(float_conversion))

#float ---> int
# height = 5.8
# print (height)
# print(type(height))
# int_conversion = int(height)
# print(int_conversion)
# print(type(int_conversion))

#int ---> str

# age = 25
# print (age)
# print(type(age))
# str_conversion = str(age)
# print(str_conversion)
# print(type(str_conversion))

#str ---> int

# ticket_num = "12289183"
# print(ticket_num)
# print(type(ticket_num))
# int_conversion = int(ticket_num)
# print(int_conversion)
# print(type(int_conversion))

#str ---> float
# user_num = "8732879217"
# print(user_num)
# print(type(user_num))
# float_conversion = float(user_num)
# print(float_conversion)
# print(type(float_conversion))


#input function

#string concatination
# user_1 = input("enter first subject marks")
# user_2 = input("enter first subject marks")
# result = user_1 + user_2
# print(result)

#convert to integer

# user_1 = int(input("enter first subject marks: "))
# user_2 = int(input("enter first subject marks: "))
# result = user_1 + user_2
# print(result)


#convert to float

# user_1 = float(input("enter first subject marks: "))
# user_2 = float(input("enter first subject marks: "))
# result = user_1 + user_2
# print(result)



#exercise

#Write a program that prints a pattern using multiple print statements.

# print('££££')
# print("******")
# print('''**********''')

#Create a Python script for a simple task and add comments to explain each step.

#below code performs addition

# a = 30
# b = 50
# c = a + b 
# print (c)

#multi line comments
'''
above code had two variables, a variable contains 30. b variable contains 50
here variable c stores result value. To get a result two variables performs addition and gave
resultant value

'''

#Implement a program that uses a dictionary to store information about a book
#(title, author, publication year).

# book_name = {
#     "title" : "The Roasting Tin",
#     "author" : "Rukmini Lyer",
#     "publication_year" : "2017",
# }
# print (book_name)
# print (type(book_name))
# print (id(book_name))

#Write a python program that takes a string as input  35  and return float value.

# order_id = "35"
# print(order_id)
# print(type(order_id))
# float_conversion = float(order_id)
# print(float_conversion)
# print(type(float_conversion))

#Write a program to take two names as input and print them together

# emp_name = "Naveen"
# emp_surname = "Sk"
# print(emp_name + emp_surname)

#Create a program that takes user input for their age, converts it to an integer, adds 5, and then prints the result.

# age = "25"
# print (age)
# print(type(age))
# int_conversion = int(age)
# int_conversion_new = int_conversion + 5
# print(int_conversion_new)
# print(type(int_conversion_new))
# print(id(int_conversion_new))

#Build a calculator program that takes two numbers as input and performs the arithmetic operation.

# marks_1 = int(input("enter subject marks"))
# marks_2 = int(input("enter subject marks"))
# print(marks_1 + marks_2)