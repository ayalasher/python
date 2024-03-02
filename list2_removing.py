#We will be looking into how Itemscan be rmpoved froma list
fruits = [ "apple", "mango" , "banana" , "watermelon " ,"kiwi" ,"orange" , "lemon"]

print(fruits)

#remove specifies the item to be removed
fruits.remove("apple")#apple is removed
print(fruits)
#Note that incase remove is used and the item has a duplicate , Only the first Item duplicate will be removed

#pop is used to remove items with an index
fruits.pop(1) #banana is removed 
print(fruits)
#incase the index has not benn specified , The last item in the list is removed


# The  "del" keyword can be used to remove an Item from the list using  its index
del fruits[0]#mango has been removed
print(fruits)
#When "del" is used without specifying the index , The whole listis goinr to be deleted

#clear erases all the items of the list but the list still remains
fruits.clear()#all Items are cleared
print(fruits)