#accessing The elements in a tuple
fruits = ( "apple", "mango" , "banana" , "watermelon " ,"kiwi" ,"orange" , "lemon")
print(fruits)
#use of indexing
print(fruits[1])

#use of negative indexing
print(fruits[-1]) #The last Item of the tuple while -2 is the second last element

#range of indexing
print(fruits[2:5])

#from beginning to the point
print(fruits[:4])

#from a point to te end
print(fruits[3:])

#negative indexing with range
print(fruits[-4:-1])

#checking if  an Item exists in a tuple

if "apple" in fruits :
    print("The Item is available in the tuple ")
else: 
    print("The Item in the is not available in the tuple")