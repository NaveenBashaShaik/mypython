'''You are given a string sentence. Print the characters at even indices.'''

sentence = "Python is amazing"
empty = []
for i in range(len(sentence)):
    if i%2 == 0:
        empty.append(sentence[i])    
print("".join(empty))


'''
You are given a string s. Replace all spaces in the string
with underscores (_) and print the modified string.
'''

# s = "Python is fun and powerful"
# underscores = s.replace(" ", "_")
# print(underscores)

'''
You are given a string s. Check if the string contains only digits.

'''


# s = "12345"
# print(s.isdigit())


'''
You are given a string s. Print the string in reverse order.

'''

# s = "Python is amazing"
# print(s[::-1])

'''
You are given a string s . Capitalize the first letter of each word in the string 
and print the modified string.

'''

# s = "python programming is fun"
# print(s.title())