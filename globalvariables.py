#we aregoing to look inton global variables 
#global variables are variables that are created outside functions
#They can be used inside or outside functions
# A global variable 
age = str(19) 
def myfunc():
    #a local variable
    #The variable will only be used inside the function 
    age = str(20) 

    global Name
    Name = "ayal"

    #The "global" keywors can also be used to re)-assign a value of a variable inside a function 

    #To create a global variable inside afunction you can sue the "global" keyword 
    print("my brother is "+ age + " years old")
    

myfunc()

print("I am " + age + " years old ")