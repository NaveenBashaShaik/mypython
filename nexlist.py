#######Reverse List:
'''
Write Python code to reverse the order of elements in the given list 
Print the reversed list.

'''
# list_1 = [10, 20, 30, 40, 50, 11]
# list_1.reverse()
# print(list_1)

######## Common Elements:
'''
Given two lists list1 and list2 , find and print the common elements between them
'''
# empty = []
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# for i in list1:
#     if i in list2:
#         empty.append(i)
# print(empty)        



###### Unique Elements:  
'''
Create a new list unique_list containing only the unique elements from the 
given list original_list . Print the unique list.
'''
# empty = [] 
# original_list = [1, 2, 2, 3, 4, 4, 5]
# for i in original_list:
#     if i not in empty:
#         empty.append(i)
# print(empty)

### Remove Duplicates:
'''
Remove duplicate elements from the given list duplicated_list and print the list
without duplicates while preserving the order.

'''
# empty = list()
# duplicated_list = [1, 2, 2, 3, 4, 4, 5]
# result = [empty.append(i) for i in duplicated_list if i not in empty]
# print(empty)

####### List Concatenation
'''
 Write a Python script that concatenates two lists and prints the result.
'''

# list_1 = [2,3,4,5,6]
# list_2 = [8,9,1,2]
# conc_list = list_1 + list_2
# print(conc_list)

###### List Repetition

'''
 Write a Python script that repeats a list three times and prints the result.
'''
# list_1 = [2,3,4,5,6]
# re_list = list_1 * 3
# print(re_list)


#########List Removal
''''
Write a Python script that removes the elements at even indices from a list.
'''

# list_1 = [2,3,4,5,6,8,9,10,1]
# for i in list_1:
#     if i%2 == 0:
#         list_1.remove(i)
# print(list_1)

#####List Insertion

'''
Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of 
a list
'''

# list_1 = [1,2,3,4,5,6,7,8,9]
# for i in reversed([10,11,12]):
#     list_1.insert(0,i)
# print(list_1)


########## List comprehensions


'''
 Create a list of squares of numbers from 1 to 10.
'''

# print([i ** 2 for i in range (1,11)])


'''Generate a list of even numbers from 1 to 20.'''


# print([num for num in range(1,21) if num%2 == 0])


'''Given a list of words, create a list containing the lengths of each word'''

words = ["apple", "banana", "cherry", "date"]
# for i in words:
#     print(len(i))

# print([len(i) for i in words])