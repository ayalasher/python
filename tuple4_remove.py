#we are looking into how you remove Items in a tuple 
fruits = ( "apple", "mango" , "banana" , "watermelon " ,"kiwi" ,"orange" , "lemon")

#changing the tuple to a list
y = list(fruits)

#removing of the Item
y.remove("apple")

#re-converting the list back to a tuple     
fruits = tuple(y)

print(fruits)

#You can use del to delete the entire tuple

#Unpacking is the next thing we look into
