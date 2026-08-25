#LOOPS IN PYTHON;
#Loops are used to repeat instructions.
#Two types of loop:
# 1:while loop
# 2:for loop
#let's start:
#simple program
# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")
# #print 5 times hello
# #if we want to print hello 5 times
# # i=1
# # while (i<=10):
# #     print("Waxiir")
# #     i+=1

# i=1
# while(i<=100):
#     print(i)
#     i+=1
# #print 5,4,3,2,1
# j=5
# while(j>=1):
#     print(j)
#     j-=1    

# Let's solve problem
# QNO 1: Print numbers from 5(except 5) to 200.
# n=6
# while(n<=200):
#     print(n)
#     n+=1

# QNO 2:print numbers from 200 to 5(5 should not included).
# n1=200
# while(n1>=6):
#     print(n1)
#     n1-=1

#QNO 3:Print the multiplication table of a number n.
practice_n=int(input("Enter any numbers:"))
n2=1
while(n2<=10):
    print(practice_n*n2)
    n2+=1

#QNO 4: Print the elements of the following list using a loop
#[2,3,4,66,7,78,98]
numbers=[2,3,4,55,60,23,50,33]
n3=0
while(n3<len(numbers)):
    print(numbers[n3])
    n3+=1

#QNO 5:
# Search for a number x in this touple using loop

practice_n=(2,3,4,55,60,23,50,33)
x=3
n4=60
while(n4<len(practice_n)):
    if(practice_n[n4]==x):
        print("X Found at index:", n4)
    n4+=1

#Break and Continue
#Break: used to terminate the loop when encountered.
#Continue: terminates execution in the current iteration and continues of the loop with the next iteration.
# i=1
# while i<=5:
#     print(i)
#     if(i==4):
#         break
#     i+=1
# print("end of a break loop ")

break_n=(3,4,6,2,9,60,89)
x1=60
n5=0
while n5<len(break_n):
    if(break_n[n5]==x1):
        print("x1 Found at index",n5)
        break
    else:
        print("Finding...")
    n5+=1

print("end of break loop")

#Continue
n6=0
while n6<=5:
    if(n6==4):
        n6+=1
        continue #skip the fourth number
    print(n6)
    n6+=1
print("end of continue loop")

#check for even numbers
print("The following are even numbers:")
n7=1
while n7<=20:
    if(n7%2!=0):
        n7+=1
        continue
    print(n7)
    n7+=1

#For loops in Python:
#Used for sequential traversal. For traversing list, string, tuples etc.
print("Print for loop:")
for_number=[70,54,31,60]
for val in for_number:
    print(val)

print("This is the example of list:")
cars=["TOYOTA","Honda Civic","Carulla","BMW"]
for val in cars:
    print(val)

#for string:
str="REHMAN WAXIIR"
for char in str:
    print(char)

#use of else
str="Amjid"
for char in str:
    print(char)
else:
    print("End for loop with else")

#if we search any string
str="Muhammad"
for char in str:
    if(char=='m'):
        print("found m")
        break
    print(char)
else:    
    print("End of search char.")

#QQNO 1: PRACTICE QUESTIONS USNIG FOR:
#Print the elements of the following list using loop:
Practice_for=[1,4,60,34,56,52,12,99,90,43,55]
for val in Practice_for:
    print(val)

# Q NO2:Search for a number  in the tuple using loop:
practice_for2=(1,4,60,34,56,52,12,99,43,77,55)
x=55
idx=0
for num in practice_for2:
    if(num==x):
        print("X are found at index:",idx)
        break
    idx+=1

#RANGE():
#Range functions returns a seuence of a numbers,starting from 0 by default,and increments by 1 by default, and stop before a specified number.
# range(start?,stop,step?)
#Three method to write a range functions()
# 1: for el in range(7):
#     print(el)
# 2: for el in range(1,7):
#     print(el)
# 3: for el in range(1,7,4):
#     print(el)
#simple:
print(range(7))
#OR
print("This is first method.")
seq=range(6)
for n in seq:
    print(n)
#OR Simple
for n in range(9):
    print(n)

# Method 2:
print("This is  second method.")
seq=range(2,6)
for n in seq:
    print(n)

# Method 3:
print("This is third method.")
seq1=range(2,12,4)#range(start,stop,step)
for n in seq1:
    print(n)

#Practice Questions using for and range:
# QNO 1:Print numbers from 5 to 150.
p_range=range(5,151)
for p_n in p_range:
    print(p_n) 

#QNO 2: Print numbers from 150 to 5.
p_range2=range(150,4,-1)
for p_n2 in p_range2:
    print(p_n2)    

#QNO3: Print the multiplication table of a number n.
numbers=int(input("Enter numbers:"))
p_range3=range(2,10)
for p_n3 in p_range3:
    print(numbers*p_n3)

#PASS Statement:
# pass is a null statement that does nothing. It is used as a placeholder for future code.
# for el range (4):
#     pass
seq2=range(7)
for s in seq2:
    pass
print("Here we are doing some work.")
        
#Qno 1: Write a program to finf the sum of first n numbers(using while)
n=20
sum=0
for i in range(1,n+1):
    sum+=i

print("Total numbers of sum=",sum)    

#Qno2: Write a program to find the factoril of first n numbers.(using for)
n=6
fact=1
i=1
while(i<=n):
    fact*=i
    i+=1
print("Total numbers of factorial=",fact)  

#In for:
n=6
fact=1
for i in range(1,n+1):
    fact*=i
print("factorial=",fact)    


