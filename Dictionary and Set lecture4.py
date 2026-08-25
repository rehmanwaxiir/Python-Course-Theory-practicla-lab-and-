# Dictionary in Python:
# Dictionaries are used to store values in key:values pairs
# They are unsorted, mutable(changeble)and don't allow duplicate keys
# dict={
#"name": "Rehman",
# "
# "cgpa": "3.4",
# "marks": [56,89,59],
# }
# dict["name"],dict["cgpa"],dict["marks"]
# dict["key"]="value" #to assign or add new
# StInfo={
#     #"key":"values",
# "name":"Rehman",
# "learning":"coding",
# "Subject":["java","OOPs","C++","Python"],
# "age": "21",
# "sgpa":"3.4",
# }
# print(StInfo)
# If we access dictionary values
# print(StInfo["name"])
# print(StInfo["Subject"])
# If we assign new values or change new value
# StInfo["sgpa"]="3.5"
# print(StInfo)
# StInfo["surname"]="Rehmanwaxiir"#add a new value
# print(StInfo)
null_dict={}
null_dict["name"]= "Rehmanwaxiir"
print(null_dict)

#Nested dictionary in Python
student={
    "name":"Rehmanwaxiir",
    "Score":{
        "Chem":89,
        "AI": 91,
        "coal":88,
    }
    # "name1":"Rehan",
    # "Scores":{
    #     "AI":90,
    #     "Database": 88,
    #     "Info Security": 92,
    # }
}
print(student)
# print(student["Score"])
# print(student["name"])
# print(student["name1"])
# print(student["Scores"])
print(student["Score"]["AI"])

# Dictionary Methods
# 1:myDict.keys() #returns all keys
# 2:myDict.values() #returns all values
# 3:myDict.items() #returns all(key, val)pairs as tuples
# 4:myDict.get("key") #returns the key according to value
# 5:myDict.update(newDict) #insert the specified items to the dictionary 

#If we are print all keys in dictionary
print(student.keys())#print all keys in Dict. returns all outer keys
#if we print total number of keys
print(len(student))
print(len(list(student.keys())))
print(student.values())#single function
print(list(student.values()))#two functions
print(len(student.values()))#two functions
print(len(list(student.values())))#three functions

print(student.items())#returns items in parenthesis
pairs=list(student.items())
print(pairs[0])
print(list(student.items()))
print(len(student.items()))
print(len(list(student.items())))

print(student.get("name"))# returns name
print(list(student.get("Score")))
print(len(student.get("Score")))
print(len(list(student.get("Score"))))

#update Method
student.update({"City":"Waziristan"})
print(student)
#OR
new_dict={"city": "Wazxiristan","age":19}
print(new_dict)
#if we are update the old key bu new
new_dict={"name":"Zoya Rehman","age":16}
student.update(new_dict)#update the previous name and age
print(student)

#SET IN PYTHON:
#Set is the collection of the unorderd items.
#Each element in the set must be unique and immutable.
#nums={1,2,3,4,5}
set2={1,2,2,3,3,4}#The repeated element stored only once, so it resolved to{1,2.3,4}
print(set2)
#null_set=set()#empty set syntax
set1={"1,2,3,4,5,6"}
print(set1)
set2={"Hello","Rehman, good morning", "Can i talk to you"}#we stores the strings values like"Hello".
print(set2)
print(type(set1))

print(len(set1))
print(len(set2))

#SET METHODS
# set.add(element)
# set.remove(element)
# set.clear()#empties the set
# set.pop()#remove a random value
#set.union(set2) #combines both set values and returns new
#set.intersection(set2)#combines common values and returns new
# Let's we create an empty set
collection= set() #empty set

collection.add(3)# we add some values
collection.add(4)
collection.add(9)
collection.add("Waxiir")#add any string but can't pass list
collection.add((5,6,7,8))#pass any touple
print(len(collection))
print(collection)

#Remove method:
#collection.remove(2)#error b/c there is no exist such element
collection.remove(3)#remove 3 
print(collection)

#Clear Method:
collection.clear()
print(collection)

print(len(collection))#length will be 0

#POP Method: stores any randon values.
collection={"Hello","Rehman","learns","Python"}
print(collection.pop())#choose any random value
print(collection.pop())#choose any random value
print(collection.pop())#choose any random value
print(collection.pop())#choose any random value

#Union set: combines both set values and returns new value
collection1={1,2,3,4,5,6}
collection2={3,6,2,7,7,8}
print(collection1.union(collection2))

#Intersection set: combines common values and returns new
collection1={1,2,3,4,50,80}
collection2={3,6,2,7,70,80}
print(collection1.intersection(collection2))
# LET'S PRACTICE THE PROBLEM:
# Q NO1:Store the following meanin in a python dictionary:
# table:"a piece of furniture","list of facts and figure"
#cat:"a small animal"
practice_dict={
    "table":("a piece of furniture","list of facts and figures"),
    "cat":"a small animal",
}
print(practice_dict)
#Q NO2: You are given a list of subjects for students.Assume one classroom is required for 1 subject.How many classroom are needed by all students
practice_subjects={
    "Phy","AI","COAL","DBMS","Phy","DBMS","AI","Probality & Statistics",
}
print(practice_subjects)
print(len(practice_subjects))

#Q NO3: Write  program to enter marks of 3 subjects from the user and store them in a dictionary.Add one by one .Use subject name as key and marks as value.

prctice_dict={
"phy":int(input("Enter phy marks:")),
"BD":int(input("Enter DB marks:")),
"AI":int(input("Enter AI marks:")),
}
print(prctice_dict)
#Q NO4: Figure out a way to store 5 and 5.0 as separate values in the set.
practice_set={5,"5.0"}
print(practice_set)
#OR To enter from user to print int and float and stored in a set.
practice_set1={ (
int(input("Enter integrs:")),
float(input("Enter float:")),
)
}
print(practice_set1)
#OR 
practice_set2={
("int",5),
("float",5.0),
}
print(practice_set2)
