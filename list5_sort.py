#we will be sorting things alphabetically 
#sorting is by ascending by default
#You should note that sorting is case sensitive...It begins with capital letters then down to small letters
fruits = [ "apple", "mango" , "banana" , "watermelon " ,"kiwi" ,"orange" , "lemon"]
#output of the list
print(fruits)

#sorting
fruits.sort()
#output of the sorted
print(fruits)

numbers = [12,34,5,67,9,78]
#sorting
numbers.sort()
#output of the ascending alphabetically sorted Items
print(numbers)

#sorting is automatically ascending
#To make the sorting descending you have to use reverse - true
numbers.sort(reverse=True)
print(numbers)

#reverse can be used to teverse the order of the items of a list 
fruits.reverse()
print(fruits)#the reverse of the alphabeticallys sorted LIst

