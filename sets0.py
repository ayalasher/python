#sets...sets ...sets
#sets are written using curly brackets  {}
#tuples use normal brackets ()
#lists use square brackets []
#sets are unordered , unchangable , and not indexed thus cannot allow duplicate values
#True and 1 are considered as duplicates and cannot be stored in one set
# false and zero are also considered as duplicate and cannot be stored in one set
fruits = {"apple","mango","banana","pineapple","tangerine"}#note that teh second apple is not going to be recognised as part of the set
quantity = {23,94,30,78,76}



print(quantity)
print(fruits)

#The length of a set 
print(len(fruits))

#sets can contain int str and boolean 
#They can also contain data types of different type
#the type comes out to sets
print(type(fruits))


#There is another way to create sets
cars = set(("volovo","mercedes","audi","cybertruck"))
print(cars)