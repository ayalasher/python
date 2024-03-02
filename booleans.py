    #boolaens stand for two things TRues or false , one or zero 

print(10<15) #true
print(10>15) #false
print(10==15) #false

a = 200
b = 15

if b > a :
    print("b is greater than a ")

else :
    print("b is not greater than a ")

#booleans for strings and numerical values will alwaysreturn true
# however the number zero does not return true
#all  brackets , None and False return False    


#functions can also return a boolean
def myfunc() : 
    
    return False

print(myfunc())


def Myfunction() : 
    return False

if Myfunction():
    print("YES ! ")

else : 
    print("NO ! ")