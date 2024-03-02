#WE are going to look into methods 
# These are functions  that belong to objects


#Creation of the class
class person :
    #using of the __init__ function 
    #This function is called when the object is created frpm the function 


    # The self parameter 
# It is a reference to the current instance of the class and is used to access the variables in the class
# you can name it however you want but ensure that it is the first parameter in the parameters area of the function 
    def __init__(details,name,age):
        details.name = name 
        details.age = age
# creation of the function inside the 
    def myfunct(details):
        print("Hello my name is " + P1.name )

# Creation of the object 
#object -- class name -- the information to be input into the objects 
P1 = person("JOHN", 24)

#Modification of object properties
P1.age = 40


#Deleting of properties can be done using the "del" keyword
# del P1.age   -- when his is actie and the code is run it brings out an error

#deleting of objects can also be done using the "del" keyword 
# del P1 -- This is going to delete the whole object and not just one property

P1.myfunct()
print(P1.age)

#pass can also be used after class creation incase you want to leave the class empty
# This will not allow a display of an error 



