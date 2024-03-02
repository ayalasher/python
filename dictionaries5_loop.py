#we are going to look itno the various ways you can loop throgh the Items in a 
details = {
    "brand" : "Tesla" ,
    "model" : "cybertruck" ,  
    "year" : 2024 , 
    "color" : "gloss-black" , 
    "warranty-years" : 10 , 
    "autopilot" : True
}


print("KEYS !! ")
for x in details : 
    print(x)#output is the key Items of the dictionary

#another method for keys is as follows
    
for w in details.keys() :
    print(w)


print("VALUES !! ")
#to print all the values do the below
for y in details : 
    print(details[y])

#another method for the values is shown below
for z in details.values():
    print(z)
