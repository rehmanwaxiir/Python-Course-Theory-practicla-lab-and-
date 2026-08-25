# #String and conditional Statement
# #String: String is data type that stores a sequence of characters.
# #Basic Operations
# #1: Concatenation
# #"Hello"+"world"-> Helloworld
# #length of str
# l#en(str)
# str1="This is a sring."
# str2='Rehman waxiir.'
# str3="""This is a string"""
# #If we are creating some sentences in a string.
# str1="This is s string. we are creating it in Python."
# print(str1)
# #We use escap squence character such as; \n for next line. \t for tab
# #example
# str1="Hi, this is Rehman waxiir.\nStudies in CS,\tCommonded Language is Python."
# print(str1)
# #Concatenation (+)
# str1="Rehman"
# str2="Waxiir"
# print(str1+str2)
# #Calculate the length of a string
# str1="Rehmanwaxiir"
# len1=len(str1)
# print(len1)
# #OR
# str1="Rehmanwaxiir"
# print(len(str1))

# #INDEXING

# str="REHMAN WAXIIR"
# ch=str[4]
# print(ch)
# ch=str[7]
# print(ch)

# #Slicing: Accessing part of a string
# #str[startin_index: ending_index]
# #ending index does not allowed
# str="Rehman waxiir"
# ch=str[0:6]
# print(ch)
# ch=str[7:13]
# print(ch)
# ch=str[:6]
# print(ch)
# ch=str[7:]
# print(ch)
# print(str[0:6]) #Same as the upper mention output

# #Negative Slicing
# str="Waxiir"
# print(str[-4:-1])
# print(str[-6:])

# #String Functions
# #example
# #str.endswith("end of string").# returns true if string end with substr
# str="I am a coder"
# print(str.endswith("er"))# Returned True
# str1="I am studying in Python from Youtube"
# print(str1.endswith("tub")) #Returned False

# #Capitalized function,it for 1st Character of string to make capital.// str.capitalize()
# str1="i am studying in Python from Youtube.also studies in ML"
# str1=str1.capitalize()
# print(str1)

# #Replace Function: replace old values by new values(old, new)#replaces all occurrences of old.// str.replace(old,new)
# str2=" I am a coder, and i well create some big real life projects."
# print(str2.replace("a","e"))
# print(str2.replace("code","python developer"))

# #Find Function: returns 1st index of 1st occurer
# str2=" I am a coder, and i well create some big real life projects."
# print(str2.find("p"))
# print(str2.find("real"))

# #Count function: Counts the occurrence of substr.//str.count("i")
# str2=" I am a coder, and i well create some big real life projects."
# print(str2.count("i"))
# print(str2.count("real"))

# #LET'S SOLVE PRACTICE QUESTIONS
# #Q NO 1:Write a program to input user first name and print its length.
# name=input("Enter your name:")
# print("length of your name is",len(name))
# OR
# len=len(name)
# print("length of your name is ",len)

# #Q NO 2: Write a program to find the occurrence of '$' of a string.
# str3="Hi, This $is Rehman$,belongs $from tribal area's ."
# print(str3.count("$"))

# #CONDITIONAL STATEMENTS
# #if-elif-else(SYNTAX)
# #if(condition)
# #statement1
# #elif(condition):
# #statement2
# #else:
# #statementN
# #let's practice 
# #Uses if condition
# age=18.100
# if(age>=18):
#     print("you can apply:")

# # Uses of elif condition
# light="pink"
# if(light=="red"):
#     print("stop")  #indentation(four propor spaces)
# elif(light=="green"):
#     print("go")
# elif(light=="Yellow"):
#     print("look")

# # Uses of else Condition
# light="pink"
# if(light=="red"):
#     print("stop")
# elif(light=="green"):
#     print("go")
# elif(light=="Yellow"):
#     print("look")

# else:
#     print("The traffic light is broken.")

# #Practice problem: Uses 
# points=int(input("Enter the Drivers license point: "))
# if(points >=24):
#     Grade="A"
# elif(points >=20 and points < 24):
#     Grade="B"
# elif(points >=16 and points < 20):   
#     Grade="C"
# elif(points >=12 and points < 16):
#     Grade="D"       
# else:
#     Grade="The Driver liscens are banned for one year"
# print("The driver Grade is: ", Grade) 

# nesting loop
# age=int(input("Enter driver age:"))
# #nesting
# if(age>=18):
#     if(age>=80):
#         print("can't drive")
#     else:
#         print("can drive")
# else:
#     print("can't drive")            

# # Let's solve practice questions
# # Write a program to check if a number enter by the user is odd or even
# num=int(input("Enter a number:"))
# if(num%2==0):
#     print("Even")
# else:
#     print("Odd")

# #Q No 2:Write a program to find the greatest of 3 numbers entered by the user.
# a1=int(input("Enter first number:"))
# b1=int(input("Enter second number:"))
# c1=int(input("Enter thord number:"))
# if(a1 >= b1 and a1>=c1 ):
#     print("a1 are the greatest:",a1)
# elif(b1 >= a1 and b1>= c1):
#     print("b1 are the greatest:",b1)
# else:
#     print("c1 are the greatest:",c1)        

# Q NO 3: Write a program to check if a number is a multiple of 7 or not.
# x=int(input("Enter a number:"))
# if(x % 7==0):
#     print("Multiple of 7.")
# else:
#     print("not a multiple of 7")
