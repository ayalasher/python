#we are going to look into how you can remove items from sets
#you can us eeither the reome or the discard method
cars = {"volvo","model-x","cayenne"}


#incase the mentioned Item does not  exist the compiler will raise an error
cars.remove("volvo")

#incase you use discard and the Item to be sused does not exist The compiler will not show
cars.discard("cayenne")



#pop can also be used to remove Items but it will pick any Item in the set
# clear()  is used to remove all the Items in a set and the set remains
#del() completely deletes the set completely 


print(cars)
print(cars)