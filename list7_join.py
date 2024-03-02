#we are going to look into joining of lists
fruits = [ "apple", "mango" , "banana" , "watermelon " ,"kiwi" ,"orange" , "lemon"]

cars = list(("cayenne","cybertruck",'s550'))

fruitcar = fruits + cars 
#joining two lists using concatenation
print(fruitcar)


fruits.extend(cars)
print(fruits)


#Using the for loop with append
for x in fruits:
    cars.append(x)
    print(cars)

