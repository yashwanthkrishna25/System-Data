# name = input("Enter your name: ")
# print("Your name is :", name)


# name = input("Enter your name: ")
# print("Your name is :", name)

# # Variable initialization
# a = 9
# b = 5
# c = 2
# d = 7
# e = 9
# f = 9
# h = 2

# # Step-by-step calculation:
# # part1 = a - b - c           => 9 - 5 - 2 = 2
# # part2 = d * f / h           => 7 * 9 / 2 = 63 / 2 = 31.5
# # part3 = part1 * part2       => 2 * 31.5 = 63.0
# # part4 = a * b + c           => 9 * 5 + 2 = 45 + 2 = 47
# # combined = part3 + part4    => 63.0 + 47 = 110.0
# # final = combined * (d * e)  => 110.0 * (7 * 9) = 110.0 * 63 = 6930.0

# result = ((((a - b - c) * (d * f / h)) + (a * b + c)) * (d * e))

# # Output the result
# print("The result is:", result)


# a = 10
# b = 3.14
# c = 3 +4j
# # print(type(a),type(b),type(c))  
# # # <class 'int'>
# print("\n",a,"\n",b,"\n",c)
# a = input("Enter a value: ")
# try:
#     a = int(a)
#     print("You entered an integer:", a)
#     print("Type:",type(a))
# except ValueError:
#     try:
#         a = float(a)
#         print("You entered a float:", a)
#         print("Type:", type(a))
#     except ValueError:
#         print("You entered a string:", a)
#         print("Type:", type(a))
"""
pailamdrome Question 
s = input("Enter a pailamdrome: ")
if s == s[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")"""
# text = input("enter a text:")
# print(type(text))
# List (Mutable, Ordered)

"""list=[1,2,3,"Yash"]
list.append(4)
list.insert(2, "Python")
list.remove(3)
list.pop(0)
print(list)"""

# Tuple (Immutable, Ordered)

"""tuple = (1, 2, 3, "Yash")
print(tuple[3])  # Accessing the first element"""

# Range (Sequence of Numbers)
"""r = range(1, 30, 2)
print("Range:", list(r))  # Convert range to list for display
"""
# Set Types: set , frozenset
'''set = {1, 2, 3,  3, 2, 4,5,"Yash"}
print("Set:", set)  # Display the set'''

'''f = frozenset({1, 2, 3,3 , 4, 2, 4, 5, "Yash"})
print("Frozenset:", f)  # Display the frozenset
'''
'''dict={"name":"Yash","year":2004}
print("Name:", dict["name"])  # Accessing value by key
print("Year:", dict["year"])  # Accessing value by key'''\

# Type Casting and Type Checking

'''a = "Yash"
b = str(a)
print("String to Integer:", b)  # Convert string to integer# Convert integer to float
print("Type of a:", type(a))  # Check type of a'''

# Taking User Input ( input() function)

'''import datetime

# Get user input
name = input("Enter your name: ")
birth_day = int(input("Enter your birth day (1-31): "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_year = int(input("Enter your birth year (e.g., 2000): "))

# Current date
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)

# Calculate age
age = today.year - birth_year
if (today.month, today.day) < (birth_month, birth_day):
    age -= 1

# Birthday check
if (tomorrow.day == birth_day) and (tomorrow.month == birth_month):
    print(f"\n🎉 Hello {name}, tomorrow is your birthday!")
    print(f"🎂 You will be turning {age + 1} years old. Happy Birthday in advance! 🎈")
else:
    print(f"\nHello {name}, you are {age} years old.")'''

# print("Hello, Yash!")
# print(10,20,30)
# print("Yash!", "is","fun ", sep="  ")

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print(f"Hello, {name}! You are {age} years old.")

# Operators and Expressions
# import operator
# import math
# a = input("Enter first number: ")
# b = input("Enter second number: ")
# try :
#     a = int(a)
#     b = int(b)
# except ValueError:
#     print("Please enter valid integers.")
#     exit()
# # Arithmetic Operations
# print("Arithmetic Operations:")
# print("Addition:", operator.add(a, b))
# print("Subtraction:", operator.sub(a, b))   
# print("Multiplication:", operator.mul(a, b))
# print("Division:", operator.truediv(a, b))

# print("Floor Division:", operator.floordiv(a, b))
# print("Modulus:", operator.mod(a, b))
# print("Exponentiation:", operator.pow(a, b))
'''a, b = input("Enter two numbers separated by space: ").split()
try:
    a = int(a)
    b = int(b)
except ValueError:
    print("Please enter valid integers.")
    exit()
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a %b)
print(a ** b)'''

# compariSon operators

'''import operator
x = input("Enter two numbers separated by space: ").split()
y = input("Enter two numbers separated by space: ").split()

print("Comparison Operations:")
print("Equal:",(x== y))
print("Not Equal:",(x!= y))
print("Greater than:",(x< y))
print("Less than:",(x> y))
print("Greater than or equal to:",(x<= y))
print("Less than or equal to:",(x>= y))'''

# Logical Operators ( and , or , not )
'''import operator
a = input("Enter first boolean value (True/False): ")
b = input("Enter second boolean value (True/False): ")
try:
    a = a.lower() == 'true'
    b = b.lower() == 'true'
except ValueError:
    print("Please enter valid boolean values (True/False).")
    exit()
print("Logical Operations:")
print("AND:", operator.and_(a, b))
print("OR:", operator.or_(a, b))
print("NOT a:", operator.not_(a))
print("NOT b:", operator.not_(b))'''


# Bitwise Operators
'''# 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a|b) #(OR)
print(a^b) #(XOR)
print(~a) #(NOT)
print(bin(a<<b)) #(Left Shift)
print(a>>b) #(Right Shift)'''


'''lcm program'''
# import math

# # Input two numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# # Calculate LCM using GCD
# lcm= abs(a * b) // math.gcd(a, b)

# print("LCM of", a, "and", b, "is:", lcm)


'''3.5 Assignment Operators ( =, +=, -=, *=, /=, %=, //=, **=)'''

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# a += b  # a = a + b
# print("After += operation, a =", a)
# b -= a  # b = b - a
# print("After -= operation, b =", b)
# a *= b  # a = a * b
# print("After *= operation, a =", a)
# b /= a  # b = b / a
# print("After /= operation, b =", b)
# a %= b
# print("after %= operation, a=", a)
# b //= a  # b = b // a
# print("After //= operation, b =", b)
# a **= b  # a = a ** b
# print("After **= operation, a =", a)


'''3.6 Identity Operators ( is , is not )'''

# a = [1, 2, 3]
# b = a
# c = [1,2,3]
# print(a is b)
# print(a == c)
# print(a is not c)
# print(a is c)

'''3.7 Membership Operators ( in , not in )'''
# a = [1, 2, 3, 4, 5]
# print(3 in a)  # True
# print(6 not in a)  # True



'''3.8 Operator Precedence and Associativity'''
# # Operator Precedence Example
# a = 2
# b = 3
# c = 4
# result = a + b * c  # Multiplication has higher precedence than addition
# print("Result of a + b * c:", result)  # Output: 20 (5 * 2 = 10, then 10 + 10 = 20)
# # # Associativity Example
# result = ((a + b) * c)  # Left to right associativity
# print("Result of (a + b) * c:", result)  # Output: 7 (
# # 10 - 5 = 5, then 5 + 2 = 7)
# # # Input and Output

# print(2 + 3 *  4)  # Output: 14
# print((2 + 3) *4)  # Output: 20


'''4. Control Flow Statements in Python'''
# 4.1 Conditional Statements
# Conditional statements allow decision-making based on conditions. They
# evaluate Boolean expressions and execute different code blocks accordingly.


'''remove duplictes from list'''
# l=input("Enter your list:").split()
# u_l=[]
# for item in l:
#     if item not in u_l:
#         u_l.append(item)
# print("List after removing duplicates:", u_l)


'''🔹 if Statement'''
# a = int(input("Enter a number "))
# if a >= 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")




# a = int(input("Enter a number: "))
# if a > 1:
#     for i in range(2, a):
#         if a % i == 0:
#             print(a, "is not a prime number")
#             break
#     else:
#         print(a, "is a prime number")
# else:
#     print(a, "is not a prime number")


'''🔹 if-else Statement'''
# a = int(input("Enter a number odd or even: "))
# if a % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

'''🔹 if-elif-else Statement'''
# a = int(input("Enter a number: "))
# if a >90:
#     print("Grade A")
# elif a > 80:
#     print("Grade B")
# elif a > 70:
#     print("Grade C")
# elif a > 60:
#     print("Grade D")
# else:
#     print("Fail sorry you are not eligible for exam")
# year= int(input("Enter a number: "))
# if (year % 400==0):
#     print(year, "is a leap year")
# elif (year % 100==0):
#     print(year, "is not a leap year")
# elif (year % 4==0):
#     print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")

# def y(year):
#     return (year % 400 == 0) 
# year= int(input("Enter a year: "))
# if y(year):
#     print("This is a leap year")
# else:
#     print("This is not a leap year")

'''4.2 Looping in Python'''
# Looping allows you to execute a block of code repeatedly based on a condition or for a specific number of iterations.

'''🔹 for Loop'''
# n = input("Enter a number: ")
# for i in range(1, 11):
#  print(n, "x", i, "=", int(n) * i) # Output the multiplication table
# # for i in range(3):
#     print(n) # Output the number n three times name repetition
'''🔹 while Loop'''
# num = str(input("Enter a number: "))
# count = 1
# while count <=num:
#     print(count)
#     count += 1  # Increment the count to avoid infinite loop

'''alphabets from A to Z'''
# letter = input("Enter a letter (A-Z): ").lower()
# ch = 'A'
# while ch <= letter:
#     print(ch)
#     ch = chr(ord(ch) + 1)  # Move to the next letter in the alphabet

'''4.3 Nested Loops'''
"""5. Alphabet Triangle"""
# n = int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(n + i): # reverse n - i
#         print(chr(65 + j), end=' ')  # Print letters starting from 'A'
#     print()  # Move to the next line after each row

""" Star Pyramid"""
# n = int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(n- i -1): # Reverse print (i)
#         print(" ", end=' ')
#     for j in range(2 * i + 1):#(2 * (n-i) - 1) reverse print 
#         print("*", end=' ')
#     print()  # Move to the next line after each row

# a=input("Is it raining? (True/False): ")

# b=a == "True"
# print("Is it raining?", b)
# print("Data type of b:", type(b))


"""Print your name and how many times you want to print it"""
# a = input("Enter a name: ")
# b=input("Enter a number: ")
# c = range(1, int(b) + 1)
# for i in c:
#     print(f"{a}")  # Print the name followed by the current number in the range

"""TAKE INPUT FROM USER AND PRINT IT"""
# rows=5
# a=input("Enter want to print like eg.,*, abc, 123: ")
# for i in range(1, rows +1):
#     print( i * a)  # Print the input string repeated i times
# s1="hello"
# s2="world"
# s3=s1 +" "+s2
# print(s3[::-1])  # Concatenate and print the two strings

# a=input("name: ")
# b=input("greeting")
# print(f"{b}, {a}")  # Print the greeting followed by the name
"""Repeat a word multiple times"""
# w=input("Enter a word: ")
# t= int(input("How many times repeat: "))
# c= (w + "\n")* t
# print(c)  # Print the word repeated t times

"""Count the number of words in a sentence"""
# a = input("Enter a sentence: ")
# length = len(a)
# print("The number of words in the sentence is:", length)  # Print the number of

"""words in the sentence"""
# a = input("Enter a sentence: ")
# last = a.split()[-1]  # Get the last word of the sentence
# print("The last word in the sentence is:", last)  # Print the last word

"""Concatenate two words with a space in between"""

# a = input("Enter a 1st word: ")
# b= input("Enter a 2nd word : ")
# c = a + " " + b  # Concatenate the two words with a space in between
# print("The concatenated string is:", c)  # Print the concatenated string

rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    print( rows * "*")  # Print asterisks in each row equal to the number of rows
    rows -= 1  # Decrease the number of asterisks in the next











    



















