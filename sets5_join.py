#we are going to look at how you can join two sets together

Ccars = {"volvo","prius","audi"}
Ecars = {"model-X","model-s","cybertruck"}

Acars = Ccars.union(Ecars)

print(Acars)#The order of the output of the cars is going to be irregular

#Update() can also be used 

#intersection_update can only add an Item that is in both The sets 

#intersection() is used to bring out a new set which will have Items that are in both of The old sets

#symetric_difference_update() will output a set that keeps all the elements but not the duplicatesThe set is not a new set

#symetric_difference() creates a new set that will heve elements that  are not present in both sets 
#note that True and 1 are considered to be similar