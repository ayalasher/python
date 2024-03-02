#This is where we do te real inheritance 

class person :
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        
        def fullname(self) :
            print(self.firstname,self.lastname)


data = person("ayal","asher")

data.fullname()
#prints ayal asher -- similar to the calling of a function so you have to use the brackets at the end otherwise your code is not going to run 
        