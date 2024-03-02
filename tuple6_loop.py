#we are going to look at how we can loop the tuples 

fruits = ("apple", "mango" , "banana" , "watermelon " ,"kiwi" ,"orange" , "lemon")

for x in fruits  : 
    #The output is going to be all the elements of the tuple individually 
    print(x)

print("Using The range and len property")

#looping using range and len 
fruits = ("apple", "mango" , "banana" , "watermelon " ,"kiwi" ,"orange" , "lemon")

for i in range(len(fruits)):
    print(fruits[i])

print("Using the while loop")
fruits = ("apple", "mango" , "banana" , "watermelon " ,"kiwi" ,"orange" , "lemon")
y = 0 
while y < len (fruits):
    print(fruits[y])
    y = y + 1 