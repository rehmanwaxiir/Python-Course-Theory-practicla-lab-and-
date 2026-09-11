"""
OOP:
OOP(Object Oriented Programming)
Use objects in code
To map with real world scenarios.
In OOPs use two concept
1: Class(class is a blueprint for creating objects.)
Creating class
Class Student:
name="Rehman"
2:Object(Object can be anything)
Creating object(instance)
s1=Student(). s1 is an object 
print(s1.name)
take simple example
"""
class Employee:
    name="Amjid"
    age=25
    # name="Fatma"
e1=Employee()
print(e1.name)
print(e1.age)

"""
Constructor: All classes have a function called --init--(), which is always executed when the object is being intiated.
Creating class: class Employee. def--init--(self, fullname):
self.name=fullname

Creating object: e1=Student("Amjid")
print(s1.name)
--init--Function(Always executed when  the class is being initiated)
'The self parameter is a reference to the current instance of the class, and 
is used to access variables that belongs to the class.

"""
class Car:
    def __init__(self,name,model,capacity):
        self.name=name
        self.model=model
        self.capacity=capacity
        print("This is an initialization function")
c1=Car("Civic","2020","capacity")
print("name is:",c1.name)
print("model is:",c1.model) 
print("seat",c1.capacity,"is 4") 
# print()      
c2=Car("Carolla.",'2023.' ,"capacity")
print("name :",c2.name,"model:",c2.model,"seat", c2.capacity,"is 4")

"""
Attributes:
class.attributes(common attributes write one times)
object.attributes(write attributes multiple times for objects )

"""
class Car:
    Group_name="Khan group"#class attribute
    def __init__(self,name,model,seat_capacity):
        self.name=name#object attribute
        self.model=model
        self.capacity=seat_capacity
        print("This is an initialization function")
c1=Car("Civic","2020","seat capacity:")
print("name:",c1.name)
print("model:",c1.model) 
print(c1.capacity,"4")
print(c1.Group_name)
print(Car.Group_name)# print with class name and class attribute 

"""
Methods: Methods are functions that belong to objects.
Create class:
class Car:
    def __init__(self,name):
        self.name=name
        Method.
        def welcome(self):
            print("welcome to Khan group and company",self.name)
creating object:
c1=car("Xeli")
c1.welcome()            
"""
class Car:
    def __init__(self,name,color):
        self.name=name
        self.color=color
        
    def welcome(self):
        print("welcome to Khan group and company,",self.name)

    def color(self):
        return self.color
c1=Car("Xeli","Off white")
c1.welcome() 
print(c1.color)

"""
Let's solve practice Question
Create student class that takes name and marks of three subjects as arguments in constructor.
Then create a method to print the average.
"""    
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hi,",self.name,"Your avg score is:",sum/3)
s1=Student("Haroon",[97,98,99])
# print(s1.name)
s1.get_avg()                

"""
Abstraction: Hiding the implementation detail of a class and only showing the essential features to the user.
"""
class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    
    def start(self):
        self.clutch=True
        self.acc=True
        self.brk=True
        print("Car started...")
c1=Car()
c1.start()

