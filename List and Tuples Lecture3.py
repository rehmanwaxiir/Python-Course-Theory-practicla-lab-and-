# LIST AND TOUPLE:
# A built-in data types that stores set of values.
# It can store elements of different types(integers,float,string etc)
# marks=[90,,70,89,56]#marks[0],marks[1]..
#student=["kamran",83,"waziristan"]#student[0],student[1]..
#student[0]"Arjun"#allowed n python
#len(student)#returns length
# marks=[95,89,70.90,78,67]
# print(marks)
# print(type(marks))
# INDEX same as in string AND LIST SLICING:Similar to String Slicing
# print(marks[0])
# print(marks[0:3])
# print(marks[:4])
# print(marks[0:])
# print(marks[-3-1])

# student=["Rehman",78,"Waziristan"]
# print(student)
# Note: String are immutable in Python and List are mutable(which can change)
# str="Rehman"
# print(str[1])
# str[0]="a"# error
# student=["Rehman",65,"Waxiristan"]
# print(student[1])
# student[0]="Fatma"
# print(student)

#LIST SLICING: Similar to String Slicing
# list_name[starting_index:ending_index]#ending index is not included
#print(marks[0])
# print(marks[0:3])
# print(marks[:4])
# print(marks[0:])
# print(marks[-3-1])

# LIST METHOD
# list=[22,21,3]
# list.append(4)#adds one element at the end [22,21,3,24]
# list.append(24)
# print(list)

# list.sort()#sorts in ascending order[3,21,22,24]
#Ascending order
# list.sort()
# print(list)

#Decending order
# list.sort(reverse=True)
# print(list)

# list.reverse()#reverse list [3,21,22]
# list=['a','b','c','d','e','f']#->['f','e','d','c','b','a']
# list.reverse()
# print(list)

#Insert method:list.insert(index,element) #insert element at index
# list=[39,90,78,88]#inser 66 at index 2->[39,90,66,78,88]
# list.insert(2,66)
# print(list)

#Remove method: list.remove(1) #remove first occurrence of element
# list=[33,44,55,66]
# list.remove(44)
# print(list)

# POP Method: list.pop(index) #removes element at index
# list2=[332,454,676,787]
# list2.pop(2)
# print(list2) #print[332,454,787] 

#Touple in Python
#A built-in data type that lets us create immutable seuences of values.
# tup=(12,13,44,78) #tup[0],tup[1]..
# tup[0]=5 # That's not allowed in Python
# tup=() are allowed and print an empty touple()
# tup2=(1,)# comma(,) are necessary for a single touple
# tup3=(1,2,3)
# tup=(12,13,34,55)
# print(type(tup))
# print(tup[1]) #returns 13
#tup[0]=22 #error occur, it does not like  list
#TOUPLE METHODS: 
#tup=(21,34,1,22,1)
#tup.index(element) #returns inex of first occurrence  tup.index(1) is 34
# tup.count(element) #counts total occurrences  tup.count(1) is 2 times
# tup=(21,3,1,22,1)
# print(tup.index(3))

# tup1=(21,3,1,22,1)
# print(tup1.count(1)) #i occurs two times

# Let's Practic:
# Qno 1: Write a program to ask the user to enter namesof their 3 favorite movies and store  them in a list.
# movies=[]
# mov1=input("Enter first favorite movie.")
# mov2=input("Enter second favorite movie.")
# mov3=input("Enter third favorite movie.")
# # list=["str1","str2","str3"]
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

# #in short
# movies=[]
# movies.append(input("Enter first favorite movie:"))
# movies.append(input("Enter second favorite movie:"))
# movies.append(input("Enter third favorite movie:"))
# print(movies)

# Qno2: Write a program to check if a list contains a palindrome of elements.
# let's
# list1=[1,2,3,4,3,2,1]
# list2=[1,2,3,4,5,6]
# copy_list1=list1.copy()
# copy_list1.reverse()
# if(copy_list1==list1):
#     print("Palandrome")
# else:
#     print("Not a palindrome")
# 
# Qno 3: Write a program to count the number of students with the "A" grade in the following touple.
# ["C","D","A","A","B","B","A"]
# And store the above values in a list and sort them from "A" to"D".
# grade=['C','D','A','A','B','B','A'] 
# print(grade.count('A')) 
# list_of_student=["C","D","A","A","B","B","A"]
# list_of_student.sort()
# print(list_of_student)