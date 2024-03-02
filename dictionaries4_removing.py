#We are going to remove some Items from the dictionary
#

details = {
    "brand" : "Tesla" ,
    "model" : "cybertruck" ,  
    "year" : 2024 , 
    "color" : "gloss-black" , 
    "warranty-years" : 10 , 
    "autopilot" : True
}

#basic output
print(details)

#When pop() is used , The last Item is removed from the dictionary
details.pop("year") #remove the  year of the car

print(details)

#popitem()
details.popitem()#removes the autopilot
print(details)

#using del
#usind del without specifying the  key will lea dto the whole dictionary beign deleted
del details["warranty-years"]#removes warranty-years
print(details)

#using clear completely deletes the Items insid ethe dictionary
details.clear()#disable THis and follow from the top 
print(details)