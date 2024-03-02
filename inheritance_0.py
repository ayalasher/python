#we are going to look at inheritanceas something that happens in OOP 
#inbheritance is when a new class is created and the new class can take up the objects that were in another class


#class creation 
class person :
    #terminatorwill be at the creation of the class and the creation of the __init__ function which calls itself when an object is created 
    def __init__(self,name,age):
        self.name = name
        self.age = age 

# object creation 
p1 = person("maxwel",19) 

# Output of one of the properties of the class 
print(p1.name)
        