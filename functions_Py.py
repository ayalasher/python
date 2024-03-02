#we are going to look at functions in python

#we are going to call a function that prints out "hello world"
def myfunc() :
    #def is the keyword for function craetion

    #then the name of the function
    #in the naming of the function we are going to use the same rules as the naming of variables in other programming languages
    print("hello world")


myfunc()  # calling of the function created


#arguments can be used to pass information into a functions 
print("The use of arguments in functions")

#Note that the "fname" is a parameter ...
#We can have multiple parameters and arguments
def siblings(fname , lname):
    print(fname+ "  " + lname)

#calling of the functions with the arguments inside them
#If the number of functions and arguments is not the same then you will get an errordev
siblings("maxwel","ayal")
siblings("molly","otwori")
siblings("owiti","omondi")