#we are going to look at some classes
#pythnon is an OOP language so we can have classes and objects


#creation of an object
class myclass : 
    x = 5


print(myclass)#The output is going to be main.myclass

#creating an object after the creation of a class

O1 = myclass()
#Name of the object do name of the class 
print(O1.x)#The output is going to be 5 // The five
O2 = myclass 
print(O2.x)


# The value of the x 

#The _init_ function is a function found in all classes and is executed when the class is being initiated
#You can say that the function is almost automatic 

class person :
    #the __init__ function is called everytime when the class is being used to create an object
    def __init__(self,name,age) :
        self.name = name
        self.age = age 

#here we store both the name and the age of the person 
P1 = person("john",40)

print(P1.name)
print(P1.age)

class car1 : 
    def __init__(self,model,brand) : 
        self.model = model 
        self.brand = brand  

C1 = car1("f-pace","jaguar")
        
print(C1.model)
print(C1.brand)
        