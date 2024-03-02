#From here we are going tpo look at the __Str__ function in working with classes in python 
#This function decides what should be returned when the class object is represented b a string 
#If the __str__ function is not set the the string representation of the object is returned


#the one below is going to be a representation without the string function 
class person :
    def __init__(self,name, age ):
        self.name = name
        self.age = age 

    def __str__(self):
        return f"{self.name}({self.age})"
        
    
#The object name followed by the class name then the data elements to be put into the class 
# do not forget that indentation is something very important 
P1 = person("julius",45)

# print(P1.name)
# print(P1.age)

print(P1)

    