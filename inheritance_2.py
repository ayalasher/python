#We are going to look into another case of inheritance
# Python is a part of ML and we are going to see alot about it 

class person :
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname 

    # Indentation must be followed corectly
    def fullname(self) : 
            print(self.firstname,self.lastname)


x = person("ayal","asher")

x.fullname() #The output is going to be ayal asher - the two inputs itno the parameters

# Creating a new class 
# When doing this ensure yo put the parent class as a parameter -- This is where the inheritance occurs 


# The child class 
# pass is going to be simple way out 
#This is basic and is going to allow the new class to inherit everything from the parent one 
class child (person) :
     
     #Note that we can remove the pass and work with another sort of thing like the __init__ function
    #  When you add the __init__ function there , it prevents the inheritance of the original __init__ function from the parent class 
    # but you can call the __init__ function by adding a __init__ function call to the 
     def __init__(self, fname, lname):
          person.__init__(self,fname, lname)

y = child("asher","ayal")
y.fullname()  #Output is going to be asher ayal
    