#we are going to look at python lambda
#This is just a small function that allows many parameters but only one expression 
#It can have many parametersor only one parameter

#Two parameters
x = lambda a , b : a +  b 
print(x( 4 , 14))

#one parameter
y = lambda s : s *10 
print(y(40))

#using the lambda inside another function 
def number(n) : 
    return lambda i : i * n 
mydoubler = number(2)

print(mydoubler(11))