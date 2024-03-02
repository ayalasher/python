#lists is the concept of study

#They are used to store multiple elements in a single variable 

#They are ordered
#They have indexing like arrays--ordered
#When new items are added , they will be added at the end of the list
#They are changeable and allow duplicate values
#They are made using square brackets
#They can also have items with the same value

fruits = [ "apple", "mango" , "banana" , "watermelon " ,"kiwi" ,"orange" , "lemon"]
print(fruits)

#list length
print(len(fruits))

# A list can have any data type whetehr separate or combined
#The data type for a list is 'list'
print(type(fruits))

#Method 2 of making lists 
cars =list(("cayenne","cybertruck","fortuner"))
print(cars)

#accessing list items
#This will be similar to accessing the elements of an Array
print(fruits[0])
print(cars[0])

#we can also use negative indexing with -1 being the last item in the list and -2 being the second last elment in the list
print(cars[-1])

#range
print(fruits[2:5]) #from 2 to 4 ... Those are three

#in case the first number is left out output will start from the beginning
print(fruits[:5])

#in case the second number is left out The output will be from start point to the end
print(fruits[2:])

#negative indexing
print(fruits[-4:-2])

#checking -- we will use the if function and in
if "apple" in fruits : 
    print("The item is present ! ")

else :
    print("The Item is not present")

#changing will be similar to changing the values of an array
fruits[0] = "Tangerine"
print(fruits[0])

#changing a range of items
fruits[1:3] = ["Pinaapple","Guava"]
print(fruits[1:3])

#Incase you insert more items than the Items removed , The extra item will be after the replacement one..the remaining items are pushed to the left
cars[1:3] = ["model-x"]

cars.insert(1,"harrier")

print(cars)
