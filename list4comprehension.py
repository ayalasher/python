#We will look into comprehension 
#list comprehension allows someone to create a new list from an already existing one    

cars = list(("cayenne","prado","ford-ranger","crown"))
sedancars = [] 
sedancars1 = []

#using the for statement
print("Using the for statement")

for x in cars :
    if "c" in x:
        sedancars.append(x)

        print(sedancars)


#using the comprehension method
print("Usin the comprehension method")
sedancars1 = [y for y in cars if "c" in y ]
print(sedancars1)