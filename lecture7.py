#File I/O in python
# Python can be used to perform operations on a file.(read and write data)
#Types of all files
#1:Text Files: txt,.docx(Stored characters. like,MS documents stored etc), .log(stored system log files) etc
# 2:Binary Files:(which can't stored data in character form) .mp4, .mov, .png, .jpeg etc
#Opeartions
# 1: Open, read and close file
# We have to open a file before reading or writing.
# file=open("File_name","mode")
# suppose file name= personal.txt
# file mode='r' read mode, 'w' write mode, etc
# let take example
file=open("personal.txt","r")
# data=file.read()
line1=file.readline()
print(line1)
line2=file.readline()
print(line2)
file.close()
# data=file.readline()
#Write
file=open("personal.txt","w")#Replace all previous data by new data
file.write("Hi, this is Rehman waxiir\nLearning Python\nIf you like Rehmna waxiir Pyhton course then follow my account.")

#If we add new data in recent data, we use "a"mode
file=open("personal.txt","a")
file.write("\nand also rate my efforts")
file.close()

file=open("new.txt","w")#create nw file in the folder(FILE INPUT AND OUTPUT)
file.write("This is vaxiir")
# file.close()

#If we read and write in a same file, we will use "r+".(reading and writing)
#The stream is positioned at the begining of the file.
file=open("new.txt","r+")
file.write("Belong from tribal area's")#overwite the previous text
file.close()

# "w+" Open for reading an writing. the file is reated if it does not exist, otherwise the file truncated. the stream positioned at the begining of the file
file1=open("new.txt","w+")
print(file1.read())
file1.write("a new text.")#overwrite the previous txt
# print(file1.read())
file1.close()

#"a+"Open for reading and writing.The file is created if it does not exist.The stream is positioned at the end of the file.
file2=open("new.txt","a+")
file2.write(" This is n new file.")
file2.close()

#If we create a new file and writing in it.
file3=open("file2.txt","a+")
file3.write("This is a new file 2.")
file3.close()

with open("with_file.txt","r") as file:
    txt=file.read()
    print(txt)

with open("with_file.txt","w") as file:
    txt1=file.write("This is an overwrite by the previous data.")
    print(txt1)

#Deleting a file:
# Using the module
# Module(like a code library).
# import os
# os(operating system) is a module  
# If we want to delete a file, use os .remove("file name")
# import os
# os.remove("file2.txt")#remove file2.txt

#let's solve practice problem
# QNO1:Create a new file "problem.txt". Add the following data in the file.
with open ("problem.txt","w") as practice:
    practice.write("Hi everyne\nWe are learning lecture 7 about file input an output\nUsing Python\nAre you satisfied from my course.")
    practice.close()

# QNO2:Write a function that all occurrence of Python with MAD course.
def replace():
    with open ("problem.txt","r") as practice:
        data=practice.read()

    new_txt=data.replace("Python"," MAD course")
    print(new_txt)

    with open("problem.txt","w") as practice:
        practice.write(new_txt)

replace()        

# QN03: Search if the word "file" exists in the file or not
word="file"
with open("problem.txt","r") as practice:
    data=practice.read()
    if(data.find(word)!=-1):
        print("Found")
    else:
        print("Not found")        

# If we want to use function
def check_word():
    word="xyz"
    with open("problem.txt","r") as practice:
        data=practice.read()
        if(data.find(word)!=-1):
            print("Found")
        else:
            print("Not found")        
check_word()

# QNO4:WAF to find in which line of the file does the word "file" occur first.
# print-1 if the word not found
def check_word():
    word="file"
    data=True
    line_number=1
    with open("problem.txt","r") as practice:
        while data:
            data=practice.readline()
            if(word in data):
                print(line_number)
                return 
            line_number+=1
    return -1                

check_word()            

#If we search not existing word then print -1.
def check_word():
    word="xyz"
    data=True
    line_number=1
    with open("problem.txt","r") as practice:
        while data:
            data=practice.readline()
            if(word in data):
                print(line_number)
                return 
            line_number+=1
    return -1                

print(check_word())
#THE END OF THE CHAPTER 7 