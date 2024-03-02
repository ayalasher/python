#we are going to look at the various ways of adding data to arrays
fruits = [ "apple", "mango" , "banana" , "watermelon " ,"kiwi" ,"orange" , "lemon"]

print(fruits)

#adds items to a list in the end of the list
fruits.append("tangerine")
print(fruits)

#insert requites you to specify the index where the new Item should be added
fruits.insert(1,"peach")
print(fruits)

#extend can be used to add one list to another
#You can even add a list to a tuple...It is not neccesarily for lists only
Ccars = ["cayyene","fortuner","mercedes"]
Ecars = ["model-X","model-S","cybertruck"]

Ccars.extend(Ecars)

print(Ccars)