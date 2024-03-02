#we are going to look into how you can change the data in tuple
#tuples are unchangable
#The other way is by converting the tuple to a list, changing the value then convert the list to a tuple
fruits = ( "apple", "mango" , "banana" , "watermelon " ,"kiwi" ,"orange" , "lemon")

#changing the tuple to a list
y = list(fruits)

#changing of the value of the list
y[0] = "tangerine"

#converting the  list back to  a tuple
fruits = tuple(y)

print(fruits)

