#we are going to look at how you can change the items in a dictionary

details = {
    "brand" : "Tesla" ,
    "model" : "cybertruck" , 
    "year" : 2024
}

#The traditional way 
details["year"] = 2023#This way can also be used to add The key-value element to the dictionary

print(details)

#The update() way
details.update({"model" :  "model-s-plaid"})#This can also be used to add key-value Items to the dictionary
#The output
print(details)