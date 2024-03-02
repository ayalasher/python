#in declaration of variables you only use the variable name and the data to be stored in it 
#note that case sensitivity applies in tha naming of variables
#The rules of variable naming are very similar to those of C++ and Java
#pyhton is smart enough to understand the data type being used

x = 5 
#note that string variables can eitehr be double quotes or single quotes
name = "ayal"
name1 = 'maxwel'
fullname = name + " " +name1
#incase you want to specify the data type you can use casting
#an example is as follows

age = int(19) #This will be taken as a number
age1 = str(19)#This will be taken as a string 
age2 = float(19)#This will be taken as a floating point number 

print(age)#number
print(age1)#string
print(age2)#floating point number

print(fullname)
#getting the type of a variable
print(type(age2))


print(x)
print(name)