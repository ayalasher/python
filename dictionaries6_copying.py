#copying of the dictionaries
details = {
    "brand" : "Tesla" ,
    "model" : "cybertruck" ,  
    "year" : 2024 , 
    "color" : "gloss-black" , 
    "warranty-years" : 10 , 
    "autopilot" : True
}

#copy()
details1 = details.copy()

#using the dict method
details2 = dict(details)

print(details)

print(details1)

print(details2)