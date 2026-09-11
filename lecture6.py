#Function in Python
#Block of statement that perform a sepcific task.
#def func_name(parameter 1, parameter 2...): //function definition
#return value
#func_name(arg1,arg2..)#function call
#Simple
a=2
b=3
sum=a+b
print(sum)
#if we add another some
a=4
b=20
sum=a+b
print(sum)
#we need to write more lines of code
#Reduced repitation of the same code.

def sum(a,b):
    sum=a+b
    print(sum)
    return sum
sum(12,2)
sum(90,990)

#OR
def calculator(a,b):
    return a+b
sum=calculator(12,2)
print(sum)

def calavg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg
calavg(69,51,56)

def calprcnt(a,b,c,d,e,f):
    if(a==0):
        print("a is Null.")
    sum=a+b+c+d+e+f
    prcnt=(sum*100)/600
    print(prcnt)
    return prcnt
calprcnt(58,71,48,69,51,56)

#Functions in Python.
#Built-in Functions.
# print()
# len()
# type()
# range()

# User Defined functions
def user_defined(a=2,b=6):
    print(a+b)
    return a+b
user_defined()

#Practice problems
# QNO1:WAf to print the length of a list.(list is the parameter)
subjects=('phy','che','AI','COAL')
Teachers=("Salman","Afnan","Zohan","Amjid")
def print_len(subjects):
    print(len(subjects))
    
print_len(subjects)
print_len(Teachers)

#Write a Functions to print the elements of a list in a single line.(list is the parameter)

course=('phy','che','AI','COAL','DB')
# print(course[0],end=" ")#print 'phy'
# print(course[1],end=" ")#print 'che'
# print(course[2],end=" ")#print 'AI'

def print_len(list):
    for item in list:
        print(item,end=" ")

print_len(subjects)    

#WAF to find the factorial of n.(n is the parameter)
n=5
def calculat_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
        print(fact)

calculat_fact(6)    

#Write a program to convert Darham to PKR
def converter(darham_val):
    pkr_val=darham_val*76.78
    print(darham_val,"Darham=",pkr_val,"PKR")
    # print(pkr)

converter(3453)    

#WAF to print a number enter by a user that give o/p the states of a number
num=int(input("Enter a number."))
def number_status():
    if(num%2==0):
        print("The number is Even.")
    else:    
        print("The number is Odd.") 
number_status()

#RECURSION:
# When a function calls itself repeatedly.
# Loops and recursion are nearly related toeach other.
#recursive Functions
list={'The human behaviour','AI expert','Intellectual'}
def show(list):
    if(list==0):
        return
    show(list-1)
    print(list)
    
show(10)

# OR

def cal_factorial(fact):
    if(fact==0 or fact==1):
        return 1
    else:
        return fact*cal_factorial(fact-1)
        
print(cal_factorial(4))#return 24

#PRACTICE QUESTIONS:
#QNO1: Write a recursive function to calculate the sum of first n natural numbers.

def cal_sum(n):
    if(n==0):
        return 0
    # print(n)
    return cal_sum(n-1)+n
    
sum=cal_sum(9)   
print(sum)

# QNO2: Write a recursive function to print all elements in a list.
books=["The human behaviuor","AI Expert","Intellectual"]

def print_list(list,index=0):
    if(index==len(list)):
        return
    print(list[index])
    print_list(list,index+1)

print_list(books)    

    