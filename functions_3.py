#we are going to learn more about functions here

def myfunction(food) :
    for x in  food:
        print(x)


fruits = ["apple","banana","mango"]
myfunction(fruits)


#return values 
def mynos(y ):
    return y + 10 


print(mynos(4))
print(mynos(15))
print(mynos(22))

#pass can also be used after the function declaration incase you don't want the function to do any thing in particular

#positional arguments 

def parguments(a , /) :
    print(a)
parguments(3)#The output is going to be a three 


