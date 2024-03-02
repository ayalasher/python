#dictionaries are going to be looked at
#They are used to store data in key-value pairs
#They are ordered changeable and do not allow duplicates
#similarly ro sets , They are also written in curly-brackets {}  

details = {
    "brand" : "Tesla" ,
    "model" : "cybertruck" , 
    #incase you have two similar key-value pairs which are similar.. the second one is going to overwrite the second one 
    "year" : 2023 , 
    "year" : 2024
}

#The second way to create adictionary looks quite simpler
details1 = dict(brand ="BMW" , Model= "X6" , year = 2018)

print(details)#They come out all in the key-value pair method in which you had been made

#to print out an individual key-value pair 

print(details["brand"])#The value of the key is going to be output

#The length function is also available
print(len(details))#outputs the number of Items put in the library


#dictionaries can have Items of any data type
#the type command being run will show that it is a dictionary 
print(type(details))
print(details1)
print(details1["brand"])
print(type(details1))