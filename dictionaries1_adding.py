#we are going to look into how you can add Items to dictionaries

details = {
    "brand" : "Tesla" ,
    "model" : "cybertruck" ,  
    "year" : 2024
}
print(details)

#mthod 1
x = details["model"]
print(x)

#using get()
y = details.get("brand")
print(y)


#keys() returna all the keys in the dictionary
z = details.keys()
print(z)#as a dictionary sort of thing

#when you add a new Item to the dictionary the keys will also be updated
details["color"] = "gloss black"
print(z)

#values on the other side returns all the value sin the dictionary
a = details.values()
print(a)

#when change happens , the change will also be noticed
details["color"] = "army green"
print(a)

details["price"] = 100000

print(details)
print(a)

#items returns all the items in a key-value pair kind of way
b = details.items()
#even after changing of Items or adding new items..the dictionary is going to update Itself
print(b)


