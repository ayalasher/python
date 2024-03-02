#we are going to add some values to the tuple

fruits = ( "apple", "mango" , "banana" , "watermelon " ,"kiwi" ,"orange" , "lemon")
print(fruits)

#changing the tuple to a list 
y = list(fruits)

#appending of the LIIST
y.append("peach")

fruits = tuple(y)

print(fruits)