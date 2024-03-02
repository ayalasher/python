#python does not have arrays but you can use lists like arrays
#although you will have to add numpy to your computer inorder for that to be possible


cars = ["cayenne","fortuner","X6"]

#changing the value
cars[0] = "cybetruck"

#normal output
print(cars)


#printing the type
print(type(cars))

#getting a specific  Item form the list
print(cars[0])

#getting the length
print(len(cars))

#append can be sued to add elements to the end of the list/array
cars.append("model-x")
print(cars)


#pop for removing
#you have to specify the index position of the element that you wabt to pop 
cars.pop(0)

print(cars)

#remove can be used for removing but you have to use the itrem itself inside the double quotes