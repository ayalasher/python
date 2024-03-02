#Looping throgh lists is going to be done
fruits = [ "apple", "mango" , "banana" , "watermelon " ,"kiwi" ,"orange" , "lemon"]
print(fruits)
i=0

#using the "for" Loop
for x in fruits:
    print(x) #prints out all individual elements of the list



print("Using the range and len properties")
for i in range(len(fruits)):
    print(fruits[i])


#using the "while" loop
print("Looping using the while loop!")
x=0

while x < len(fruits): 
    print(fruits[x])
    x = x + 1 

#using comprehension
print("using the comprehension method ")
[print(y) for y in fruits]